# Herencia en Python

"""
La herencia en Python es un concepto fundamental de la programación orientada a objetos que nos permite crear nuevas clases a partir de clases existentes, heredando todas sus propiedades y métodos. Esto nos permite reutilizar el código existente y crear jerarquías de clases que comparten comportamiento común.

A continuación se muestra un ejemplo simple de una clase Animal que define una propiedad especie y un método hacerSonido():

class Animal:
    def __init__(self, especie):
        self.especie = especie

    def hacerSonido(self):
        print('Este animal hace un sonido')
Ahora podemos crear una clase derivada Perro que hereda de la clase Animal y añade una propiedad raza y un método ladrar():

class Perro(Animal):
    def __init__(self, especie, raza):
        super().__init__(especie)
        self.raza = raza

    def ladrar(self):
        print('El perro está ladrando')
En este ejemplo, la clase Perro hereda de la clase Animal mediante la declaración class Perro(Animal). El método __init__() de Perro llama al método __init__() de Animal utilizando la función super().__init__() para inicializar la propiedad especie. Además, Perro añade una propiedad raza y un método ladrar().

Ahora podemos crear un objeto de la clase Perro y llamar a sus métodos y propiedades:

miPerro = Perro('Canino', 'Labrador')
print(miPerro.especie)  # Canino
miPerro.hacerSonido()  # Este animal hace un sonido
miPerro.ladrar()  # El perro está ladrando
Como podemos ver, miPerro hereda la propiedad especie y el método hacerSonido() de la clase Animal, y también tiene su propia propiedad raza y método ladrar().

La herencia nos permite reutilizar el código existente y crear jerarquías de clases que comparten comportamiento común. También nos permite crear clases más específicas a partir de clases más generales, lo que nos permite crear código más modular y escalable.
"""