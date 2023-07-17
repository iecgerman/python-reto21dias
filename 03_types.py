# Tipos de datos: Numbers, Strings y Diccionarios

# También podemos utilizar la notación científica para representar números muy grandes o muy pequeños.

numero_grande = 1e6 # 1 millón
numero_pequeno = 1e-6 # 0.000001

print(numero_grande)
print(numero_pequeno) # no sale

# podemos tipar una variable para que solo pueda contener números con decimales utilizando el tipo de dato float

pi: float = 3.14
salario: float = 1500.50

nombre = 'german'
apellido = 'garcia'

# Podemos concatenar dos strings utilizando el operador +:
print("Hola, " + nombre + " " + apellido + "!") 
# "Hola, Platzi Academy!"

# También podemos utilizar la notación f-strings para crear strings que incluyen variables y expresiones:

print(f"Hola, {nombre} {apellido}!") # ES DE LAS MAS USADAS
# "Hola, Platzi Academy!"

"""
Python proporciona una serie de métodos para manipular strings. Algunos de los métodos más comunes son:

len(): Devuelve la longitud de un string.
upper(): Devuelve el string en mayúsculas.
lower(): Devuelve el string en minúsculas.
split(): Devuelve una lista de strings separados por un carácter.
"""
print(len(nombre)) # 6
print(nombre.upper()) # PLATZI
print(nombre.lower()) # platzi
print(nombre.split('a')) # ['Pl', 'tzi']

"""
Diccionarios
Los diccionarios son estructuras de datos que nos permiten almacenar un conjunto de pares clave-valor. Estos pares son conocidos como elementos del diccionario.

Para crear un diccionario, debemos utilizar las llaves {} y especificar los elementos del diccionario mediante la sintaxis clave: valor. Los valores de los elementos pueden ser de cualquier tipo de dato, incluyendo otros diccionarios.
"""

persona = {
  "nombre": "Fulanita",
  "platziRank": 9567,
	"cursoFavorito": {
		"nombre": "Básico de Python",
		"clases": 30,
		"duracion": "2 horas"
	}
}

"""
Para acceder a los elementos de un diccionario, podemos utilizar la clave como índice.

Ejemplo:
"""

print(persona["nombre"]) # "Fulanita"
print(persona["cursoFavorito"]["nombre"]) # "Básico de Python"
print(persona["platziRank"]) # 9567

# Los valores booleanos (boolean) son un tipo de dato que representa un valor verdadero o falso

curso_completado = True
lectura_completada = False

#No pasa nada si no recuerdas el tipo de dato con el que estás trabajando, dentro de Python existe la función type() la cual te dirá el tipo de dato con el que estás trabajando

type("#PlatziChallenge") 
# <class 'str'>
type(30) 
# <class 'int'>
type({}) 
# <class 'dict'>

type([]) # <class 'list'>