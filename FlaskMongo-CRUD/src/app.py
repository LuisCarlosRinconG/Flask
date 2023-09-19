#en consola
# actualizar o intalar pip con python.exe -m pip install --upgrade pip
# pip install flask
# pip install virtualenv
# py -3 -m venv env
# crear carpeta source para los codigos(src)
# carpeta templates para archivos index
# carpeta static para dar estilos como css
# Para activar entorno virtual
#Set-ExecutionPolicy Unrestricted -Scope Process  
#.\env\Scripts\activate    
#paara ejecuttar
#python .\src\app.py  

from flask import Flask, redirect, render_template, request, url_for
from config import *
from persona import Persona


# Instancias para realizar operaciones con la DB
con_bd = Conexion()

app = Flask(__name__)

@app.route('/')
def index():
    # Se modifica la vista index para poder hacer el muestreo de los datos
    personas = con_bd['Personas']
    PersonasRegistradas=personas.find()
    return render_template('index.html', personas = PersonasRegistradas)


# Ruta para guardar los datos de la DB
@app.route('/guardar_personas', methods = ['POST'])
def agregarPersona():
    personas = con_bd['Personas']
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    telefono = request.form['telefono']

    if nombre and apellido and telefono:
        persona = Persona(nombre, apellido, telefono)
        #insert_one para crear un documento en Mongo
        personas.insert_one(persona.formato_doc())
        return redirect(url_for('index'))
    else:
        return "Error"
    

# En este caso se eliminara atravez de la URL
# Ruta para eliminar datos en la DB donde la ruta se llama eliminar_persona y recibe un parametro llamado nombre_persona
@app.route('/eliminar_persona/<string:nombre_persona>')
def eliminar(nombre_persona):
    personas = con_bd['Personas']
    # Se hace uso de delete_one para borrar los datos de la DB personas donde el dato que se elimina es el que se para como argumento para nombre
    personas.delete_one({ 'nombre': nombre_persona})
    # Creamos un redireccionamiento que redirija a la vista index
    return redirect(url_for('index'))

#Editar o actualizar el contenido 
@app.route('/editar_persona/<string:nombre_persona>', methods = ['POST'])
def editar(nombre_persona):
    personas = con_bd['Personas']
    # Se realiza el mismo proceso de inserción y extracción para poder actualizar los datos
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    telefono = request.form['telefono']
    # Utilizaremos la función update_one()
    if nombre and apellido and telefono:
        personas.update_one({'nombre': nombre_persona}, 
                            {'$set': {'nombre' : nombre , 'apellido': apellido, 'telefono': telefono}}) # update_one() necesita de al menos dos parametros para funcionar
        return redirect(url_for('index'))
    else:
        return "Error de actualización"


if __name__ == '__main__':
    app.run(debug = True, port = 2001)