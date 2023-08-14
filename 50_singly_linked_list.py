# Singly Linked List en Python

"""
Una Singly Linked List (lista enlazada simple) es una estructura de datos lineal en la que cada elemento (nodo) contiene un valor y un puntero al siguiente nodo en la lista. La lista enlazada comienza con un nodo llamado cabeza (head) que apunta al primer elemento de la lista, y termina con un nodo llamado cola (tail) que apunta a None.

Complejidad Algorítmica
La siguiente tabla muestra la complejidad algorítmica (notación Big O) de las diferentes operaciones en las singly linked lists:

Algoritmo	Notación Big O
Acceder a Elementos	O(n)
Inserción al Inicio	O(1)
Inserción al Final	O(n)
Inserción en Medio	O(n)
Eliminación al Inicio	O(1)
Eliminación al Final	O(n)
Eliminación en Medio	O(n)
Ventajas de las Singly Linked Lists
Inserción y eliminación rápida de elementos al inicio de la lista, ya que solo se necesita actualizar el puntero de la cabeza (head), lo cual se realiza en tiempo constante O(1).
Tamaño dinámico: Las singly linked lists pueden crecer o reducir su tamaño dinámicamente sin necesidad de reasignar memoria para una estructura de datos de tamaño fijo.
Eficiencia en memoria: Las singly linked lists solo requieren el espacio necesario para almacenar el valor de cada nodo y un puntero al siguiente nodo, lo que las hace más eficientes en términos de uso de memoria en comparación con otras estructuras de datos como los arrays.
Limitaciones de las Singly Linked Lists
Acceder a un elemento en una posición específica de la lista requiere recorrer la lista desde la cabeza hasta la posición deseada, lo cual toma tiempo lineal O(n) en el peor de los casos.
Las singly linked lists no admiten el recorrido hacia atrás, ya que solo tienen un enlace que apunta al siguiente nodo y no al nodo anterior.
Realizar operaciones de búsqueda frecuentes puede ser ineficiente, ya que en el peor de los casos la búsqueda requiere recorrer toda la lista, lo cual tomaría tiempo lineal O(n). En estos casos, sería más eficiente utilizar otras estructuras de datos como los árboles de búsqueda binarios o las tablas hash.
Implementación de Singly Linked List en Python
En Python, se puede implementar una singly linked list utilizando clases. Cada nodo de la lista es un objeto que tiene dos propiedades: value, que almacena el valor del nodo, y next, que apunta al siguiente nodo en la lista.

Veamos un ejemplo de cómo se puede construir una singly linked list en Python:

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def delete(self, value):
        if self.head is None:
            return
        if self.head.value == value:
            self.head = self.head.next
            self.length -= 1
            return
        current_node = self.head
        while current_node.next:
            if current_node.next.value == value:
                current_node.next = current_node.next.next
                self.length -= 1
                return
            current_node = current_node.next

En la implementación anterior, tenemos dos clases: Node y LinkedList. La clase Node representa un nodo en la lista, mientras que la clase LinkedList es la lista en sí misma.

El método append agrega un nuevo nodo al final de la lista. Si la lista está vacía, los punteros head y tail se actualizan para que apunten al nuevo nodo. De lo contrario, se actualiza el puntero next del último nodo en la lista para que apunte al nuevo nodo, y el puntero tail se actualiza para que apunte al nuevo nodo.

El método prepend agrega un nuevo nodo al inicio de la lista. Si la lista está vacía, los punteros head y tail se actualizan para que apunten al nuevo nodo. De lo contrario, se actualiza el puntero next del nuevo nodo para que apunte al nodo actual de la cabeza, y el puntero head se actualiza para que apunte al nuevo nodo.

El método delete elimina un nodo con un valor dado de la lista. Si el valor se encuentra en el nodo de la cabeza, el puntero head se actualiza para que apunte al siguiente nodo. De lo contrario, se recorre la lista hasta encontrar el nodo anterior al nodo que se desea eliminar. Una vez encontrado, se actualiza el puntero next del nodo anterior para que salte el nodo a eliminar.

Utilizando esta implementación, podemos aprovechar las ventajas de las singly linked lists para realizar operaciones eficientes de inserción y eliminación. Sin embargo, es importante tener en cuenta las limitaciones y elegir la estructura de datos adecuada según los requisitos específicos del problema.
"""