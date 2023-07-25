"""Las dictionary comprehensions, son una característica poderosa de Python que nos permite crear diccionarios de forma concisa y eficiente utilizando una sintaxis compacta. Son una forma elegante de transformar o filtrar elementos de una secuencia para crear un nuevo diccionario.

La sintaxis básica de una dictionary comprehension es la siguiente:"""

# nuevo_diccionario = {clave_expresion: valor_expresion for elemento in secuencia if condicion}

"""clave_expresion es una expresión que define cómo se generarán las claves del nuevo diccionario.
valor_expresion es una expresión que define cómo se generarán los valores del nuevo diccionario.
elemento es una variable que representa cada elemento de la secuencia mientras se recorre.
secuencia es la secuencia de origen de la cual se obtendrán los elementos.
condicion es una condición opcional que filtra los elementos de la secuencia.
Aquí hay un ejemplo para uso de las dictionary comprehensions:"""

personas = [("Juan", 25), ("María", 30), ("Pedro", 20)]

# Crear un nuevo diccionario con el nombre como clave y la edad como valor, solo para personas mayores de 25 años
personas_mayores = {nombre: edad for nombre, edad in personas if edad > 25}
print(personas_mayores)  # Output: {'María': 30}

# Crear un nuevo diccionario con el nombre como clave y la longitud del nombre como valor para todas las personas
diccionario_longitudes = {nombre: len(nombre) for nombre, _ in personas}
print(diccionario_longitudes)  # Output: {'Juan': 4, 'María': 5, 'Pedro': 5}
"""En el primer ejemplo, se crea un nuevo diccionario llamado personas_mayores que contiene solo a las personas mayores de 25 años del diccionario original. Las claves del nuevo diccionario son los nombres y los valores son las edades correspondientes. Esto se logra mediante la expresión nombre: edad en la dictionary comprehension, y se aplica la condición edad > 25.

En el segundo ejemplo, se crea un nuevo diccionario llamado diccionario_longitudes que contiene la longitud de cada nombre del diccionario original. Las claves del nuevo diccionario son los nombres y los valores son las longitudes de los nombres correspondientes. Esto se logra mediante la expresión nombre: len(nombre) en la dictionary comprehension.

Todo esto y más lo puedes aprender en el Curso de Python: Comprehensions, Funciones y Manejo de Errores"""