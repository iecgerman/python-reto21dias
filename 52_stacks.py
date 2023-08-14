"""
Un stack (o pila) es una estructura de datos lineal que sigue el principio “último en entrar, primero en salir” (Last In, First Out, LIFO). Esto significa que el último elemento agregado al stack será el primero en ser eliminado. En Python, podemos implementar un stack utilizando listas.

Complejidad Algorítmica
La complejidad de los métodos de un stack en Python depende de la implementación utilizada. Si se utiliza una lista, la complejidad es la siguiente:

Algoritmo	Notación Big O
Agregar un elemento (push)	O(1)
Eliminar un elemento (pop)	O(1)
Acceder al último elemento	O(1)
Acceder a un elemento en una posición específica	O(1)
En general, utilizar listas para implementar un stack en Python es una opción eficiente, ya que ofrece un buen rendimiento para todas las operaciones.

Construyamos un Stack en Python
A continuación, implementaremos un stack en Python utilizando una clase y aprovechando la estructura de lista nativa de Python.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def push(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.top = new_node
            self.bottom = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.length += 1

    def pop(self):
        if not self.top:
            return None
        if self.top == self.bottom:
            self.bottom = None
        popped_node = self.top
        self.top = self.top.next
        self.length -= 1
        return popped_node.value

    def peek(self):
        return self.top.value if self.top else None

    def is_empty(self):
        return self.length == 0
En esta implementación, hemos creado la clase Node que representa un nodo en el stack, y la clase Stack que implementa el stack en sí.

La clase Node tiene un constructor que inicializa el nodo con un valor y establece next como None.

La clase Stack tiene un constructor que inicializa el stack con top, bottom y length establecidos como None, None y 0, respectivamente.

Los métodos implementados en la clase Stack son los siguientes:

push: Agrega un nuevo nodo en la parte superior del stack. Si el stack está vacío, asigna el nuevo nodo tanto a top como a bottom. En caso contrario, hace que new_node.next apunte al nodo actual en la parte superior del stack, actualiza top para que apunte al nuevo nodo y aumenta length en 1.
pop: Elimina y devuelve el valor del nodo en la parte superior del stack. Si el stack está vacío, devuelve None. Si top y bottom son iguales, se establece bottom en None. Guarda el nodo en la parte superior en la variable popped_node, actualiza top para que apunte al siguiente nodo en el stack, disminuye length en 1 y devuelve el valor de popped_node.
peek: Devuelve el valor del nodo en la parte superior del stack sin eliminarlo. Si el stack está vacío, devuelve None.
is_empty: Verifica si el stack está vacío comprobando si length es igual a 0.
Oportunidades donde puedes usar un Stack
El stack es una estructura de datos muy versátil que puede utilizarse en diversas situaciones. Algunas oportunidades donde es conveniente utilizar un stack en Python incluyen:

Evaluación de expresiones matemáticas: Los stacks son útiles para evaluar expresiones matemáticas en notación postfija (o notación polaca inversa), donde los operadores siguen a sus operandos.
Reversión de cadenas: Puedes utilizar un stack para invertir el orden de los caracteres en una cadena.
Validación de sintaxis: Los stacks pueden ayudar a validar la sintaxis de expresiones, como verificar el equilibrio de paréntesis, corchetes y llaves.
Implementación de algoritmos como el recorrido en profundidad (DFS) de un grafo o la búsqueda en profundidad de un árbol.
Es importante tener en cuenta las características del stack y elegir la estructura de datos adecuada según los requisitos específicos del problema.

En resumen, hemos aprendido cómo implementar un stack en Python utilizando listas y una clase. También hemos explorado las oportunidades en las que un stack puede ser útil y la complejidad algorítmica de los métodos implementados.
"""

