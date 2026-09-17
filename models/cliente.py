from database.conexion import obtener_conexion

def obtener_clientes():
    """Devuelve la lista completa de clientes desde la base de datos."""
    conexion = obtener_conexion()
    if not conexion:
        return []
    
    try:
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM cliente")
        clientes = cursor.fetchall()
        cursor.close()
        conexion.close()
        return clientes
    except Exception as e:
        print(f"Error al obtener clientes: {e}")
        return []

def agregar_cliente(nombre, apellido, dni, edad, palabra_clave, direccion, localidad):
    """Inserta un nuevo cliente en la base de datos."""
    conexion = obtener_conexion()
    if not conexion:
        return False
        
    try:
        cursor = conexion.cursor()
        sql = """INSERT INTO cliente (nombre, apellido, dni, edad, palabra_clave, direccion, localidad) 
                 VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        valores = (nombre, apellido, dni, edad, palabra_clave, direccion, localidad)
        
        cursor.execute(sql, valores)
        conexion.commit()
        cursor.close()
        conexion.close()
        return True
    except Exception as e:
        print(f"Error al agregar cliente: {e}")
        return False