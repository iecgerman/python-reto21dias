# Jerarquía de animales usando herencia

"""En este desafío, debes crear una jerarquía de clases mediante el uso de la herencia.

La clase base será Animal con las propiedades name, age y specie y un método getInfo que devuelve un objeto con la información del animal.

Luego, debes crear una clase Mammal que herede de Animal y tenga una propiedad adicional hasFur y un método getInfo que sobreescriba al del padre y incluya la información de hasFur.

Finalmente, debes crear una clase Dog que herede de Mammal y tenga una propiedad adicional breed y un método getInfo que sobreescriba al del padre y incluya la información de breed, al igual que el método bark que devuelva el string "woof!". Las propiedades de specie y hasFur deben estar incluídas como "dog" y True respectivamente desde la implementación por lo que no debe ser necesario pasar los valores a la hora de crear la instancia.

Ejemplo 1

Input:
bird = Animal("pepe", 1, "bird")
bird.getInfo()

Output:

{
  "name": "pepe",
  "age": 1,
  "specie": "bird",
}

Ejemplo 2

Input:
hippo = Mammal("bartolo", 3, "hippo", false)
hippo.getInfo()

Output:

{
  "name": "bartolo",
  "age": 3,
  "specie": "hippo",
  "hasFur": false,
}"""

class Animal:
  # creamos el metodo constructor con sus parametros
  def __init__(self, nombre, edad, especie):
    # definimos lo que le estamos pidiendo que sea igual a cada parametro
    self.nombre = nombre
    self.edad = edad
    self.especie = especie

  def getInfo(self):
    return {
      "nombre": self.nombre,
      "edad": self.edad,
      "especie": self.especie
    }
# creamos la subclase Mamifero que hereda su clase padre Animal(SIN AGRAVIAR)
class Mamifero(Animal):
  # se crea su metodo constructor y se heredan los parametros de la clase padre mas el parametro nuevo
  def __init__(self, nombre, edad, especie, pelaje):
    # para poderlos heredar ocupamos usar super()
    super().__init__(nombre, edad, especie)
    # hacemos referencia al nuevo objeto "pelaje"
    self.pelaje = pelaje

  def getInfo(self):
    info = super().getInfo()
    info["pelaje"] = self.pelaje
    return info

class Perro(Mamifero):
  def __init__(self, nombre, edad, criar):
    super().__init__(nombre, edad, "perro", True)
    self.criar = criar

  def getInfo(self):
    info = super().getInfo()
    info["criar"] = self.criar
    return info

  def ladrar(self):
    return "woof!! woof!!"

bird = Animal("pepe", 1, "bird")
print(bird.getInfo())

hippo = Mamifero("bartolo", 3, "hippo", False)
print(hippo.getInfo())

perro = Perro("fido", 4, "pastor aleman");
print(perro.ladrar())



# SOLUCION


"""class Animal:
  def __init__(self, name, age, specie):
    self.name = name
    self.age = age
    self.specie = specie

  def getInfo(self):
    return {
      "name": self.name,
      "age": self.age,
      "specie": self.specie
    }


class Mammal(Animal):
  def __init__(self, name, age, specie, hasFur):
    super().__init__(name, age, specie)
    self.hasFur = hasFur

  def getInfo(self):
    info = super().getInfo()
    info["hasFur"] = self.hasFur
    return info


class Dog(Mammal):
  def __init__(self, name, age, breed):
    super().__init__(name, age, "dog", True)
    self.breed = breed

  def getInfo(self):
    info = super().getInfo()
    info["breed"] = self.breed
    return info

  def bark(self):
    return "woof!"
  
bird = Animal("pepe", 1, "bird")
print(bird.getInfo())

dog = Dog("fido", 4, "pastor aleman");
print(dog.bark())

"""