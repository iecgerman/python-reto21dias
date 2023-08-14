# CREDITOS A JULIO CARDENAS

from mail import Mail

class Queue:
  def __init__(self):
    self.cabeza   = None
    self.cola     = None
    self.longitud = 0
  
  def enqueue(self, from_email, to, body, subject):
    newMail = Mail(from_email, to, body, subject)  
    if self.longitud == 0:
      self.cabeza = newMail
      self.cola   = newMail
    else:
      self.cola.next = newMail
      self.cola = newMail
    self.longitud += 1  

  def dequeue(self):
     
    if self.longitud == 0:
      raise Exception("La cola esta vacia")
    else:
      salida = {} 
      salida["from"]    = self.cabeza.from_email
      salida["to"]      = self.cabeza.to
      salida["body"]    = self.cabeza.body
      salida["subject"] = self.cabeza.subject
      auxiliar = self.cabeza
      self.cabeza = self.cabeza.next
      del auxiliar
      self.longitud -= 1 
      if self.longitud == 0:
        self.cola = None 
      return salida

  
  def peek(self):
    if self.longitud == 0:
      raise Exception("La cola esta vacia")
    else:
      salida = {}
      salida["from"]    = self.cabeza.from_email
      salida["to"]      = self.cabeza.to
      salida["body"]    = self.cabeza.body
      salida["subject"] = self.cabeza.subject
      return salida
    
  def is_empty(self):
    return self.longitud == 0
  
  def size(self):
    return self.longitud 
  
queue = Queue()
  
queue.enqueue(
  "user1@example.com",
  "support@example.com",
  "Body 1",
  "Subject 1"
)

emailQueue = Queue()

emailQueue.enqueue(
    'jane@ejemplo.com',
    'support@ejemplo.com',
    'No puedo iniciar sesión en mi cuenta',
    'Problema de inicio de sesión'
)

emailQueue.enqueue(
    'joe@ejemplo.com',
    'support@ejemplo.com',
    'Mi pedido no ha llegado todavía',
    'Estado del pedido'
)

email = emailQueue.dequeue()
print(email)