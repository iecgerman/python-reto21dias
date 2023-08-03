# Crea tu propio método map

"""
En este desafío, deberás implementar una función personalizada que emule el comportamiento del método map utilizando funciones de orden superior HOF.

La función recibirá dos parámetros: una lista y una función (func). La lista contendrá un conjunto de elementos (números, objetos, cadenas, etc.), y la función se utilizará para realizar una acción específica en cada elemento de la lista. El objetivo es retornar una nueva lista con los resultados obtenidos de aplicar la función a cada elemento, de manera similar a como lo haría el método map.

Ejemplo 1:


Input: my_map([1, 2, 3, 4], lambda num: num * 2)

Output: [2, 4, 6, 8]

Ejemplo 2:


Input: my_map([
{"name": "michi", "age": 2},
{"name": "firulais", "age": 6}],
lambda pet: pet["name"])

Output: ["michi", "firulais"]
"""

def map_german(lista, func): # recibimos una lista y una fincion como parametros
  lista_nueva = [] # aqui se almacenaran los elementos que iremos iterando
  for elemento in lista:
    lista_nueva.append(func(elemento)) # recordemos que con append() podemoa agregar elementos a una nueva lista
  return lista_nueva # retornamos todo el ciclo

respuesta = map_german([1,2,3,4,34,12,32], lambda num: num*2) #aqui nuestra funcion nos da 2 argumentos el primero es una lista de numeros y el segundo es una funcion lambda en la cual el parametro num, se multiplicara por 2 y ese valor se almacenara en la lista nueva

print(respuesta) # [2, 4, 6, 8, 68, 24, 64]

respuesta2 = map_german([
{"name": "michi", "age": 2},
{"name": "firulais", "age": 6},
{"name": "rocky", "age": 5},
{"name": "brownie", "age": 3},
{"name": "bebe", "age": 4}],
lambda pet: pet["name"]) # aca nuestra lista sera un diccionario, y la parametro de func sera una lambda que nos dara el nombre de la mascota (valor) con la clave "name" y esto al ejecutarlo en el ciclo se almacenara en la nueva lista
print(respuesta2) # ['michi', 'firulais', 'rocky', 'brownie', 'bebe']
  
  

"""def my_map(list, func):
  new_list = []
  for item in list:
    new_list.append(func(item))
  
  return new_list

response = my_map([1, 2, 3, 4], lambda num: num * 2)
print(response)

response2 = my_map([
{"name": "michi", "age": 2},
{"name": "firulais", "age": 6}],
lambda pet: pet["name"])
print(response2)"""

