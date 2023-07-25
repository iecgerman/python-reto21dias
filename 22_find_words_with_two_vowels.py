"""
En este desafío, debes crear la lógica de la función find_words_with_two_vowels que encuentre las palabras que contienen exactamente dos vocales en una lista de palabras. Las vocales pueden ser tanto mayúsculas como minúsculas.

Recibirás un único parámetro: una lista de palabras. La función debe devolver una nueva lista que contenga todas las palabras de la lista original que cumplan con la condición mencionada anteriormente. En caso de no haber palabras que cumplan con esta condición deberás retornar una lista vacía.

Ejemplo 1:

Input: find_words_with_two_vowels([
  "hello",
  "Python",
  "world",
  "platzi"
])

Output: ["hello", "platzi"]

Ejemplo 2:

Input: find_words_with_two_vowels(["text", "test", "python", "example"])
Output: []

"""

"""def find_words_with_two_vowels(words):
  vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
  return [word for word in words if sum(1 for char in word if char in vowels) == 2]

response = find_words_with_two_vowels([
  "hello",
  "Python",
  "world",
  "platzi"
])
print(response)"""


def palabra_con_dos_vocales(palabras):
  print(palabras)
  #creamos un set (conjunto) asi no puede haber ducplicados
  vocales = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

  return [palabra for palabra in palabras if sum(1 for letra in palabra if letra in vocales) == 2]

respuesta = palabra_con_dos_vocales([
  "hello",
  "Python",
  "world",
  "platzi"
])
print(respuesta)
  
