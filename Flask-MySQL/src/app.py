from flask import Flask, render_template, request, redirect, flash
import controlador

app = Flask(__name__)

"""
Definición de rutas
"""



@app.route("/agregar_tarea")
def formulario_agregar_tarea():
    return render_template("agregar_tarea.html")


@app.route("/guardar_tarea", methods=["POST"])
def guardar_tarea():
    nombre = request.form["nombre"]
    descripcion = request.form["descripcion"]
    tiempo = request.form["tiempo"]
    encargado = request.form["encargado"]
    controlador.insertar_tarea(nombre, descripcion, tiempo, encargado)
    # De cualquier modo, y si todo fue bien, redireccionar
    return redirect("/tareas")


@app.route("/")
@app.route("/tareas")
def index():
    tareas = controlador.obtener_tarea()
    return render_template("index.html", tareas=tareas)


@app.route("/eliminar_tarea", methods=["POST"])
def eliminar_tarea():
    controlador.eliminar_tarea(request.form["id"])
    return redirect("/tareas")


@app.route("/formulario_editar_tarea/<int:id>")
def editar_tarea(id):
    # Obtener la tarea por ID
    tarea = controlador.obtener_tarea_por_id(id)
    return render_template("editar_tarea.html", tarea=tarea)


@app.route("/actualizar_tarea", methods=["POST"])
def actualizar_tarea():
    id = request.form["id"]
    nombre = request.form["nombre"]
    descripcion = request.form["descripcion"]
    tiempo = request.form["tiempo"]
    encargado = request.form["encargado"]
    controlador.actualizar_tarea(nombre, descripcion, tiempo, encargado, id)
    return redirect("/tareas")


# Iniciar el servidor
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)