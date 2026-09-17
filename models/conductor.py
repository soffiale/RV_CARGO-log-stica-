from database.conexion import obtener_conexion

def obtener_conductores():
    """Devuelve la lista completa de conductores desde la BD."""
    conexion = obtener_conexion()
    if not conexion:
        return []
    
    try:
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM conductor")
        conductores = cursor.fetchall()
        cursor.close()
        conexion.close()
        return conductores
    except Exception as e:
        print(f"Error al obtener conductores: {e}")
        return []

def agregar_conductor(nombre, apellido, dni, licencia, telefono):
    """Inserta un nuevo conductor en la base de datos."""
    conexion = obtener_conexion()
    if not conexion:
        return False
        
    try:
        cursor = conexion.cursor()
        sql = """INSERT INTO conductor (nombre, apellido, dni, licencia, telefono) 
                 VALUES (%s, %s, %s, %s, %s)"""
        valores = (nombre, apellido, dni, licencia, telefono)
        
        cursor.execute(sql, valores)
        conexion.commit()
        cursor.close()
        conexion.close()
        return True
    except Exception as e:
        print(f"Error al agregar conductor: {e}")
        return False