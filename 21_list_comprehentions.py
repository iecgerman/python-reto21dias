# List comprehension

"""
Las list comprehensions, son una característica poderosa de Python que nos permite crear listas de forma concisa y eficiente utilizando una sintaxis compacta. Las list comprehensions son una forma elegante de transformar o filtrar elementos de una lista existente para crear una nueva lista.

La sintaxis básica de una list comprehension es la siguiente:


nueva_lista = [expresion for elemento in lista_original if condicion]

"""

numeros = [1, 2, 3, 4, 5]

# Crear una nueva lista con el cuadrado de los números pares de la lista original
cuadrados_pares = [num ** 2 for num in numeros if num % 2 == 0]
print(cuadrados_pares)  # Output: [4, 16]

# Crear una nueva lista con los números impares multiplicados por 2 de la lista original
impares_multiplicados = [num * 2 for num in numeros if num % 2 != 0]
print(impares_multiplicados)  # Output: [2, 6, 10]

"""
En el primer ejemplo, se crea una nueva lista llamada cuadrados_pares que contiene el cuadrado de los números pares de la lista original. La expresión num ** 2 eleva al cuadrado cada número y se agrega a la lista si cumple la condición num % 2 == 0.

En el segundo ejemplo, se crea una nueva lista llamada impares_multiplicados que contiene los números impares de la lista original multiplicados por 2. La expresión num * 2 multiplica cada número impar por 2 y se agrega a la lista si cumple la condición num % 2 != 0.

Las list comprehensions también pueden incluir cláusulas else para manejar casos en los que la condición no se cumple.
"""

numeros = [1, 2, 3, 4, 5]

# Crear una nueva lista con los números pares de la lista original, y 'No par' para los impares
numeros_par_o_no_par = ['Par' if num % 2 == 0 else 'Impar' for num in numeros]
print(numeros_par_o_no_par)  # Output: ['No par', 'Par', 'No par', 'Par', 'No par']

"""
En este ejemplo, se crea una nueva lista llamada numeros_par_o_no_par que contiene la cadena 'Par' para los números pares y la cadena 'No par' para los números impares de la lista original.

Las list comprehensions son una herramienta muy útil en Python que nos permite escribir código más limpio y legible al mismo tiempo que realizamos transformaciones y filtrados en las listas de manera eficiente.

Todo esto y más lo puedes aprender en el Curso de Python: Comprehensions, Funciones y Manejo de Errores
"""
