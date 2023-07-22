"""

La estructura de control “if” en Python sirve para tomar decisiones en función de si una determinada condición es verdadera o falsa. El código dentro de un bloque “if” sólo se ejecutará si la condición es verdadera, mientras que el código en un bloque “else” sólo se ejecutará si la condición es falsa.

La sintaxis básica de una estructura “if” es la siguiente:

if condicion:
  # código a ejecutar si la condición es verdadera
else:
  # código a ejecutar si la condición es falsa
Una de las formas más comunes de utilizar una estructura “if” es comparando una variable con un valor específico. Por ejemplo:

"""

edad = 25
if edad >= 18:
  print("Eres mayor de edad")
else:
  print("Eres menor de edad")
  
# En este ejemplo, se establece una variable “edad” con un valor de 25. Luego, se utiliza una estructura “if” para comprobar si la edad es mayor o igual a 18. Si es verdadero, se imprimirá “Eres mayor de edad” en la consola, de lo contrario, se imprimirá “Eres menor de edad”.

# También es posible utilizar varias condiciones en una estructura “if” utilizando la palabra clave “elif”. Por ejemplo:

calificacion = 75

if calificacion >= 90:
  print("Obtuviste una A")
elif calificacion >= 80:
  print("Obtuviste una B")
elif calificacion >= 70:
  print("Obtuviste una C")
else:
  print("Obtuviste una calificación insuficiente")
# En este ejemplo, se establece una variable “calificacion” con un valor de 75. Luego, se utiliza una estructura “if-elif” para determinar en qué rango de calificación se encuentra. Si la calificación es mayor o igual a 90, se imprimirá “Obtuviste una A”, si es mayor o igual a 80, se imprimirá “Obtuviste una B”, y así sucesivamente.

# Todo esto y más lo puedes aprender en el Curso de Fundamentos de Python