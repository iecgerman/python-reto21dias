"""
¿Qué es un Queue?
Un Queue (cola) es una estructura de datos lineal que sigue la regla de “primero en entrar, primero en salir” (FIFO). En otras palabras, el primer elemento que se inserta en la cola es el primero en ser eliminado. Funciona como una fila de elementos en la que nuevos elementos se agregan al final y se eliminan del frente. Las colas son útiles en situaciones donde es importante mantener el orden de llegada de los elementos.

Complejidad algorítmica
Los métodos en una cola tienen una complejidad algorítmica constante, lo que significa que la eficiencia no depende del tamaño de la cola. Veamos la complejidad de los principales métodos:

Algoritmo	Big O Notation
Acceder a elementos	O(n)
Insertar	O(1)
Eliminar	O(1)
Verificar si está vacía	O(1)
Verificar la cantidad	O(1)
Como se puede observar, las operaciones de acceso, inserción y eliminación son todas O(1), lo que hace que los queues sean altamente eficientes.

Oportunidades donde puedes usar un Queue
Hay diversas situaciones en las que es conveniente utilizar un Queue:

Procesamiento en el mismo orden de llegada: Cuando necesitas procesar datos en el mismo orden en que fueron recibidos, como mensajes de correo electrónico, solicitudes de clientes, tareas en un sistema de planificación, etc.
Registro de eventos: Para mantener un registro de los últimos elementos agregados o modificados, como los registros de transacciones de un sistema de base de datos.
Recorrido en amplitud (BFS): En algoritmos de búsqueda en árboles o grafos, como el recorrido en amplitud (BFS), donde se deben explorar los nodos en orden de proximidad desde un nodo inicial.
Situaciones en las que NO es muy conveniente usarlos

Aunque los queues son eficientes para ciertos casos, hay situaciones donde no son la mejor opción:

Acceso aleatorio: Si necesitas acceso aleatorio a los elementos (por índice), es más eficiente utilizar estructuras como arrays o listas enlazadas.
Búsqueda de elementos específicos: Si necesitas buscar elementos específicos dentro de la cola, también sería más eficiente usar una estructura de datos como un hash table (diccionario) para obtener una búsqueda más rápida.
Construyamos un Queue
A continuación, mostraremos una implementación de una cola en Python utilizando la clase Node para representar los nodos del queue y la clase Queue para definir la estructura de la cola:

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            raise IndexError("La queue está vacía")
        removed_node = self.first
        if self.first == self.last:
            self.last = None
        self.first = self.first.next
        self.length -= 1
        return removed_node.value

    def is_empty(self):
        return self.length == 0

    def size(self):
        return self.length
En esta implementación, la clase Node representa un nodo de la cola, con un constructor que inicializa el valor del nodo y establece next como None.

La clase Queue representa la cola y tiene un constructor que inicializa los punteros first y last como None y la longitud length en 0.

Los métodos implementados en la clase Queue son los siguientes:

enqueue: Agrega un nuevo nodo al final de la cola. Si la cola está vacía, tanto first como last apuntan al nuevo nodo. En caso contrario, se establece last.next para que apunte al nuevo nodo y se actualiza last para que apunte al nuevo nodo.
dequeue: Elimina y devuelve el valor del nodo en el frente de la cola. Si la cola está vacía, se lanza una excepción IndexError. Si first y last son iguales, se establece last en None. Se actualiza first para que apunte al siguiente nodo en la cola, se disminuye length en 1 y se devuelve el valor del nodo removido.
is_empty: Verifica si la cola está vacía comprobando si length es igual a 0.
size: Devuelve la cantidad de nodos en la cola, que es el valor de length.
Esta implementación nos permite crear y utilizar una cola eficiente en Python, respetando el principio de “primero en entrar, primero en salir”.
"""