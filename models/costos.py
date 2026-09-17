from database.conexion import obtener_conexion

def obtener_costos():
    """Devuelve la lista completa de costos desde la base de datos."""
    conexion = obtener_conexion()
    if not conexion:
        return []
    
    try:
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM costos")
        costos = cursor.fetchall()
        cursor.close()
        conexion.close()
        return costos
    except Exception as e:
        print(f"Error al obtener costos: {e}")
        return []

def agregar_costo(concepto, costo_combustible, peajes, mantenimiento):
    """Inserta un nuevo costo en la base de datos."""
    conexion = obtener_conexion()
    if not conexion:
        return False
        
    try:
        cursor = conexion.cursor()
        sql = """INSERT INTO costos (concepto, costo_combustible, peajes, mantenimiento) 
                 VALUES (%s, %s, %s, %s)"""
        valores = (concepto, costo_combustible, peajes, mantenimiento)
        
        cursor.execute(sql, valores)
        conexion.commit()
        cursor.close()
        conexion.close()
        return True
    except Exception as e:
        print(f"Error al agregar costo: {e}")
        return False