Las funciones lambda en Python son funciones anónimas que se pueden definir de manera concisa en una sola línea. A diferencia de las funciones regulares, las funciones lambda no requieren un nombre y se utilizan principalmente para realizar operaciones simples y rápidas.

La sintaxis básica de una lambda es la siguiente:

lambda argumentos: expresion
argumentos son los parámetros de la función.
expresion es la operación que se realizará y se devolverá como resultado.
Las lambdas se utilizan comúnmente en combinación con otras funciones, como map(), filter() y reduce(), para realizar operaciones sobre secuencias de manera más concisa.

Aquí hay algunos ejemplos para ilustrar el uso de las lambdas:

# Ejemplo 1: Función lambda simple
suma = lambda a, b: a + b
resultado = suma(2, 3)
print(resultado)  # Output: 5

# Ejemplo 2: Uso de lambda con map()
numeros = [1, 2, 3, 4, 5]
duplicados = list(map(lambda x: x * 2, numeros))
print(duplicados)  # Output: [2, 4, 6, 8, 10]

# Ejemplo 3: Uso de lambda con filter()
numeros = [1, 2, 3, 4, 5]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # Output: [2, 4]

En el primer ejemplo, se define una función lambda llamada suma que toma dos argumentos a y b y devuelve su suma. Luego, se llama a la función lambda pasando los argumentos 2 y 3, y se almacena el resultado en la variable resultado.

En el segundo ejemplo, se utiliza una lambda junto con la función map() para duplicar cada elemento de la lista numeros. La función lambda multiplica cada elemento por 2, y map() aplica esta operación a cada elemento de la lista.

En el tercer ejemplo, se utiliza una lambda junto con la función filter() para filtrar los números pares de la lista numeros. La función lambda verifica si un número es divisible por 2 y devuelve True si lo es.

Las funciones lambda son útiles cuando se necesita definir rápidamente una función pequeña y sencilla sin tener que escribir una función completa. Se utilizan comúnmente en combinación con otras funciones para operar sobre secuencias de manera más eficiente y concisa.

Todo esto y más lo puedes aprender en el Curso de Python: Comprehensions, Funciones y Manejo de Errores