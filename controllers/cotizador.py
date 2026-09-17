import requests
from database.conexion import obtener_conexion
from models.costos import obtener_costos

def obtener_distancia_km(origen, destino):
    """
    Consulta las APIs públicas de Nominatim (OpenStreetMap) y OSRM
    para obtener las coordenadas geométricas y la distancia exacta por carretera.
    """
    try:
        # User-Agent requerido por la política de uso de Nominatim
        headers = {'User-Agent': 'RVCargoApp/1.0'}
        
        # 1. Geocodificación: Convertir nombres de ciudades/direcciones en coordenadas (lat, lon)
        res_origen = requests.get(
            f"https://nominatim.openstreetmap.org/search?q={origen}&format=json&limit=1", 
            headers=headers
        ).json()
        
        res_destino = requests.get(
            f"https://nominatim.openstreetmap.org/search?q={destino}&format=json&limit=1", 
            headers=headers
        ).json()
        
        # Validación: Si alguna dirección no devuelve coordenadas, se interrumpe
        if not res_origen or not res_destino:
            return 0.0

        # Extraer latitud y longitud de los resultados
        lat1, lon1 = res_origen[0]['lat'], res_origen[0]['lon']
        lat2, lon2 = res_destino[0]['lat'], res_destino[0]['lon']

        # 2. Enrutamiento con OSRM: Calcular la distancia real por ruta terrestre
        url_osrm = f"http://router.project-osrm.org/route/v1/driving/{lon1},{lat1};{lon2},{lat2}?overview=false"
        res_ruta = requests.get(url_osrm).json()

        # OSRM devuelve la distancia en metros; convertimos a kilómetros
        return round(res_ruta['routes'][0]['distance'] / 1000.0, 2)
        
    except Exception:
        # Retorno de seguridad en caso de fallos de red o APIs
        return 0.0


def procesar_cotizacion(origen, destino, horas_espera, paradas):
    """
    Procesa la cotización del viaje, aplica la regla de tarifas fija
    e inserta el presupuesto de forma segura en MySQL.
    """
    # 1. Obtención dinámica de costos base ($165 combustible + $45 mantenimiento = $210/km)
    lista_costos = obtener_costos()
    
    if lista_costos:
        costo_combustible = float(lista_costos[0].get('costo_combustible', 165))
        costo_desgaste = float(lista_costos[0].get('mantenimiento', 45))
    else:
        # Valores por defecto en caso de no conectar con el módulo de costos
        costo_combustible = 165.0
        costo_desgaste = 45.0

    # Tarifa unificada por kilómetro
    costo_km = costo_combustible + costo_desgaste

    # 2. Calcular la distancia del trayecto
    km = obtener_distancia_km(origen, destino)

    # 3. Cálculo del costo total (Nota: las paradas y horas de espera se registran pero no suman costo)
    total = round(km * costo_km, 2)

    # 4. Persistencia en MySQL (Uso de consultas parametrizadas %s para prevenir SQL Injection)
    conexion =(obtener_conexion)
    cursor = conexion.cursor()
    
    query = """
        INSERT INTO presupuestos (origen, destino, distancia_km, monto_total)
        VALUES (%s, %s, %s, %s)
    """
    # Los valores se pasan como tupla para garantizar la sanitización
    cursor.execute(query, (origen, destino, km, total))
    
    # Confirmar transacción en la base de datos
    conexion.commit()
    
    # Obtener el ID autonumérico generado para este presupuesto
    id_presupuesto = cursor.lastrowid
    
    # Liberar recursos y cerrar conexión
    cursor.close()
    conexion.close()

    # 5. Estructuración del diccionario de retorno (ideal para convertir a JSON)
    return {
        "id": id_presupuesto,
        "origen": origen,
        "destino": destino,
        "distancia_km": km,
        "costo_por_km": costo_km,
        "costo_distancia": total,
        "horas_espera": horas_espera,
        "paradas": paradas,
        "total": total
    }