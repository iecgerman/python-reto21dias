# PASO 2

"""La clase PayPal debe recibir un correo (email) en el constructor y el método make_pay debe agregar las propiedades:

plataforma: "PayPal"
correo: $EmailRecibido."""

from pagar import Pagar

class PayPal(Pagar): # creamos la la clase hija que hereda la clase padre Pagar, recordemos que si queremos que esto funcione hay que importar Pagar
  def __init__(self, correo): #creamos su método constructor simepre usando self seguido del parámetro que utilizaremos en este caso correo
    self.xyz = correo # como dato si ponemos self.correo = correo no significan lo mismo, self.correo esta haciendo referencia a si mismo y despues del = correo es el parametro que recibiremos por ejemplo test@mail.com

  def hacer_pago(self, total_a_pagar):
    informacion_de_pago = super().hacer_pago(total_a_pagar)
    informacion_de_pago['plataforma'] = 'PayPal'
    informacion_de_pago['correo'] = self.xyz
    return informacion_de_pago