"""Para este ejercicio decidí resolverlo de dos formas, ambas con la función filter y con lambda la diferencia entre ambas soluciones es como implementé la función lambda.
.
.
.

Forma #1
Creando la función anónima directamente en el primer parámetro de la función filter"""

print("-----------forma 1----------- \n")

def filter_user_messages(messages, user):
  filtered = list(filter(lambda msg: msg["sender"].upper() == user.upper(), messages))
  return filtered

response = filter_user_messages([
  {'sender': 'Alice', 'content': 'Hola, ¿cómo estás?'},
  {'sender': 'Bob', 'content': '¡Bien, gracias!'},
  {'sender': 'Alice', 'content': '¿Quieres tomar un café?'},
  {'sender': 'Charlie', 'content': 'Hola a todos.'},
  {'sender': 'Alice', 'content': 'Nos vemos luego.'}
], "alice")

print(response)

# [{'sender': 'Alice', 'content': 'Hola, ¿cómo estás?'}, {'sender': 'Alice', 'content': '¿Quieres tomar un café?'}, {'sender': 'Alice', 'content': 'Nos vemos luego.'}]

  
"""Forma #2
Las funciones lambda al ser anónimas pueden asignarse a una variable y esa variable utilizarla como una función tal cual. Así que para la 2da forma asigne la función de filtrado a una variable llamada filter_by_user y esa “variable” (que en realidad es una función) la pase en el primer parámetro de filter."""

print("-----------forma 2----------- \n")

def filter_user_messages(messages, user):
  filter_by_user = lambda msg: msg["sender"].upper() == user.upper()
  filtered = list(filter(filter_by_user, messages))
  return filtered

response = filter_user_messages([
  {'sender': 'Alice', 'content': 'Hola, ¿cómo estás?'},
  {'sender': 'Bob', 'content': '¡Bien, gracias!'},
  {'sender': 'Alice', 'content': '¿Quieres tomar un café?'},
  {'sender': 'Charlie', 'content': 'Hola a todos.'},
  {'sender': 'Alice', 'content': 'Nos vemos luego.'}
], "alice")

print(response)
  
"""📢NOTA: filter recibe dos parámetros, la función que realiza el filtrado y la lista de los elementos que se van a filtrar. Es importante notar que al mandar el parámetro filter_by_user va sin paréntesis () por que nosotros no estamos ejecutando la función, sino que filter internamente lo hace, a esto se le llama higher order functions y se describen en la lectura que sigue."""