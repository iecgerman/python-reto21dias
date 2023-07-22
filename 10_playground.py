# 10 - Dibuja un triangulo usando bucles

# que pedo en el replit si me sale y el el playgound me sale medio pinito

def print_triangle(size, character):
  #size = 5 # Número de líneas a imprimir
  #character = "$" # Caracter a imprimir
  #i = 0 # contador 

  # Imprime los espacios en blanco
  for i in range (size):
    print(" " * (size -i -1), end="")
    #           (5 - 0 -1 = 4)
    #           (5 - 1 -1 = 3)

  # Imprime los simboles que forman el pinito
    print(character * (2 * i + 1))
    #                 (2 * 0 + 1) = 1
    #                 (2 * 1 + 1) = 3

print_triangle(5,"$")
# EN EL FOR NO SE PONE "i += 1"

"""
# solucion del profe orlando sanchez

def print_triangle(size, character):
    triangle = ''
    for i in range(size):
        triangle += " " * (size - i - 1)
        triangle += character  + character * (2 * i)
        if i != size - 1:
            triangle += "\n"
    return triangle

pinito = print_triangle(5,"$")
print(pinito)
"""

"""
i = 1
while i <= 10:
  print(i)
  i += 1
  
def print_triangle(size, character):
  size = 1
  character += "* \n"
  while size < 6:
    print(size)

"""

"""
i = 1
while i <= 10:
  print(i)
  i += 1

print(" "*4 + "$")
print(" "*3 + "$"*3)
print(" "*2 + "$"*5)
print(" "*1 + "$"*7)
"""

"""
size = 0 
character = "$"
espacio = " "
while size < 5:
  size += 1
  print(f"{espacio}{character*size}")
  if size == 5:
    break
"""

# pinito con un while
"""
n = 5  # Número de líneas
i = 0  # Contador

while i < n:
  
  # Imprime espacios en blanco
  print(' ' * (n - i - 1), end='')

  # Imprime el símbolo $ por cada línea
  print('$' * (2 * i + 1))

  i += 1
"""

# pinito con un for
"""
n = 5 # Número de líneas
i = 0 # Contador

for i in range (n):
  # Imprime espacios en blanco
  print(" " * (n -i -1), end="")
#              5 -0 -1 = 4
#              5 -1 -1 = 3
#              5 -2 -1 = 2
#              5 -3 -1 = 1
#              5 -4 -1 = 0
  

  #Imprime el simbolo $ por cada línea
  print("$" * (2 * i + 1))
#              2 * 0 + 1 = 1
#              2 * 1 + 1 = 3
#              2 * 2 + 1 = 5
#              2 * 3 + 1 = 7
#              2 * 4 + 1 = 9

# EN EL FOR NO SE PONE "i += 1"
"""

# Solución del reto
"""
def print_triangle(size, character):
    triangle = ""
    for i in range(1, size + 1):
        spaces = " " * (size - i)
        line = character * (2 * i - 1)
        if i == size:
         triangle += spaces + line
        else:   
         triangle += spaces + line + "\n"
    return triangle

print(print_triangle(3, "*"))
"""