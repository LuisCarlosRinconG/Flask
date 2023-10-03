# Crear y almacenar objetos en la base de datos

class Producto:
    def __init__(self, nombre_producto, valor_producto,cantidad_producto):
        self.nombre_producto = nombre_producto
        self.valor_producto = valor_producto
        self.cantidad_producto= cantidad_producto
    
    # Metodo para almacenar los documentos
    def formato_doc(self):
        return{
            'nombre_producto': self.nombre_producto,
            'valor_producto': self.valor_producto,
            'cantidad_producto': self.cantidad_producto
        }