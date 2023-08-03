# Manejo de excepciones

"""
En este desafío, debes crear una función llamada calculate_discounted_price que calcule el precio con descuento de un producto. La función recibirá dos parámetros: price (precio) y discount (descuento). Tu objetivo es implementar la lógica necesaria para calcular el precio con el descuento aplicado.

Sin embargo, hay algunas condiciones y manejo de excepciones que debes tener en cuenta:

Si el precio o el descuento son valores negativos, deberás lanzar una excepción del tipo ValueError con el mensaje "El precio y el descuento deben ser valores positivos".

Si el precio o el descuento no son números, deberás lanzar una excepción del tipo TypeError con el mensaje "El precio y el descuento deben ser números".

En caso de que ocurra cualquier otro tipo de excepción no prevista, deberás capturarla y lanzar una excepción genérica del tipo Exception con el mensaje "Ha ocurrido un error inesperado" seguido del mensaje de la excepción original para obtener más detalles.

Tu función debe retornar el precio con el descuento aplicado. Si el cálculo se realiza correctamente, deberás retornar el resultado. En caso de producirse alguna excepción, deberás propagarla para que pueda ser manejada en el contexto adecuado.

Ejemplo 1:


Input: calculate_discounted_price(100, 0.2)
Output: 80.0

Ejemplo 2:


Input: calculate_discounted_price(-50, 0.2)
Output: ValueError: El precio y el descuento deben ser valores positivos
"""

def calcular_precio_con_descuento(precio, descuento):
  if not isinstance(precio, (int,float)) or not isinstance(descuento, (int,float)):
    raise TypeError('EL PRECIO O EL DESCUENTO DEBEN SER NUMEROS')

  if precio < 0 or descuento < 0:
    raise ValueError('EL PRECIO O EL DESCUENTO DEBEN DE SER VALORES POSITIVOS')

  try:
    precio_descontado = precio - (precio * descuento)
    return precio_descontado

  except Exception as e:
    raise Exception ('HA OCURRIDO UN ERROR: ' + str(e))

#respuesta = calcular_precio_con_descuento(100, 0.2)
#respuesta = calcular_precio_con_descuento('A', 0.2)
respuesta = calcular_precio_con_descuento(-100, 0.2)
print(respuesta)