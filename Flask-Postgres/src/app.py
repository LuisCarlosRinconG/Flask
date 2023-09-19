from flask import Flask, render_template,request,redirect,url_for
# Se importa todo de el archivo config.py
from config import *
app=Flask(__name__)

#Variable para hacer la conexion
con_bd = EstablecerConexion()

@app.route('/')
def index():
    return render_template('index.html')

#Ruta para guardar los datos
@app.route('/guardar_personas', methods=['POST'])
def agregarPersonas():
    # Creación de un cursor para la manipulacion de la base de datos
    '''
    -el objeto cursor es una estructura de control para el recorrido(y potencial procesamiento)
    de los registros del resultado de una consulta
    '''
    cursor=con_bd.cursor()
    nombre=request.form['nombre']
    apellido=request.form['apellido']
    telefono=request.form['telefono']
    # Mostrar datos
    if nombre and apellido and telefono:
        sql="""
        INSERT INTO personas(nombre,apellido,telefono)
        VALUES(%s,%s,%s)
        """
        # Por medio de cursor con la funcion execute que recibe dos parametros se va a ejecutar la consulta
        cursor.execute(sql,(nombre,apellido,telefono))
        con_bd.commit()
        return redirect(url_for('index'))
    else:
        return "error en la consulta"

if __name__=='__main__':
    app.run(debug=True)