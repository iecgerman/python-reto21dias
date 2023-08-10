# nos dice que debe ser abstracta y crear las clases hijas class Articulo(Producto): y class Servicio(Producto):

# La clase Articulo deberá implementar el método agregarACarrito() de manera que retorne el string "Agregando {self.cantidad} unidades del artículo {self.nombre} al carrito", donde {self.nombre} es el nombre y {self.cantidad} es la cantidad del producto 

from producto import Producto # OJO SIEMPRE SE NOS OLVITA IMPORTAR
"""line 5, in <module>
    class Articulo(Producto):
NameError: name 'Producto' is not defined"""
  
class Articulo(Producto):
  def agregarACarrito(self):
    return f"Agregando {self.cantidad} unidades del artículo {self.nombre}"

# la clase Servicio deberá implementar el método agregarACarrito() de manera que retorne el string "Agregando el servicio {self.nombre} al carrito", donde {self.nombre} es el nombre del servicio.

class Servicio(Producto):
  def agregarACarrito(self):
    return f"Agregando el servicio {self.nombre} al carrito" 

# crear la clase Carrito que será el carrito de compras y tendrá los siguientes métodos:

class Carrito:
  def __init__(self):
    self.productos = []

  def agregarProducto(self, producto):
    producto.agregarACarrito()
    self.productos.append(producto)

  def borrarProducto(self, producto):
    self.productos = [item for item in self.productos if item.nombre != producto.nombre]

  def calcularTotal(self):
    total = sum(item.precio * item.cantidad for item in self.productos)
    return total

  def obtenerProductos(self):
    return self.productos

libro = Articulo("Libro", 100, 2)
curso = Servicio("Curso", 120, 1)

carrito = Carrito()
carrito.agregarProducto(libro)
carrito.agregarProducto(curso)
total = carrito.calcularTotal()
print(total)

libro = Articulo("Libro", 100, 2);
curso = Servicio("Curso", 120, 1);

carrito = Carrito();
carrito.agregarProducto(libro);
carrito.agregarProducto(curso);
carrito.borrarProducto(libro);
total = carrito.calcularTotal()
print(total)