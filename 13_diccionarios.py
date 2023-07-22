# Los diccionarios son una estructura de datos que permiten almacenar una colección de pares clave-valor. Las claves son strings y se utilizan para acceder a los valores correspondientes. 

mi_diccionario = {
    'clave1': valor1,
    'clave2': valor2,
    'clave3': valor3
}

# Por ejemplo, el siguiente código crea un diccionario llamado “curso” que tiene cinco pares clave-valor: “nombre”, “duración”, “clases”, “detalles” y “comentarios”:

curso = {
    'nombre': '30 días de Python',
    'duración': '20 horas',
    'clases': 100,
    'detalles': {
        'tecnologias': ['Python', 'Flask', 'Django'],
        'calificacion': 5,
    },
    'comentarios': ['¡Excelente curso!', 'Python es poderoso', 'Hola']
}

# Para acceder a los valores de un diccionario, se utiliza la notación de corchetes y se especifica la clave.

print(curso['nombre']) 
# "30 días de Python"

# Además de los valores, los diccionarios también pueden tener métodos, que son funciones asociadas a un diccionario. Por ejemplo, el siguiente código crea un diccionario “coche” con una clave “marca” y un método “encender”:

coche = {
    'marca': 'Toyota',
    'encender': lambda: print('El coche ha sido encendido')
}

# Para llamar a un método de un diccionario, se utiliza la notación de corchetes y se especifica la clave.

coche['encender']() # "El coche ha sido encendido"

# Python también tiene una característica llamada herencia, que permite crear nuevos diccionarios a partir de diccionarios existentes y heredar sus pares clave-valor. Esto permite a los desarrolladores crear nuevos objetos a partir de objetos existentes y agregar o modificar sus pares clave-valor, pero esto lo verás mucho más adelante, por el momento no tienes de que preocuparte.