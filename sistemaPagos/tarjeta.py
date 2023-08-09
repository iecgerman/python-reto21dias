# PASO 3

"""La clase Card recibirá un número de tarjeta de 16 dígitos. Al momento de acceder al método hacer_pago, se validará si la tarjeta en cuestión tiene esa longitud. En caso de no tener los 16 dígitos, se debe lanzar una Exception. En caso contrario, al método que proviene de la clase padre Pagar, se le agregará la propiedad de ultimos_4_digitos: donde se devolverán los últimos 4 dígitos de la tarjeta."""

# improtamos la clase padre Pagar

from pagar import Pagar

class Tarjeta(Pagar): # la clase Tarjeta hereda la superclase Pagar
  def __init__(self, numero_de_tarjeta): # creamos método constructor
    self.numero_de_tarjeta = numero_de_tarjeta # hacemos referencia al parámetro

  def hacer_pago(self, total_a_pagar):
    if len(self.numero_de_tarjeta) != 16: #
      raise Exception("La tarjeta debe contener 16 dígitos")
    informacion_de_pago = super().hacer_pago(total_a_pagar) # aqui con super()estamos heredando de la superclase Pagar donde ahi se encuentra el método def hacer_pago()
    informacion_de_pago["ultimos_4_digitos"] = self.numero_de_tarjeta[-4:] #
    return informacion_de_pago

