'''
Para trabajar con PosTgres se instala 
pip install psycopg2
'''


'''
#Script SQL de como deberia verse

CREATE TABLE public.personas
(
    id serial NOT NULL,
    nombre character varying(30),
    apellido character varying(30),
    telefono character varying(10),
    CONSTRAINT pk_id_personas PRIMARY KEY (id)
);

ALTER TABLE IF EXISTS public.personas
    OWNER to postgres;

COMMENT ON TABLE public.personas
    IS 'Coleccion llamada personas';
COMMENT ON CONSTRAINT pk_id_personas ON public.personas
    IS 'Se esta definiendo la llave primaria ';

'''


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