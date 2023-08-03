# Maneja correctamente los errores

"""En este desafío, debes crear una función llamada calculate_average que calcule el promedio de una lista de números. Sin embargo, la función debe manejar correctamente dos casos especiales:

Si la lista está vacía, la función debe generar una excepción ValueError con el mensaje "La lista está vacía".

Si la lista contiene elementos que no son números, la función debe generar una excepción TypeError con el mensaje "La lista contiene elementos no numéricos".

Tu objetivo es implementar la función calculate_average de manera que maneje adecuadamente estos casos y devuelva el promedio de los números en la lista.

Aquí tienes algunos ejemplos de entrada y salida esperada:

Ejemplo 1:


Input: calculate_average([1, 2, 3, 4, 5])
Output: 3.0

Ejemplo 2:


Input: calculate_average([10, 20, 30, 40, 50])
Output: 30.0

Ejemplo 3:


Input: calculate_average([])
Output: ValueError: La lista está vacía

Ejemplo 4:


Input: calculate_average([1, 2, '3', 4, 5])
Output: TypeError: La lista contiene elementos no numéricos"""

"""La función isinstance devuelve un booleano.

EJEMPLOS
Podemos comprobar si el número entero 5 pertenece a la clase int con el siguiente código:

isinstance(5, int)

True

Si pasásemos como segundo argumento el nombre de la clase str (cadenas de texto), la función devuelve False:

isinstance(5, str)

False

El argumento classinfo puede ser una tupla de nombres de clases, devolviéndose True si el objeto analizado pertenece a alguna de ellas:

isinstance(5, (int, str))

True

isinstance(5, (bool, str))

False

También puede ser una estructura recursiva de tuplas:

isinstance(5, ((int, str), (float, bool)))

True

isinstance(5, ((complex, str), (float, bool)))

False

Podemos probar la función con una clase personalizada:

class circulo:
    def __init__(self, radio):
        self.radio = radio

c = circulo(3)

isinstance(c, circulo)

True"""


def calcular_promedio(lista_numeros):
  if len(lista_numeros) == 0:
    raise ValueError('LA LISTA ESTA VACIA')

  total = 0

  for numero in lista_numeros:
    if not isinstance(numero, (int, float)):
      raise TypeError('DEBEN DE SER PUROS NUMEROS')

    total += numero

  return total / len(lista_numeros)

#respuesta = calcular_promedio([10,29,23]) # 20.66
#respuesta = calcular_promedio([]) # ValueError: LA LISTA ESTA VACIA
respuesta = calcular_promedio([23,'A',34]) # TypeError: DEBEN DE SER PUROS NUMEROS
print(respuesta)

"""def calcular_promedio(lista_numeros):
  if lista_numeros == []:
    raise ValueError("LA LISTA ESTA VACIA")  
  try:
    return sum(lista_numeros) / len(lista_numeros)
  except TypeError:
    raise TypeError('DEBEN DE SER PUROS NUMEROS')
    
respuesta = calcular_promedio([10,'A',30])
print(respuesta)"""