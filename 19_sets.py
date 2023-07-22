Los sets en son estructuras de datos que permiten almacenar valores únicos. Los sets en Python no permiten duplicados, lo que los hace ideales cuando se necesita mantener una colección de elementos únicos.

Crear un set en Python es sencillo, puedes hacerlo de la siguiente manera:

my_set = set()
También es posible crear un set a partir de una lista existente:

my_list = [1, 2, 3, 4, 5]
my_set = set(my_list)
Algunos de los métodos más utilizados en los sets de Python son:

add(value): este método agrega un valor único al set. Si se intenta agregar un valor que ya existe en el set, no ocurrirá ningún cambio.
remove(value): este método elimina un valor específico del set. Si el valor no existe, se generará un error.
discard(value): este método elimina un valor específico del set. Si el valor no existe, no se genera ningún error.
pop(): este método elimina y devuelve un elemento aleatorio del set.
clear(): este método vacía completamente el set.
len(): esta función devuelve la cantidad de elementos que existen en el set.
Ejemplos de uso 👇

my_set = set()

# Agregar elementos al set
my_set.add(1)
my_set.add(2)
my_set.add(3)

# Imprimir el set
print(my_set)  # Output: {1, 2, 3}

# Verificar si un elemento existe en el set
print(2 in my_set)  # Output: True

# Eliminar un elemento del set
my_set.remove(2)

# Verificar si un elemento existe en el set después de ser eliminado
print(2 in my_set)  # Output: False

# Vaciar el set
my_set.clear()

# Verificar el tamaño del set después de ser vaciado
print(len(my_set))  # Output: 0

Iterar sobre sets
Los sets en Python no son estructuras indexadas, por lo que no se puede acceder a sus elementos mediante índices como se hace en las listas o tuplas. Sin embargo, es posible iterar sobre los elementos de un set utilizando un ciclo for-in.

Al iterar sobre un set, el ciclo for recorre automáticamente cada elemento del set en el orden en que fueron agregados.

Aquí un ejemplo de como hacerlo 👇

my_set = {1, 2, 3, 4, 5}

# Iterar sobre los elementos del set
for element in my_set:
    print(element)
En este ejemplo, se declara un set llamado my_set con algunos elementos. Luego, se utiliza el ciclo for-in para iterar sobre los elementos del set y se imprime cada elemento en la consola.

Usando slice syntax
También se puede utilizar la slice syntax([1:]) para iterar sobre un set a partir de un índice específico. Esta técnica permite omitir los primeros elementos del set durante la iteración.

Aquí un ejemplo de cómo utilizar esta sintaxis para iterar en un set a partir del segundo elemento:

my_set = {1, 2, 3, 4, 5}

# Iterar sobre los elementos del set a partir del segundo elemento
for item in my_set[1:]:
    print(item)
El set my_set contiene los elementos del 1 al 5. Al utilizar la sintaxis [1:], se indica que se desea iterar sobre los elementos a partir del segundo elemento (índice 1). Esto significa que se omitirá el primer elemento del set durante la iteración.

El resultado de este código será:

2
3
4
5

Cabe destacar que, a diferencia de las listas, los sets en Python no están indexados y no tienen un orden específico. Por lo tanto, al utilizar la slice syntax [1:] en un set, no se garantiza que se omitirán los primeros elementos en el mismo orden en que fueron agregados al set.

Intersecciones
Las intersecciones son una operación comúnmente utilizada en los sets para encontrar elementos que están presentes en dos o más sets al mismo tiempo. Puedes realizar la operación de intersección utilizando el método intersection() o el operador &.

Aquí tienes un ejemplo de cómo encontrar la intersección entre dos sets:

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Usando el método intersection()
intersection = set1.intersection(set2)
print(intersection)  # Output: {4, 5}

# Usando el operador &
intersection = set1 & set2
print(intersection)  # Output: {4, 5}
En este ejemplo, tenemos dos sets: set1 y set2. Queremos encontrar los elementos que están presentes en ambos sets. Utilizando el método intersection() o el operador &, obtenemos un nuevo set llamado intersection que contiene la intersección de los dos sets originales.

El resultado de la impresión será {4, 5}, ya que esos son los elementos que se encuentran en ambos sets.

Es importante tener en cuenta que la operación de intersección devuelve un nuevo set que contiene los elementos comunes entre los sets originales. Si alguno de los sets no tiene elementos en común con los otros sets, la intersección resultante será un set vacío.

Además, puedes realizar la intersección entre más de dos sets al mismo tiempo. Solo necesitas agregar los sets adicionales dentro de la función intersection() o utilizar el operador & entre ellos.