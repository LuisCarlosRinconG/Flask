from config import obtener_conexion


def insertar_tarea(nombre, descripcion, tiempo, encargado):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO user(nombre, descripcion, tiempo, encargado) VALUES (%s, %s, %s, %s)",
                        (nombre, descripcion, tiempo, encargado))
    conexion.commit()
    conexion.close()

def obtener_tarea():
    conexion = obtener_conexion()
    tareas = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, nombre, descripcion, tiempo, encargado FROM user")
        tareas = cursor.fetchall()
    conexion.close()
    return tareas


def eliminar_tarea(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM user WHERE id = %s", (id,))
    conexion.commit()
    conexion.close()


def obtener_tarea_por_id(id):
    conexion = obtener_conexion()
    tarea = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT id, nombre, descripcion, tiempo, encargado FROM user WHERE id = %s", (id,))
        tarea = cursor.fetchone()
    conexion.close()
    return tarea


def actualizar_tarea(nombre, descripcion, tiempo, encargado, id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE user SET nombre = %s, descripcion = %s, tiempo = %s, encargado = %s WHERE id = %s",
                        (nombre, descripcion, tiempo, encargado, id))
    conexion.commit()
    conexion.close()