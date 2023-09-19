# Importar Flask y request 
from flask import Flask, redirect, render_template,request, url_for

# Crear la aplicación
app = Flask(__name__)

# Ruta para el inicio
@app.route('/')

# Vista para el inicio
def index():    
    info = {
        'nombre':'Juan',
        'apellido':'Perez',
        'telefono':3201099183
    }
    return render_template('index.html', datos=info)

# Perfil
@app.route('/perfil/<nombre>/<apellido>/<int:n1>')
def perfil(nombre,apellido,n1):
    asignaturas = ["matematica","español","quimica","artes","Programación"]
    info1 = {
        'nombre':nombre,
        'apellido':apellido,
        'numero':n1,
        'telefono':3002453423,
        'asignaturas': asignaturas,
        'num_asignaturas':len(asignaturas)
    }
    return render_template('perfil.html', datos1 = info1)

#Proceso antes de peticion
@app.before_request
def antes():
    print("Proceso de antes de la petición")

#Proceso despues de peticion
@app.after_request
def despues(response):
    print("Proceso despues de la petición")
    return response

#funcion de query String
def ruta_parametros():
    print(request)
    print(request.args)
    print(request.args.get('p1'))
    print(request.args.get('p2'))
    return "!Hola¡"

#Funcion de error 404

def error_404(error):
    #return render_template('error_404.html'),404
    #Redireccionar a la funcion de index
    return redirect(url_for('index'))


# Comprobación para lanzar la app
#Siempre va al final de todo
if __name__ == '__main__':
    app.add_url_rule('/ruta_prueba', view_func=ruta_parametros)
    app.register_error_handler(404,error_404)
    app.run(debug=True, port=5555)
    