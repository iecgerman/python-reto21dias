# Abstracción en Python

"""
La abstracción es un concepto fundamental en la programación orientada a objetos que permite representar objetos y sus características de manera simplificada, ocultando los detalles internos de su implementación. En Python, la abstracción se logra mediante el uso de clases, métodos y herencia. A continuación, se presenta una explicación detallada sobre la abstracción en Python:

Clases y Objetos: En la abstracción, una clase es una plantilla que define las propiedades y comportamientos de un objeto. Un objeto, por otro lado, es una instancia de una clase. La clase define una interfaz clara y simplificada para interactuar con los objetos, ocultando los detalles internos de cómo se implementa esa funcionalidad. Para definir una clase en Python, se utiliza la palabra clave class, seguida del nombre de la clase:
class MiClase:
    # Definición de propiedades y métodos de la clase
Para crear un objeto a partir de una clase, se utiliza la siguiente sintaxis:

objeto = MiClase()
Métodos: Los métodos son funciones definidas dentro de una clase y representan el comportamiento de los objetos. Los métodos permiten interactuar con los objetos y realizar operaciones específicas. Pueden recibir parámetros y acceder a las propiedades del objeto a través del parámetro self. Los métodos ayudan a definir la interfaz de la clase, ofreciendo una forma simplificada de interactuar con los objetos sin necesidad de conocer los detalles internos. Por ejemplo:
class MiClase:
    def metodo(self, parametro):
        # Código del método
        pass
Herencia: La herencia es un mecanismo que permite crear nuevas clases basadas en clases existentes. Una clase derivada o subclase hereda las propiedades y métodos de una clase base o superclase, lo que facilita la reutilización de código y permite definir nuevas funcionalidades adicionales. En Python, se utiliza la palabra clave class seguida del nombre de la subclase y entre paréntesis el nombre de la superclase:
class ClaseBase:
    # Definición de la clase base

class SubClase(ClaseBase):
    # Definición de la subclase
La subclase puede agregar nuevos métodos o atributos, o modificar los existentes de la clase base. Esto permite extender la funcionalidad y crear una abstracción más específica. Por ejemplo:

class ClaseBase:
    def metodo_base(self):
        # Código del método base
        pass

class SubClase(ClaseBase):
    def metodo_subclase(self):
        # Código del método de la subclase
        pass
Sobreescritura de Métodos: La sobreescritura de métodos es una técnica utilizada en la abstracción que permite a una subclase redefinir un método heredado de la superclase. Al sobre escribir un método, la subclase puede modificar o ampliar el comportamiento del método heredado. Esto permite adaptar la funcionalidad a las necesidades específicas de la subclase. Por ejemplo:
class ClaseBase:
    def metodo(self):
        # Código del método base
        pass

class SubClase(ClaseBase):
    def metodo(self):
        # Código del método modificado
        pass
Cuando se llama al método metodo() en un objeto de la subclase, se ejecuta la versión del método definida en la subclase en lugar de la versión heredada de la superclase.
"""