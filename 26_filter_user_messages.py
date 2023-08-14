# Filtra mensajes de un user específico

"""
En este desafío implementarás una función que filtre los mensajes de un usuario específico. La función filter_user_messages recibirá dos parámetros:

messages: una lista de mensajes
user: un nombre de usuario.
Debe devolver una nueva lista que contenga solo los mensajes del usuario especificado.

La lista messages contiene diccionarios con información sobre cada mensaje, incluyendo el remitente ('sender') y el contenido del mensaje ('content').

En caso de no encontrar mensajes del usuario deberá retornar una lista vacía []

Ejemplo 1:

Input:

messages = [
  {'sender': 'Alice', 'content': 'Hola, ¿cómo estás?'},
  {'sender': 'Bob', 'content': '¡Bien, gracias!'},
  {'sender': 'Alice', 'content': '¿Quieres tomar un café?'},
  {'sender': 'Charlie', 'content': 'Hola a todos.'},
  {'sender': 'Alice', 'content': 'Nos vemos luego.'}
]

user = 'Alice'
filter_user_messages(messages, user)

Output:

[
  {'sender': 'Alice', 'content': 'Hola, ¿cómo estás?'},
  {'sender': 'Alice', 'content': '¿Quieres tomar un café?'},
  {'sender': 'Alice', 'content': 'Nos vemos luego.'}
]

"""

"""def filter_user_messages(messages, user):
  filtered_messages = filter(lambda msg: msg['sender'] == user, messages)
  return list(filtered_messages)

response = filter_user_messages([
  {'sender': 'Alice', 'content': 'Hola, ¿cómo estás?'},
  {'sender': 'Bob', 'content': '¡Bien, gracias!'},
  {'sender': 'Alice', 'content': '¿Quieres tomar un café?'},
  {'sender': 'Charlie', 'content': 'Hola a todos.'},
  {'sender': 'Alice', 'content': 'Nos vemos luego.'}
], "alice")

print(response)"""

def filtrar_mensajes_usuario(mensajes, usuario):

  # tambien puede ir list() antes de filter()
  filtrado_mensajes = filter(lambda mensaje: mensaje['sender'] == usuario, mensajes) # aquí el orden importa, si pongo primero mensajes y despues usuario me marca error
  return list(filtrado_mensajes) # ojo al no poner list si no nos imprime un iterable <filter object at 0x7fb787657790>
  
respuesta = filtrar_mensajes_usuario([
  {'sender': 'Alice', 'content': 'Hola, ¿cómo estás?'},
  {'sender': 'Alice', 'content': '¿Quieres tomar un café?'},
  {'sender': 'Alice', 'content': 'Nos vemos luego.'}
], usuario = 'Alice') # ojo con la coma antes de usuario
# podemos tambien quitar usuario y dejar solo 'Alice' tambien podemos usar upper() por si recibimos mayusculas como lo hizo Paola Camacho Alpiztle

print(respuesta)



"""
def filter_user_messages(messages, user):
  filtered_messages = filter(lambda msg: msg['sender'] == user, messages)
  return list(filtered_messages)

response = filter_user_messages([
  {'sender': 'Alice', 'content': 'Hola, ¿cómo estás?'},
  {'sender': 'Bob', 'content': '¡Bien, gracias!'},
  {'sender': 'Alice', 'content': '¿Quieres tomar un café?'},
  {'sender': 'Charlie', 'content': 'Hola a todos.'},
  {'sender': 'Alice', 'content': 'Nos vemos luego.'}
], "alice")

print(response)
"""