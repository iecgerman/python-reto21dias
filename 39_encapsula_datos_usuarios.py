# Encapsula los datos de los usuarios

"""
En este desafío, debes implementar la lógica de la clase "Usuario" que represente un usuario en una red social y utilizar encapsulamiento para proteger sus datos privados.

La clase debe tener las siguientes variables privadas:

nombre
edad
amigos (lista de diccionarios Usuario)
mensajes (lista de strings)
Además, debes proporcionar los siguientes métodos públicos:

agregarAmigo(amigo): agrega un usuario a la lista de amigos del usuario actual.
enviarMensaje(mensaje, amigo): agrega un mensaje a la lista de mensajes del usuario actual y al amigo especificado.
mostrarMensajes(): devuelve la lista de mensajes del usuario actual.
También debes tener definidos los getters y setters para acceder a los datos privados como el nombre y la edad, los cuales pueden ser modificados mediante su propio setter.

Ejemplo 1:

Input:

usuario1 = Usuario("Juan", 20)
usuario2 = Usuario("Maria", 25)
usuario1.agregarAmigo(usuario2)
usuario1.enviarMensaje("Hola Maria!", usuario2)

print(usuario1.mostrarMensajes())

Output:

["Hola Maria!"]

Ejemplo 2:

Input:

usuario1 = Usuario("Juan", 20)
usuario1.nombre = "Pepito"
print(usuario1.nombre)

Output:

"Pepito"
"""

class Usuario:
  def __init__(self, nombre, edad):
    self._nombre = nombre # ojo hay que poner guión bajo, para tener buenas practicas y saber que son datos privados
    self._edad = edad
    self._amigos = [] # lista de diccionarios Usuario
    self._mensajes = [] # lista de strings

  # creamos los métodos públicos
  def agregarAmigo(self, amigo):
    self._amigos.append(amigo)

  def enviarMensajes(self, mensaje, amigo):
    self._mensajes.append(mensaje)
    self._mensajes.append(mensaje)

  def mostrarMensajes(self):
    return self._mensajes
  
  @property #esto es como usar get_nombre
  def nombre(self):
    return self._nombre #

  @nombre.setter # esto equivale a usar set_nombre
  def nombre(self, valor):
    self._nombre = valor

  @property
  def edad(self):
    return self._edad

  @edad.setter
  def edad(self, valor):
    self.edad = valor

usuario1 = Usuario("Juan", 20)
usuario2 = Usuario("Maria", 25)
usuario1.agregarAmigo(usuario2)
usuario1.enviarMensajes("Hola Maria!", usuario2)

usuario1.mostrarMensajes()

usuario1 = Usuario("Juan", 20)
usuario2 = Usuario("Maria", 25)
usuario1.agregarAmigo(usuario2)
usuario1.enviarMensajes("Hola Maria!", usuario2)

print(usuario1.mostrarMensajes()) # ['Hola Maria!', 'Hola Maria!']

usuario1 = Usuario("Juan", 20)
usuario1.nombre = "Pepito"
print(usuario1.nombre)


"""
En este desafío, debes implementar la lógica de la clase "Usuario" que represente un usuario en una red social y utilizar encapsulamiento para proteger sus datos privados.

La clase debe tener las siguientes variables privadas:

name
age
friends (lista de diccionarios Usuario)
messages (lista de strings)
Además, debes proporcionar los siguientes métodos públicos:

addFriend(friend): agrega un usuario a la lista de amigos del usuario actual.
sendMessage(message, friend): agrega un mensaje a la lista de mensajes del usuario actual y al amigo especificado.
showMessages(): devuelve la lista de mensajes del usuario actual.
También debes tener definidos los getters y setters para acceder a los datos privados como el nombre y la edad, los cuales pueden ser modificados mediante su propio setter.

Ejemplo 1:

Input:

usuario1 = User("Juan", 20)
usuario2 = User("Maria", 25)
usuario1.addFriend(usuario2)
usuario1.sendMessage("Hola Maria!", usuario2)

usuario1.showMessages()

Output:

["Hola Maria!"]

Ejemplo 2:

Input:

usuario1 = User("Juan", 20)
usuario1.name = "Pepito"
print(usuario1.name)

Output:

"Pepito"



# SOLUCION DEL RETO VARIABLES EN INGLES
class User:
  def __init__(self, name, age):
    self._name = name
    self._age = age
    self._friends = []
    self._messages = []

  def addFriend(self, friend):
      self._friends.append(friend)

  def sendMessage(self, message, friend):
      self._messages.append(message)
      friend._messages.append(message)

  def showMessages(self):
    return self._messages

  @property
  def name(self):
    return self._name

  @name.setter
  def name(self, value):
    self._name = value

  @property
  def age(self):
    return self._age

  @age.setter
  def age(self, value):
    self._age = value

usuario1 = User("Juan", 20)
usuario2 = User("Maria", 25)
usuario1.addFriend(usuario2)
usuario1.sendMessage("Hola Maria!", usuario2)

print(usuario1.showMessages()) # ['Hola Maria!']


usuario1 = User("Juan", 20)
usuario1.name = "Pepito"
print(usuario1.name) # Pepito

"""