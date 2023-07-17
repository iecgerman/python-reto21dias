# Los operadores aritméticos nos permiten realizar operaciones matemáticas básicas, como la suma, la resta, la multiplicación y la división.

# Suma
print(1 + 2) # 3

# Resta
print(5 - 2) # 3

# Multiplicación
print(3 * 4) # 12

# División
print(10 / 2) # 5.0

# División entera
print(10 // 3) # 3

# Módulo (devuelve el resto de una división)
print(10 % 3) # 1

# Potencia
print(2 ** 3) # 8

print("\n"* 2)

# Los operadores de asignación nos permiten asignar valores a variables.

x = 10
x += 5 # x = x + 5
print(x) # 15

x -= 3 # x = x - 3
print(x) # 12

x *= 2 # x = x * 2
print(x) # 24

total = 1000
total *= 0.2  # total = total * 0.2
print(total)

x /= 4 # x = x / 4
print(x) # 6.0

x //= 3 # x = x // 3
print(x) # 2.0

x %= 2 # x = x % 2
print(x) # 0.0

x **= 3 # x = x ** 3
print(x) # 0.0

print("\n"* 2)

# Los operadores de comparación nos permiten comparar valores y nos devuelven True o False según el resultado de la comparación.

print(1 < 2) # True
print(2 > 1) # True
print(1 <= 2) # True
print(2 >= 1) # True
print(1 != 2) # True

print("\n"* 2)

# Entre estos existen 2 operadores de igualdad los cuales son == y is. El primero realiza una comparación de valor y el segundo, además de comparar el valor, también verifica si ambos objetos son el mismo objeto en memoria.

print(1 == "1") # True
print(1 is "1") # False

print("\n"* 2)

# AND (and): Este operador lógico evalúa si ambas expresiones son verdaderas. Si ambas expresiones son verdaderas, devuelve True, de lo contrario, devuelve False. Por ejemplo:

edad = 25
mayor_de_edad = edad >= 18

if edad >= 18 and mayor_de_edad:
  print("Eres mayor de edad")
else:
  print("Aún eres menor de edad ")
  
print("\n"* 2)

# OR (or): Este operador lógico evalúa si al menos una de las expresiones es verdadera. Si al menos una de las expresiones es verdadera, devuelve True, de lo contrario, devuelve False. Por ejemplo:

edad = 25
tiene_identificacion = True

if edad >= 18 or tiene_identificacion:
    print("Puedes entrar al bar")
else:
    print("No tienes la edad o la identificación suficiente para entrar al bar")

print("\n"* 2)

# **NOT (not)**: Este operador lógico invierte el valor de la expresión. Si la expresión es verdadera, devuelve False, de lo contrario, devuelve True. Por ejemplo:

es_fin_de_semana = True

if not es_fin_de_semana:
    print("A trabajar")
else:
    print("A disfrutar del fin de semana")

print("\n"* 2)