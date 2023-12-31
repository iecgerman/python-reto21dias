# Crea tu propia Lista en Python

"""
Tu objetivo es crear una clase llamada MyList que simule el comportamiento de una Lista nativa en Python, sin utilizar los métodos ya existentes. Implementarás la lógica de los siguientes métodos:

map(func): itera sobre cada elemento de nuestra estructura aplicando la función func a cada uno de ellos y devuelve una nueva lista (que será una instancia de MyList).

filter(func): itera sobre cada elemento de nuestra estructura filtrándolos según lo que indique la función func y devuelve una lista con los elementos filtrados (también una instancia de MyList).

join(character): concatena todos los elementos de nuestra estructura de datos en un string, separándolos por el carácter indicado (character). Si no se proporciona un carácter, el separador por defecto será una coma ",".

append(item): agrega un elemento item al final de la lista y aumenta la longitud (length).

pop(): elimina el último elemento de la lista y lo retorna, disminuyendo también la longitud (length).

shift(): elimina el primer elemento de la lista y lo retorna, disminuyendo la longitud (length).

unshift(item): agrega un elemento item al inicio de la lista y aumenta la longitud (length).

Además, deberás almacenar los elementos dentro de la propiedad data y el número de elementos dentro de la propiedad length, para que puedan ser consultados desde las pruebas.

Ejemplo 1:

Input:

myList = MyList()
myList.append("a")
myList.append("b")
myList.append("c")

print(myList.data)

Output:

{0: 1, 1: 2, 2: 3}

Ejemplo 2:

Input:

myList = MyList()
myList.append("Platzinauta")
myList.unshift("Hola!")

print(myArray.data)

Output:
{0: "Hola!", 1: "Platzinauta"}
"""

class MyList:
  def __init__(self):
    self.data = {}
    self.length = 0

  def append(self, item):
    self.data[self.length] = item
    self.length += 1

  def pop(self):
    if self.length == 0:
      return None
    last_item = self.data[self.length - 1]
    del self.data[self.length - 1]
    self.length -= 1
    return last_item

  def shift(self):
    if self.length == 0:
      return None
    first_item = self.data[0]
    for i in range(1, self.length):
      self.data[i - 1] = self.data[i]

    del self.data[self.length - 1]
    self.length -= 1
    return first_item

  def unshift(self, item):
    for i in range(self.length, 0, -1):
      self.data[i] = self.data[i - 1]

    self.data[0] = item
    self.length += 1

  def map(self, func):
    new_array = MyList()
    for i in range(self.length):
      new_array.append(func(self.data[i]))

    return new_array

  def filter(self, func):
    new_array = MyList()
    for i in range(self.length):
      if func(self.data[i]):
        new_array.append(self.data[i])

    return new_array

  def join(self, character=","):
    joined_string = ""
    for i in range(self.length):
      joined_string += str(self.data[i])

      if i != self.length - 1:
        joined_string += character

    return joined_string

myList = MyList()
myList.append("a")
myList.append("b")
myList.append("c")

print(myList.data) # {0: 'a', 1: 'b', 2: 'c'} 

myList = MyList()
myList.append("Platzinauta")
myList.unshift("Hola!")

print(myList.data) # {0: 'Hola!', 1: 'Platzinauta'}