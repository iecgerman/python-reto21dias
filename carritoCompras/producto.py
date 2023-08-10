# entonces en el desafio nos dicen que la clase padre sera Producoto:

class Producto:
  def __init__(self, nombre, precio, cantidad):
    self.nombre = nombre
    self.precio = precio
    self.cantidad = cantidad

  def agregarACarrito(self):
    raise NotImplementedError("La lógica de este método debe ser implementada por las clases hijas")