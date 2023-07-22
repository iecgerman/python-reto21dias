Los ciclos son una herramienta esencial dentro de Python. Sirven para repetir un bloque de código varias veces, dependiendo de una condición específica. Los ciclos son fundamentales para la automatización de tareas y la eficiencia en el código.

Existen dos tipos de ciclos en Python: los ciclos “for” y los ciclos “while”. Ambos tienen una sintaxis similar, pero se utilizan en situaciones diferentes.

Ciclo For
El ciclo “for” es utilizado para repetir un bloque de código un número específico de veces. Su sintaxis básica es la siguiente:

for variable in secuencia:
  # código a ejecutar
La variable se establece para recorrer los elementos en la secuencia especificada, y el código dentro del ciclo se ejecutará para cada elemento de la secuencia. Por ejemplo, el siguiente ciclo “for” imprimirá los números del 1 al 10 en la consola:

for i in range(1, 11):
  print(i)
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
También se utiliza para recorrer las propiedades de un diccionario y de colecciones como una lista.

El uso de un ciclo “for in” es la siguiente:

user = {
  "name": "Pepito",
  "age": 20,
  "role": "Python developer"
}

for prop in user:
  print(user[prop])
# "Pepito"
# 20
# "Python developer"
En este ejemplo, se establece una variable “prop” que se utilizará para recorrer las propiedades del diccionario. El valor de cada propiedad se imprimirá en la consola.

Por otro lado, la sintaxis de un ciclo for para recorrer una lista es la siguiente:

technologies = ["py", "django", "webscraping"]

for element in technologies:
  print(element)
# "py"
# "django"
# "webscraping"
En este ejemplo, se establece una variable “element” que se utilizará para recorrer cada elemento en la lista. Cada valor se imprimirá en la consola.

Ciclo While
Por otro lado, el ciclo while se utiliza para repetir un bloque de código mientras se cumpla una determinada condición. Su sintaxis básica es la siguiente:

while condición:
  # código a ejecutar
La condición se evalúa antes de ejecutar el código dentro del ciclo y si la condición es verdadera, el código se ejecutará de nuevo. Por ejemplo, si quisiéramos hacer una implementación del ejemplo anterior con los números del 1 al 10, quedaría de la siguiente manera:

i = 1
while i <= 10:
  print(i)
  i += 1
En Python no existe una estructura de ciclo do-while como en otros lenguajes de programación, pero se puede lograr un comportamiento similar utilizando un ciclo while junto con una condición inicial que siempre se cumpla.

Por ejemplo, para imprimir los números del 1 al 10 utilizando un ciclo while con un comportamiento similar a un do-while, se puede hacer lo siguiente en Python:

i = 1
while True:
    print(i)
    i += 1
    if i > 10:
        break
En este caso, la condición inicial es True, por lo que el ciclo se ejecutará al menos una vez. En cada iteración, se imprime el valor de la variable i y se incrementa en 1. Después de cada incremento, se evalúa la condición de que i sea mayor que 10. Si esto es cierto, se utiliza la instrucción break para salir del ciclo.

Este código imprimirá los números del 1 al 10 en la consola de Python.