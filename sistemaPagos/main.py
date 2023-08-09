# PASO 5

# OJO AQUI ME DIO EL SIGUIETE ERROR PORQUE NO ESTOY IMPORTANDO LOS MODULOS, EN ESTE CASO OCUPO EL MODULO pagar.py

""" line 11, in <module>
    pagar = Pagar()
NameError: name 'Pagar' is not defined"""

from pagar import Pagar
from efectivo import Efectivo
from paypal import PayPal
from tarjeta import Tarjeta

"""Por último se debe implementar la lógica de la función procesar_pago la cual recibirá un metodo_de_pago y la cantidad total_a_pagar, para poder devolver el objeto llamando al método hacer_pago de cada entidad recibida."""

# esto es super fácil debemos crear una funcion que retorne otra función con el objeto que ocupamos como el correo, la tarjeta, etc.

def procesar_pago(metodo_de_pago, total_a_pagar):
    return metodo_de_pago.hacer_pago(total_a_pagar)

print('**********Ejemplo 1:********** ')

tarjeta = Tarjeta("4913478952471122")
print(procesar_pago(tarjeta, 100)) # {'realizado': True, 'cantidad': 100, 'ultimos_4_digitos': '1122'}

print('\n**********Ejemplo 2:**********')

paypal = PayPal("test@mail.com")
print(procesar_pago(paypal, 240)) # {'realizado': True, 'cantidad': 240, 'plataforma': 'PayPal', 'correo': 'test@mail.com'}

print('\n**********Ejemplo 3:**********')

efectivo = Efectivo()
print(procesar_pago(efectivo, 400)) # {'realizado': True, 'cantidad': 400}

pagar = Pagar()
print(procesar_pago(pagar, 400)) # {'realizado': True, 'cantidad': 400}

print('\n********** Ejemplo con Error de tarjeta: **********')

tarjeta1 = Tarjeta("91347895247113453645634563453634221")
print(procesar_pago(tarjeta1, 100))

"""File "/home/runner/python-reto21dias/sistemaPagos/tarjeta.py", line 15, in hacer_pago
    raise Exception("La tarjeta debe contener 16 dígitos")
Exception: La tarjeta debe contener 16 dígitos"""