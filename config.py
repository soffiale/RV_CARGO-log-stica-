import os

class Config:
    # Si te conectás local usa 127.0.0.1; si te conectás remoto o por Ngrok, cambias esta IP o puerto
    DB_HOST = os.getenv('DB_HOST', '127.0.0.1')
    DB_PORT = int(os.getenv('DB_PORT', 3306))
    DB_USER = os.getenv('DB_USER', 'root')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'Arcángeles369')
    DB_NAME = os.getenv('DB_NAME', 'rv_cargo')