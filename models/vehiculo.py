from database.conexion import obtener_conexion

def obtener_vehiculos():
    """Devuelve la lista completa de vehículos desde la base de datos."""
    conexion = obtener_conexion()
    if not conexion:
        return []
    
    try:
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM vehiculo")
        vehiculos = cursor.fetchall()
        cursor.close()
        conexion.close()
        return vehiculos
    except Exception as e:
        print(f"Error al obtener vehiculos: {e}")
        return []

def agregar_vehiculo(patente, marca, modelo, capacidad_carga_kg, tipo):
    """Inserta un nuevo vehículo en la base de datos."""
    conexion = obtener_conexion()
    if not conexion:
        return False
        
    try:
        cursor = conexion.cursor()
        sql = """INSERT INTO vehiculo (patente, marca, modelo, capacidad_carga_kg, tipo) 
                 VALUES (%s, %s, %s, %s, %s)"""
        valores = (patente, marca, modelo, capacidad_carga_kg, tipo)
        
        cursor.execute(sql, valores)
        conexion.commit()
        cursor.close()
        conexion.close()
        return True
    except Exception as e:
        print(f"Error al agregar vehiculo: {e}")
        return False