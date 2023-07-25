# Calcula la longitud de las palabras

"""def count_words_by_length(words):
  list_word = [len(word) for word in words] 
  return {word: list_word.count(word) for word in list_word} 

response = count_words_by_length([
  "apple",
  "banana",
  "orange",
  "grapefruit",
  "pear",
  "kiwi"
])

print(response)"""

def palabras_con_la_misma_cantidad_de_caracteres(palabras):
  cantidad_de_caracteres = [len(palabra) for palabra in palabras] # aquí se va a crear una lista de palabras que medira la cantidad de caracteres palabra por palabra de los parametros de la funcion
  print('cantidad_de_caracteres =>',cantidad_de_caracteres)
  
  return { palabra: cantidad_de_caracteres.count(palabra) for palabra in cantidad_de_caracteres } # aqui nos va a regresar un diccionario con la llave word y el valor sera la cuenta de cada palabra en la lista de palabras por cada palabra que exista en la lista

respuesta = palabras_con_la_misma_cantidad_de_caracteres([
  "apple",
  "banana",
  "orange",
  "grapefruit",
  "pear",
  "kiwi"
])
print(respuesta)
# cantidad_de_caracteres => [5, 6, 6, 10, 4, 4]
# {5: 1, 6: 2, 10: 1, 4: 2}