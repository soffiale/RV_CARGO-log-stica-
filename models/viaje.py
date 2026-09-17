from database.conexion import obtener_conexion

def obtener_viajes():
    """Devuelve la lista completa de viajes programados desde la base de datos."""
    conexion = obtener_conexion()
    if not conexion:
        return []
    
    try:
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM viaje")
        viajes = cursor.fetchall()
        cursor.close()
        conexion.close()
        return viajes
    except Exception as e:
        print(f"Error al obtener viajes: {e}")
        return []

def agregar_viaje(origen, destino, fecha_salida, cliente, conductor, vehiculo, paquete):
    """Inserta un nuevo viaje relacionando las demás entidades en la base de datos."""
    conexion = obtener_conexion()
    if not conexion:
        return False
        
    try:
        cursor = conexion.cursor()
        sql = """INSERT INTO viaje (origen, destino, fecha_salida, cliente, conductor, vehiculo, paquete) 
                 VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        valores = (origen, destino, fecha_salida, cliente, conductor, vehiculo, paquete)
        
        cursor.execute(sql, valores)
        conexion.commit()
        cursor.close()
        conexion.close()
        return True
    except Exception as e:
        print(f"Error al agregar viaje: {e}")
        return False