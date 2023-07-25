# solucion Orlando Sanchez

def has_two_vowels(word):
  vowels = ["a", "e", "i" , "o", "u", "A", "E", "I", "O", "U"]
  list_letters = []
  for letter in word:
    if letter in vowels:
        list_letters.append(letter)
  if len(list_letters) == 2:
    return True
  else:
    return False 

def has_two_vowels(words):
  new_list = [word for word in words if has_two_vowels(word)]
  return new_list

response = has_two_vowels([
  "hello",
  "Python",
  "world",
  "platzi"
])

print(response)