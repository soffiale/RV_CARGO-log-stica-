from database.conexion import obtener_conexion

def obtener_paquetes():
    """Devuelve la lista completa de paquetes desde la base de datos."""
    conexion = obtener_conexion()
    if not conexion:
        return []
    
    try:
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM paquete")
        paquetes = cursor.fetchall()
        cursor.close()
        conexion.close()
        return paquetes
    except Exception as e:
        print(f"Error al obtener paquetes: {e}")
        return []

def agregar_paquete(peso_kg, alto_cm, ancho_cm, largo_cm, descripcion):
    """Inserta un nuevo paquete en la base de datos."""
    conexion = obtener_conexion()
    if not conexion:
        return False
        
    try:
        cursor = conexion.cursor()
        sql = """INSERT INTO paquete (peso_kg, alto_cm, ancho_cm, largo_cm, descripcion) 
                 VALUES (%s, %s, %s, %s, %s)"""
        valores = (peso_kg, alto_cm, ancho_cm, largo_cm, descripcion)
        
        cursor.execute(sql, valores)
        conexion.commit()
        cursor.close()
        conexion.close()
        return True
    except Exception as e:
        print(f"Error al agregar paquete: {e}")
        return False