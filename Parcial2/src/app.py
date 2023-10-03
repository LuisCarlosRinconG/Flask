from flask import Flask, redirect, render_template, request, url_for
from config import *
from producto import Producto


# Instancias para realizar operaciones con la DB
con_bd = Conexion()

app = Flask(__name__)

# Crud de productos
@app.route('/')
def index():
    # Se modifica la vista index para poder hacer el muestreo de los datos
    productos= con_bd['Productos']
    ProductosRegistradas=productos.find()
    return render_template('index.html', productos = ProductosRegistradas)


# Ruta para guardar los datos de la DB
@app.route('/guardar_producto', methods = ['POST'])
def agregarPersona():
    productos = con_bd['Productos']
    nombre_producto = request.form['nombre_producto']
    valor_producto = request.form['valor_producto']
    cantidad_producto = request.form['cantidad_producto']

    if  nombre_producto and valor_producto and cantidad_producto:
        producto = Producto(nombre_producto , valor_producto, cantidad_producto)
        #insert_one para crear un documento en Mongo
        productos.insert_one(producto.formato_doc())
        return redirect(url_for('index'))
    else:
        return "Error"
    

# En este caso se eliminara atravez de la URL
# Ruta para eliminar datos en la DB donde la ruta se llama eliminar_persona y recibe un parametro llamado nombre_persona
@app.route('/eliminar_producto/<string:nombre_producto>')
def eliminar(nombre_producto):
    productos = con_bd['Productos']
    # Se hace uso de delete_one para borrar los datos de la DB personas donde el dato que se elimina es el que se para como argumento para nombre
    productos.delete_one({ 'nombre_producto': nombre_producto})
    # Creamos un redireccionamiento que redirija a la vista index
    return redirect(url_for('index'))

#Editar o actualizar el contenido 
@app.route('/editar_producto/<string:nombre_producto>', methods = ['POST'])
def editar(nombre_producto):
    productos = con_bd['Productos']
    # Se realiza el mismo proceso de inserción y extracción para poder actualizar los datos
    nombre_producto = request.form['nombre_producto']
    valor_producto = request.form['valor_producto']
    cantidad_producto = request.form['cantidad_producto']
    # Utilizaremos la función update_one()
    if nombre_producto and valor_producto and cantidad_producto:
        productos.update_one({'nombre_producto': nombre_producto}, 
                            {'$set': {'nombre_producto' : nombre_producto , 'valor_producto': valor_producto, 'cantidad_producto': cantidad_producto}}) # update_one() necesita de al menos dos parametros para funcionar
        return redirect(url_for('index'))
    else:
        return "Error de actualización"


if __name__ == '__main__':
    app.run(debug = True, port = 2001)