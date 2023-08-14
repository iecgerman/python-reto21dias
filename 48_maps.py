# Maps en Python

"""
Los Maps en Python son estructuras de datos que permiten almacenar pares clave-valor y acceder a ellos de manera eficiente. A diferencia de los diccionarios regulares, las claves en un Map pueden ser de cualquier tipo de dato inmutable, incluyendo enteros, cadenas, tuplas y objetos personalizados. Los Maps son especialmente útiles cuando se necesitan realizar búsquedas rápidas de valores asociados a una clave determinada.

Para crear un Map en Python, se puede utilizar la siguiente sintaxis:

map = {}
También es posible crear un Map a partir de una lista de pares clave-valor:

pairs = [("key1", "value1"), ("key2", "value2")]
map = dict(pairs)
Los métodos más utilizados de los Maps en Python son los siguientes:

map[key] = value: este método agrega un par clave-valor al Map.
value = map.get(key): este método devuelve el valor asociado a una clave determinada. Si la clave no existe, devuelve None.
key in map: este método verifica si una clave determinada existe en el Map. Devuelve True si la clave existe y False en caso contrario.
del map[key]: este método elimina una clave y su valor asociado del Map.
map.clear(): este método vacía completamente el Map.
len(map): esta función devuelve la cantidad de pares clave-valor que existen en el Map.
Ejemplos de uso de Map en Python:

map = {}

# Agregar pares clave-valor al Map
map["key1"] = "value1"
map["key2"] = "value2"
map[3] = "value3"

# Obtener el valor asociado a una clave
print(map.get("key1"))  # Output: "value1"

# Verificar si una clave existe en el Map
print("key2" in map)  # Output: True

# Eliminar una clave del Map
del map["key2"]

# Verificar si una clave existe en el Map después de ser eliminada
print("key2" in map)  # Output: False

# Vaciar el Map
map.clear()

# Verificar el tamaño del Map después de ser vaciado
print(len(map))  # Output: 0

En resumen, los Maps en Python son estructuras de datos útiles para almacenar pares clave-valor y para realizar operaciones eficientes de búsqueda, adición y eliminación de valores asociados a una clave determinada.
"""

