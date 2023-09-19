# Crear y almacenar objetos en la base de datos

class Persona:
    def __init__(self, nombre, apellido, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
    
    # Metodo para almacenar los documentos
    def formato_doc(self):
        return{
            'nombre': self.nombre,
            'apellido': self.apellido,
            'telefono': self.telefono    
        }