import os
import pymysql
from pymysql.err import OperationalError, InternalError

def obtener_conexion():
    try:
        conexion = pymysql.connect(
            host=os.environ.get('DB_HOST'),
            user=os.environ.get('DB_USERNAME'),
            password=os.environ.get('DB_PASSWORD'),
            port=int(os.environ.get('DB_PORT', 3306)),
            db=os.environ.get('DB_DATABASE')
        )
        print("Conexión exitosa a la base de datos")
        return conexion
    except (OperationalError, InternalError) as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

