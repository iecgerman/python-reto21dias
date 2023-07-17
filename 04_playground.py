# Retorna el tipo de dato

def found_type(value):
   # Tu código aquí 👇
   return type(value)
value = found_type(1)
print(value)

value = found_type("Dieguillo")
print(value)

value = found_type(True)
print(value)

"""
En este desafío encontrarás una función llamada solution que recibe un parámetro llamado valor. Debes encontrar el tipo de dato del parámetro valor y retornarlo desde la función solution.

Recuerda que el parámetro valor será distinto por cada distinta forma en que ejecutemos la función solution.

Ejemplo 1:


Input:

solution(1)
solution("Dieguillo")
solution(True)

Output:

"number"
"string"
"boolean"
"""

# con mis variables
"""
def solution(valor):
  return type(valor)

valor = solution(1)
print(valor)

valor = solution("Dieguillo")
print(valor)

valor = solution(True)
print(valor)
"""