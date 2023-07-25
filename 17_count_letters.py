# Calcula la cantidad de letras en una oración

"""
En este desafío deberás implementar la lógica de una función que cuente la cantidad de ocurrencias de cada letra en una cadena de texto y lo almacene en un diccionario.

Es importante mencionar que la función debe ser sensible a mayúsculas y minúsculas, es decir, las letras mayúsculas y minúsculas deben considerarse diferentes.

Ejemplo 1:


Input: "Hola mundo"

Output: {
  'H': 1, 
  'o': 2, 
  'l': 1, 
  'a': 1, 
  ' ': 1, 
  'M': 1, 
  'u': 1, 
  'n': 1, 
  'd': 1
}
"""

def contador_de_letras(cadena_de_texto):
  dict_letras = {} # aquí nos crea el dict

  for letra in cadena_de_texto:
    if letra in dict_letras:
      # aqui indice_de_letra va a apuntar al indice 1, luego al 2, 3, 4...
      dict_letras[letra] += 1 # cada que encuentre una letra igual sumara 1

    else:
      # aqui significa que solo encontro 1 letra igual en el parametro cadena_de_texto
      dict_letras[letra] = 1

  return dict_letras

respuesta = contador_de_letras("Pachyrringo Stark")
print("\n Diccionario en formato fila: \n")
print(respuesta)

print("\n en formato columna: \n")
for llave, valor in respuesta.items():

  print(llave, "=>", valor)