def find_words_with_two_vowels(words):
  # Tu código aquí 👈

  
  print(words)
  
  print("Me debe devolver las palabras con 2 vocales:")

  vowels = "aeiouAEIOU"
  print("-------------------------------------")

  result = []  

  for word in words:
    num_vowels = sum(1 for char in word if char in vowels)
    if num_vowels == 2:
      result.append(word)

  return result

result = find_words_with_two_vowels([ "hello",  "Python", "world", "platzi" ])
print(result)



# ahora con list comprehention

def find_words_with_two_vowels(words):
  vowels = "aeiouAEIOU"
  print("-----------list_comprehentions-----------")
  return [word for word in words if sum(1 for char in word if char in vowels) == 2]

response = find_words_with_two_vowels([
  "hello",
  "Python",
  "world",
  "platzi"
])

print(response)