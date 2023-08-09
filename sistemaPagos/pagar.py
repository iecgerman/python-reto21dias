# PASO 1

# Bueno primero que nada te piden que crees una clase base (padre) que se llame Pagar

class Pagar:
  def __init__(self): # agregamos su método constructor
    pass
  
  def hacer_pago(self, total_a_pagar):
    return {
      "realizado": True,
      "cantidad": total_a_pagar
    }
# seguido de eso debe de contener un único método llamado hacer_pago (make_pay)

"""Este método recibirá el total_a_pagar y devolverá un objeto con dos propiedades

realized: true
quantity: $cantidadAPagar"""


  
"""Además, deberás crear también las clases PayPal, Tarjeta (Card) y Efectivo (Cash), donde cada una debe heredar de la clase Pay.

Tenemos que crear paypal.py, efectivo.py y tarjeta.py"""