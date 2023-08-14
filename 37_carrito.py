# se encuentra en app37 y carpeta carritoCompras en español

"""
En este desafío debes crear un sistema de carrito de compras.

Dentro del playground tendrás un archivo producto.py que será la clase base(Padre) y será abstracta. Deberás crear las clases hijas Articulo y Servicio que extenderán de Producto.

La clase Articulo deberá implementar el método agregarACarrito() de manera que retorne el string "Agregando x unidades del artículo x al carrito", donde x es el nombre y la cantidad del producto. Por otro lado, la clase Servicio deberá implementar el método agregarACarrito() de manera que retorne el string "Agregando el servicio x al carrito", donde x es el nombre del servicio.

Además, debes crear la clase Carrito que será el carrito de compras y tendrá los siguientes métodos:

def agregarProducto(self, producto): este método agregará un producto al final de la lista de compras y deberá llamar al método product.agregarACarrito() de cada producto o servicio.

def borrarProducto(self, producto): este método recibirá un producto y lo eliminará de la lista de productos

def calcularTotal(self): este método calculará el total de los productos agregados y lo devolverá.

def obtenerProductos(self): este método devolerá el array de los productos que contiene el carrito.

Ejemplo 1

Input:

libro = Articulo("Libro", 100, 2)
curso = Servicio("Curso", 120, 1)

carrito = Carrito()
carrito.agregarProducto(libro)
carrito.agregarProducto(curso)
total = carrito.calcularTotal()
print(total)

Output:

Agregando 2 unidades del artículo Libro al carrito
Agregando el servicio Curso al carrito
320

Ejemplo 2

Input:

libro = Articulo("Libro", 100, 2);
curso = Servicio("Curso", 120, 1);

carrito = Carrito();
carrito.agregarProducto(libro);
carrito.agregarProducto(curso);
carrito.borrarProducto(libro);
carrito.calcularTotal();


"""


"""
En este desafío debes crear un sistema de carrito de compras.

Dentro del playground tendrás un archivo product.py que será la clase base y será abstracta. Deberás crear las clases hijas Article y Service que extenderán de Product.

La clase Article deberá implementar el método addToCart() de manera que retorne el string "Agregando x unidades del artículo x al carrito", donde x es el nombre y la cantidad del producto. Por otro lado, la clase Service deberá implementar el método addToCart() de manera que retorne el string "Agregando el servicio x al carrito", donde x es el nombre del servicio.

Además, debes crear la clase Cart que será el carrito de compras y tendrá los siguientes métodos:

addProduct(product) este método agregará un producto al final de la lista de compras y deberá llamar al método addToCart() de cada producto o servicio.

deleteProduct(product) este método recibirá un producto y lo eliminará de la lista de productos

calculateTotal() este método calculará el total de los productos agregados y lo devolverá.

getProducts() este método devolerá el array de los productos que contiene el carrito.

Ejemplo 1

Input:

libro = Articulo("Libro", 100, 2);
curso = Servicio("Curso", 120, 1);

carrito = Carrito();
carrito.addProduct(book);
carrito.addProduct(course);
carrito.calculateTotal();

Output:

Agregando 2 unidades del artículo Libro al carrito
Agregando el servicio Curso al carrito
320

Ejemplo 2

Input:

book = Article("Libro", 100, 2);
curso = Servicio("Curso", 120, 1);

cart = Cart();
cart.addProduct(book);
cart.addProduct(course);
cart.deleteProduct(book);
cart.calculateTotal();

Output:

Agregando 2 unidades del artículo Libro al carrito
Agregando el servicio Curso al carrito
120
"""

"""
from product import Product

class Article(Product):
  def addToCart(self):
    return f"Agregando {self.quantity} unidades del articulo {self.name}"
  
class Service(Product):
  def addToCart(self):
    return f"Agregando el servicio {self.name} al carrito"
  
class Cart:
  def __init__(self):
    self.products = []
  
  def addProduct(self, product):
    product.addToCart()
    self.products.append(product)
  
  def deleteProduct(self, product):
    self.products = [item for item in self.products if item.name != product.name]
  
  def calculateTotal(self):
    total = sum(item.price * item.quantity for item in self.products)
    return total
  
  def getProducts(self):
    return self.products
  
book = Article("Libro", 100, 2)
course = Service("Curso", 120, 1)

cart = Cart()
cart.addProduct(book)
cart.addProduct(course)
total = cart.calculateTotal()
print(total)
"""

"""
class Product:
  def __init__(self, name, price, quantity):
    self.name = name
    self.price = price
    self.quantity = quantity

  def addToCart(self):
    raise NotImplementedError("La lógica de este método debe ser implementada por las clases hijas")

"""