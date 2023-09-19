# Importar Flask y request 
from flask import Flask, redirect, render_template,request, url_for

# Crear la aplicación
app = Flask(__name__)

# Ruta para el inicio
@app.route('/inicio/<nombre>/<int:altura>')
# Vista para el inicio
def index(nombre,altura):
    estaturas = {
        'nombre':nombre,
        'altura':altura,
        'resultado':"",
    }

    if(estaturas["altura"]<=150):
        estaturas["resultado"]="Persona de altura Baja"
    elif(estaturas["altura"]>=151 and estaturas["altura"]<=170):
        estaturas["resultado"]="Persona de altura Media"
    elif(estaturas["altura"]>=171 and estaturas["altura"]<=190):
        estaturas["resultado"]="Persona Alta"
    elif(estaturas["altura"]>=191 and estaturas["altura"]<=230):
        estaturas["resultado"]="Persona muy Alta"
    elif(estaturas["altura"]>=231):
        estaturas["resultado"]="Persona demasiado ALta"
    else:
        estaturas["resultado"]="¿Eso es una altura?"

    return render_template('index.html', datos=estaturas)

def error_404(error):
    return render_template('error_404.html'),404
    #Redireccionar a la funcion de index
    #return redirect(url_for('index'))


# Comprobación para lanzar la app
#Siempre va al final de todo
if __name__ == '__main__':
    app.register_error_handler(404,error_404)
    app.run(debug=True, port=9999)