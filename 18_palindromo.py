# Encuentra el mayor palíndromo

"""
En este desafío, debes crear una función que encuentre el palíndromo más largo en una lista de palabras.

Recibirás un único parámetro: una lista de palabras. Si no hay ningún palíndromo en la lista, la función debe devolver None. Si hay más de un palíndromo con la misma longitud máxima, debes devolver el primer palíndromo encontrado en la lista.

Un palíndromo es una palabra que se puede leer de la misma manera tanto hacia adelante como hacia atrás.

Ejemplo 1:


Input: find_largest_palindrome(["racecar", "level", "world", "hello"])

Output: "racecar"

Ejemplo 2:

Input: find_largest_palindrome(["Platzi", "Python", "django", "flask"])

Output: None

ok entonces tenemos que crear una lista que se llamara:

words = []

en ella se almacenaran las palabras a las cuales hay que crear una funcion que encuentre el palindromo mayor

get palindromo_mayor(words):

está facil solo hay que leer la cantida de letras que forman cada palabra y haer una comparación de cual es mayor despues otra condicion en donde verifique si esa palabra se puede leer al derecho y al derbez, me imagino que hay que ordenarlas con reverse y hacer un tipo de word[0] == word[0].reverse, ejemplo: amor == roma
"""

# esta es la que se me hizo la solucion mas entendible qeu fue de Javier Martínez González

def is_palindrome(word):
  return word == word[::-1]

def find_largest_palindrome(words):
  longest_palindrome = None
  
  for word in words:
    if is_palindrome(word):
      if longest_palindrome is None or len(word) > len(longest_palindrome):
        longest_palindrome = word

  return longest_palindrome


response = find_largest_palindrome(["somos", "recocer", "amor", "casa", "level", "world", "hello"])
print(response)



"""
def buscador(words):
  palindromo_mayor = ""
  for word in words:
    reversed_word = ""
    
    for value in range(len(word), 0, -1):
      letra = word[value - 1]
      reversed_word += letra

    if reversed_word == word:
      if(len(word) > len(palindromo_mayor)):
        palindromo_mayor = word

  if palindromo_mayor == "":
    return None

  return palindromo_mayor

response = buscador(["somos", "recocer", "amor", "casa", "level", "world", "hello"])
print(response)
"""



"""
# solucion de un comentario

def find_largest_palindrome(words):
   largest = 0
   palindrome = ""

   for word in words:
      if word == word[::-1]:
         if len(word) > largest:
            palindrome = word
            largest = len(word)
      
   return palindrome if palindrome else None

response = find_largest_palindrome(["somos", "recocer", "amor", "casa", "level", "world", "hello"])
print(response)
"""



"""
# solucion del reto

def find_largest_palindrome(words):
  largest_palindrome = ""
  for word in words:
    reversed_word = ""
    
    for value in range(len(word), 0, -1):
      letter = word[value - 1]
      reversed_word += letter
    
    if reversed_word == word:
      if(len(word) > len(largest_palindrome)):
        largest_palindrome = word
  
  if largest_palindrome == "":
    return None
  
  return largest_palindrome

response = find_largest_palindrome(["somos", "recocer", "amor", "casa", "level", "world", "hello"])
print(response)
"""