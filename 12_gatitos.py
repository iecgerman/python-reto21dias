# Encuentra a los gatitos más famosos

"""
En este desafío, debes encontrar al gatito más famoso con base en su número de seguidores.

Recibirás una lista de diccionarios que incluirán las siguientes propiedades:

"name": nombre del gatito.
"followers": una lista de números, donde cada uno representa los seguidores de cada red social.
Tu tarea es devolver una lista con los nombres de los gatos que tienen solo el mayor número de seguidores. Si hay dos o más gatos con el mismo número máximo de seguidores, deberás incluirlos en la lista resultante, manteniendo el orden en el que aparecen en la lista de entrada.

Tendrás inputs y outputs como los siguientes 👇

Ejemplo 1:


Input: find_famous_cat([
  {
    "name": "Luna",
    "followers": [500, 200, 300]
  },
  {
    "name": "Michi",
    "followers": [100, 300]
  },
])

Output: ["Luna"]

Ejemplo 2:


Input: find_famous_cat([
  {
    "name": "Mimi",
    "followers": [320, 120, 70]
  },
  {
    "name": "Milo",
    "followers": [400, 300, 100, 200]
  },
  {
    "name": "Gizmo",
    "followers": [250, 750]
  }
])

Output: ["Milo", "Gizmo"]
"""

# muy buena la solución de Camilo Andrés Rodriguez Higuera

def find_famous_cat(cats):
  name = []
  followers = []
  famous = []
  
  for cat in cats:
    name.append(cat["name"])
    followers.append(sum(cat["followers"]))

  for i, value in enumerate(followers, 0): 
    if value == max(followers):
      famous.append(name[i])

  return famous  

response = find_famous_cat([
  {
    "name": "Luna",
    "followers": [500, 200, 300]
  },
  {
    "name": "Michi",
    "followers": [100, 300]
  },
])

print(response)




# SE PASARON DE BARRIGA CON ESTO, JAMAS LO IBA A HACER SOLO

# DEJARÉ ESTE COMENTARIO Y A VER SI EN UN FUTURO ESTO YA SE ME HACE MAS FACIL ENTENDERLO (18-JUL-2023)

"""def find_famous_cat(cats):
  famous_stats = {
    "famous_cats": [],
    "max_followers": 0
  }
  
  for cat in cats:
    total_followers = 0
    for num in cat["followers"]: # <= llave followers
      total_followers += num
      
    if total_followers > famous_stats["max_followers"]:
      famous_stats["max_followers"] = total_followers
      famous_stats["famous_cats"] = []
      famous_stats["famous_cats"].append(cat["name"])
    elif total_followers == famous_stats["max_followers"]:
      famous_stats["famous_cats"].append(cat["name"])
  
  return famous_stats["famous_cats"]
                                
response = find_famous_cat([
  {
    "name": "Luna",
		"followers": [500, 200, 300]
   },
   {
		"name": "Michi",
		"followers": [100, 500]
   },
  {
    "name": "Mimi",
    "followers": [320, 120, 70]
  },
  {
    "name": "Milo",
    "followers": [400, 300, 100, 200]
  },
  {
    "name": "Gizmo",
    "followers": [250, 750]
  }
])

print(response)"""