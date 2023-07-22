# Las tuplas son otro tipo de objeto que permiten almacenar una colección de valores, pero a diferencia de las listas, son inmutables, es decir, no se pueden modificar una vez que se han creado.

mi_tupla = (valor1, valor2, valor3)

# Por ejemplo, el siguiente código crea una tupla llamada “puntos” que contiene tres valores: (1, 2), (3, 4) y (5, 6):

puntos = ((1, 2), (3, 4), (5, 6))

# Las tuplas también tienen un índice numérico que comienza en 0. Por lo tanto, el primer elemento de la tupla tiene el índice 0, el segundo tiene el índice 1, y así sucesivamente. Por ejemplo, para acceder al primer elemento de la tupla “puntos”, se utilizaría la sintaxis puntos[0].

puntos = ((1, 2), (3, 4), (5, 6))
puntos[0]
# (1, 2)

# Como las tuplas son inmutables, no se pueden actualizar un valor específico en una tupla. Pero se puede crear una nueva tupla a partir de una existente, utilizando la sintaxis tupla = tupla[:indice] + (nuevo_valor,) + tupla[indice+1:].

puntos = ((1, 2), (3, 4), (5, 6))
nuevo_punto = (7, 8)
puntos = puntos[:1] + (nuevo_punto,) + puntos[2:]
print(puntos)
# ((1, 2), (7, 8), (5, 6))

# index(elemento): Retorna el índice de la primera ocurrencia del elemento en la tupla.

puntos = ((1, 2), (3, 4), (5, 6))
print(puntos.index((3, 4))) # 1

# count(elemento): Cuenta cuántas veces un elemento está en una tupla.

numeros = (1, 2, 3, 2, 4, 2)
print(numeros.count(2)) # 3

# len(tupla): Retorna la cantidad de elementos de la tupla.

puntos = ((1, 2), (3, 4), (5, 6))
print(len(puntos)) # 3

