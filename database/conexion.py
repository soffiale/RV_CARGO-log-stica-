import mysql.connector

def obtener_conexion():
    try:
        conexion = mysql.connector.connect(
            host="127.0.0.1",
            port=3307,  # ← Debe ser 3307
            user="root",
            password="Arcangeles369",  # Deja la contraseña que utilices en tu XAMPP
            database="rv_cargo"
        )
        return conexion
    except Exception as e:
        print(f"Error al conectar a MySQL: {e}")
        return None