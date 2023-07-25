# Obten la información de los paquetes

def get_packages_info(packages):
  rta = {
    "total_weight": 0, # aquí el peso total se irá incrementanto de la suma de cada paquete como lo indica la linea 114
    "destinations": {} # aquí creamos un conjunto de paises para que no haya duplicados que se obtendran de la variable local existDestination
  }
  
  for package in packages:
    weight = package[1] # aqui para que entiendan tenemos una lista de tuplas por ejemplo (1, 20, "Mexico"), donde se leen (0, 1, 2) entoces en la linea 14 sumara todos los pesos de los paquetes
    destination = package[2] # aqui te nemos la posicion 2 de la tupla donde vamos a almacenarlos en la variable destination
    existDestination = rta["destinations"].get(destination)
    
    rta["total_weight"] += weight # esto es la suma de todos los pesos
    
    if existDestination is None: # aqui como exist_Destination empieza vacia (None) se get(obtine) de package[2] (ojo yo confudia que era leer la segunda tupla y es incorrecto) que es la primera tupla en la tercera posicion (1, 20, "Mexico")
      rta["destinations"][destination] = 1
    else:
      rta["destinations"][destination] += 1 # despues como ya no estara vacia (None) se le incremente un 1 para que sea 2 y obtenemos el siguiente pais, total si se repite no se puede duplicar porque los estamos almacenando en un conjunto (set)

  rta["total_weight"] = round(rta["total_weight"], 2) # es para que con round solo nos de los ultimos 2 digitos decimales

  return rta # retornamos a la variable rta

response = get_packages_info([
  (1, 20, "Mexico"),
  (2, 15.5, "Colombia"),
  (3, 30, "Mexico"),
  (4, 12, "Argentina"),
  (5, 8.2, "Colombia"),
  (6, 25, "Mexico"),
  (7, 18.7, "Argentina"),
  (8, 5, "Colombia"),
  (9, 22.3, "Argentina"),
  (10, 14.8, "Colombia")
])

print(response) # imprimimos la funcion get_packages_info

# {'total_weight': 171.5, 'destinations': {'Mexico': 3, 'Colombia': 4, 'Argentina': 3}}




"""print(list(response.items()))
print(list(response.keys()))
print(list(response.values()))"""
