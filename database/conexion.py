import mysql.connector
from config import Config

def obtener_conexion():
    try:
        conexion = mysql.connector.connect(
            host=Config.DB_HOST,
            port=Config.DB_PORT,
            user=Config.DB_USER,
            password=Config.DB_PASSWORD,
            database=Config.DB_NAME
        )
        return conexion
    except Exception as e:
        print(f"Error al conectar a MySQL: {e}")
        return None