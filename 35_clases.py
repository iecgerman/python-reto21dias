# Crea un auto usando clases

"""En este desafío, deberás crear la lógica para un automóvil mediante el uso de clases.

Deberás implementar la lógica necesaria en la clase Car de tal manera que nos pueda servir de base para crear nuevos autos que reciba los siguientes parametros:

brand: Marca del auto
model: Modelo del auto
year: Año del auto
mileage: kilometraje del auto
state: El estado por defecto del auto será false, indicando que el - auto se encuentra apagado.
Además, deberás implementar los siguientes métodos para hacer funcional los vehículos creados con la clase Car

turnOn(): Método que encenderá el auto.
turnOff(): Método que apagará el auto.
drive(kilometers): Con este método podremos aumentar el kilometraje según los kilómetros dados pero solo si el auto está encendido. En caso contrario, deberá mostrar el siguiente mensaje de error: "El auto está apagado".
Recuerda manejar los errores como una Exception

Ejemplo 1:

Input:
toyota = Car("Toyota", "Corolla", 2020, 0);
toyota.turnOn();
toyota.drive(100);
toyota.mileage


Output: 100

Ejemplo 2

toyota = Car("Toyota", "Corolla", 2020, 0);
toyota.turnOff()
toyota.drive(100)

Output: Exception: El auto está apagado"""

class Carro:
  def __init__(self, marca, modelo, ano, kilometraje):
    self.marca = marca
    self.modelo = modelo
    self.ano = ano
    self.kilometraje = kilometraje
    self.estado = False

  def turnOn(self):
    self.estado = True

  def turnOff(self):
    self.estado = False

  def drive(self, kms):
    if(self.estado):
      self.kilometraje += kms
    else:
      raise Exception("El auto esta apagado")    

toyota = Carro("Toyota", "Corolla", 2020, 34)

print(toyota.marca) # Toyota
print(toyota.modelo) # Corolla
print(toyota.ano) # 2020
print(toyota.kilometraje) # 34
print(toyota.estado) # False




"""
nissan = Carro("Nissan", "Versa", 2023, 20)

print(toyota.marca) # Toyota
print(toyota.modelo) # Corolla
print(toyota.ano) # 2020
print(toyota.kilometraje) # 0

while True:
  encender = input("teclea encender: ")
  if (encender.lower() == 'encender'):
    Carro.turnOn(toyota)
    break
  else:
    Carro.turnOff(toyota)"""


# me siento bien contento porque esto fue hecho por mi solito, pero creditos al video de Soy Dalto del min 15 al 45
# https://www.youtube.com/watch?v=HtKqSJX7VoM&list=LL&index=3
"""
class Carro:
  def __init__(self, marca, modelo, ano, kilometraje):
    self.marca = marca
    self.modelo = modelo
    self.ano = ano
    self.kilometraje = kilometraje

  def turnOn(self):
    print(f"Encendiendo el Carro {self.marca} Modelo {self.modelo}")

  def turnOff(self):
    print(f"Apagando el Carro {self.marca} {self.modelo}")
    

toyota = Carro("Toyota", "Corolla", 2020, 0)
nissan = Carro("Nissan", "Versa", 2023, 20)

print(toyota.marca) # Toyota
print(toyota.modelo) # Corolla
print(toyota.ano) # 2020
print(toyota.kilometraje) # 0

while True:
  encender = input("teclea encender: ")
  if (encender.lower() == 'encender'):
    Carro.turnOn(toyota)
    break
  else:
    Carro.turnOff(toyota)
"""
    
  