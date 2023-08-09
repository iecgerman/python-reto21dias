# Encapsulamiento en Python


"""
La encapsulación es uno de los principios fundamentales de la programación orientada a objetos, y se refiere a la idea de que los datos y métodos de un objeto deben estar protegidos y no deben ser accesibles directamente desde fuera del objeto. En Python, la encapsulación se logra utilizando convenciones de nomenclatura y, en el caso de las propiedades, mediante el uso de decoradores como @property.

A continuación, se presenta una explicación detallada sobre la encapsulación en Python:

Convenciones de Nomenclatura: En Python, se utilizan convenciones de nomenclatura para indicar el nivel de accesibilidad de los atributos y métodos de una clase. La convención más común es utilizar un guion bajo (_) al comienzo de un nombre de atributo o método para indicar que es un atributo o método privado, es decir, que no debería ser accedido directamente desde fuera de la clase. Aunque no hay restricciones técnicas para acceder a estos atributos o métodos, se considera una buena práctica no hacerlo. Por ejemplo:
class MiClase:
    def __init__(self):
        self._atributo_privado = 10

    def _metodo_privado(self):
        pass
Decorador @property: En Python, el decorador @property se utiliza para crear un método getter para acceder a un atributo privado como si fuera una propiedad pública. El método getter se denomina como la propiedad que se desea acceder y se define utilizando el decorador @property. Por ejemplo:
class MiClase:
    def __init__(self):
        self._atributo_privado = 10

    @property
    def atributo_publico(self):
        return self._atributo_privado
En este ejemplo, el atributo _atributo_privado es un atributo privado, pero se puede acceder a él desde fuera de la clase utilizando el método getter atributo_publico. Por ejemplo:

objeto = MiClase()
print(objeto.atributo_publico)  # Output: 10
Setter utilizando el decorador @atributo_publico.setter: En Python, también se puede utilizar el decorador @atributo_publico.setter para crear un método setter que permita modificar un atributo privado a través de una sintaxis similar a la asignación de una propiedad. El método setter se denomina como la propiedad que se desea modificar y se define utilizando el decorador @atributo_publico.setter. Por ejemplo:
class MiClase:
    def __init__(self):
        self._atributo_privado = 10

    @property
    def atributo_publico(self):
        return self._atributo_privado

    @atributo_publico.setter
    def atributo_publico(self, nuevo_valor):
        self._atributo_privado = nuevo_valor
En este ejemplo, el método setter atributo_publico permite modificar el atributo _atributo_privado utilizando una sintaxis similar a la asignación de una propiedad. Por ejemplo:

objeto = MiClase()
objeto.atributo_publico = 20
print(objeto.atributo_publico)  # Output: 20
Métodos y atributos privados: Además de utilizar la convención de nomenclatura con el guion bajo (_), se puede hacer uso de métodos y atributos privados en Python. Aunque técnicamente no hay restricciones de acceso, se considera una convención que los métodos y atributos que comienzan con dos guiones bajos (__) sean tratados como privados y no sean accedidos directamente desde fuera de la clase. Sin embargo, Python utiliza una técnica llamada name mangling para cambiar el nombre de estos atributos y métodos privados a nivel interno. Por ejemplo:
class MiClase:
    def __init__(self):
        self.__atributo_privado = 10

    def __metodo_privado(self):
        pass
En este ejemplo, el atributo __atributo_privado y el método __metodo_privado son privados, pero Python los renombra internamente utilizando el nombre de la clase que los contiene para evitar conflictos con clases derivadas. Por ejemplo, el atributo __atributo_privado se renombraría a _MiClase__atributo_privado internamente.
"""