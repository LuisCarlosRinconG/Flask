from psycopg2 import connect

# Parametros necesarios para conectarse
HOST = 'localhost'
PORT = 5432
# Se debe crear la db en postgres
BD = 'bd_personas'
USUARIO = 'postgres'
PASS = 'lUIS2984359'

# Funcion para poder conectarse a la DB
def EstablecerConexion():
    try:
        conexion= connect(host=HOST,port=PORT,dbname=BD,user=USUARIO,password=PASS)
    except ConnectionError:
        print("Error de Conexion")
    return conexion