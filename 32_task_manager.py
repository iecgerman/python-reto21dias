# NO LE ENTIENDO NI MAIZ

def crear_planificador_de_tareas():
  tareas = []

  def agregar_tarea(tarea):
    tarea['completada'] = False 
    tareas.append(tarea)
  def remover_tarea(valor):
    if isinstance(valor, int):
      tareas[:] = [tarea for tarea in tareas if tarea['id'] != valor] 
    if isinstance(valor, str):
        tareas[:] = [tarea for tarea in tareas if tarea['nombre'] != valor]      
  def obtener_tarea():
    return tareas[:] 
  def obtener_tarea_pendiente():
    return [tarea for tarea in tareas if not tarea['compleatada']] 
  def obtener_tarea_completada():
    return [tarea for tarea in tareas if tarea['completada']]
  def marcar_tarea_como_completada(valor):
    if isinstance(valor, int):
      for tarea in tareas:
        if tarea['id'] == valor:
          tarea['completada'] = True 
          break
    elif isinstance(valor, str):
      for tarea in tareas:
        if tarea['nombre'] == valor:
          tarea['completada'] = True
          break      
  def obtener_ordenamiento_de_tarea_por_prioridad():
    return sorted(tareas, key=lambda tarea: tarea['prioridad'])
  def filtrar_tarea_por_etiquetado(etiqueta):
    return [tarea for tarea in tareas if etiqueta in tarea['etiquetas']]
  def actualizar_tarea(tarea_id, updates):
    for tarea in tareas:
      if tarea['id'] == tarea_id:
        tarea.update(updates)
        break
        
  return {
    'agregar_tarea': agregar_tarea,
    'remover_tarea': remover_tarea,
    'obtener_tarea': obtener_tarea,
    'obtener_tarea_pendiente': obtener_tarea_pendiente,
    'obtener_tarea_completada': obtener_tarea_completada,
    'marcar_tarea_como_completada': marcar_tarea_como_completada,
    'obtener_ordenamiento_de_tarea_por_prioridad': obtener_ordenamiento_de_tarea_por_prioridad,
    'filtrar_tarea_por_etiquetado': filtrar_tarea_por_etiquetado,
    'actualizar_tarea': actualizar_tarea,
  }

planner = crear_planificador_de_tareas()

planner['agregar_tarea']({
    'id': 1,
    'nombre': 'Comprar leche',
    'prioridad': 1,
    'etiquetas': ['shopping', 'home']
})

planner['agregar_tarea']({
    'id': 2,
    'nombre': 'Llamar a Juan',
    'prioridad': 3,
    'etiquetas': ['personal']
})

planner['marcar_tarea_como_completada']('Llamar a Juan')

print(planner['obtener_tarea_completada']())


# Crea un planificador de tareas usando closures

"""En este desafío, implementarás la lógica de un planificador de tareas en Python. El objetivo es construir la función closure llamada createTaskPlanner, que devolverá una serie de métodos para administrar las tareas. A continuación, se detallan los métodos que deben implementarse:

addTask(task): recibe un diccionario que contiene la información de la tarea y la agrega al array de tareas. El diccionario debe contener las siguientes claves: 'id', 'name', 'priority', 'tags' y 'completed'. La clave 'completed' se establecerá automáticamente como False al agregar una tarea.

removeTask(value): recibe el id o nombre de la tarea y la elimina del array de tareas.

getTasks(): devuelve el array de tareas.

getPendingTasks(): devuelve solo las tareas pendientes.

getCompletedTasks(): devuelve solo las tareas completadas.

markTaskAsCompleted(value): recibe el id o nombre de la tarea y la marca como completada.

getSortedTasksByPriority(): devuelve una copia de las tareas ordenadas según su prioridad (3: poco urgente, 2: urgente, 1: muy urgente), sin modificar la lista original de tareas.

filterTasksByTag(tag): filtra las tareas por una etiqueta específica. updateTask(taskId, updates): busca la tarea correspondiente al id especificado y actualiza sus propiedades con las especificadas en el diccionario de actualizaciones.

Ejemplo 1:

Input: 

planner = createTaskPlanner()

planner['addTask']({
    'id': 1,
    'name': 'Comprar leche',
    'priority': 1,
    'tags': ['shopping', 'home']
})

planner['addTask']({
    'id': 2,
    'name': 'Llamar a Juan',
    'priority': 3,
    'tags': ['personal']
})

planner['markTaskAsCompleted']('Llamar a Juan')

print(planner['getCompletedTasks']())

Output:

[{
  'id': 2,
  'name': 'Llamar a Juan',
  'completed': True,
  'priority': 3,
  'tags': ['personal']
}]

Ejemplo 2:


Input:
planner = createTaskPlanner()

planner['addTask']({
    'id': 1,
    'name': 'Comprar leche',
    'priority': 1,
    'tags': ['shopping', 'home']
})

planner['addTask']({
    'id': 2,
    'name': 'Llamar a Juan',
    'priority': 3,
    'tags': ['personal']
})

print(planner['filterTasksByTag']('shopping'))

Output:

[{
    'id': 1,
    'name': 'Comprar leche',
    'completed': False,
    'priority': 1,
    'tags': ['shopping', 'home']
}]"""




# SOLUCION DEL RETO EN INGLES CON CAMEL CASE
"""def createTaskPlanner():
  tasks = []

  def addTask(task):
    task['completed'] = False
    tasks.append(task)

  def removeTask(value):
    if isinstance(value, int):
      tasks[:] = [task for task in tasks if task['id'] != value] # a la madre ya me revolvi solo con leerlo
    elif isinstance(value, str):
      tasks[:] = [task for task in tasks if task['name'] != value]

  def getTasks():
    return tasks[:]

  def getPendingTasks():
    return [task for task in tasks if not task['completed']]

  def getCompletedTasks():
    return [task for task in tasks if task['completed']]

  def markTaskAsCompleted(value):
    if isinstance(value, int):
      for task in tasks:
        if task['id'] == value:
          task['completed'] = True
          break
    elif isinstance(value, str):
      for task in tasks:
        if task['name'] == value:
          task['completed'] = True
          break

  def getSortedTasksByPriority():
    return sorted(tasks, key=lambda task: task['priority'])

  def filterTasksByTag(tag):
    return [task for task in tasks if tag in task['tags']]

  def updateTask(taskId, updates):
    for task in tasks:
      if task['id'] == taskId:
        task.update(updates)
        break

  return {
    'addTask': addTask,
    'removeTask': removeTask,
    'getTasks': getTasks,
    'getPendingTasks': getPendingTasks,
    'getCompletedTasks': getCompletedTasks,
    'markTaskAsCompleted': markTaskAsCompleted,
    'getSortedTasksByPriority': getSortedTasksByPriority,
    'filterTasksByTag': filterTasksByTag,
    'updateTask': updateTask,
  }
  
# taskPlanner = createTaskPlanner()

planner = createTaskPlanner()

planner['addTask']({
    'id': 1,
    'name': 'Comprar leche',
    'priority': 1,
    'tags': ['shopping', 'home']
})

planner['addTask']({
    'id': 2,
    'name': 'Llamar a Juan',
    'priority': 3,
    'tags': ['personal']
})

planner['markTaskAsCompleted']('Llamar a Juan')

print(planner['getCompletedTasks']())

print('****' * 5)

planner = createTaskPlanner()

planner['addTask']({
    'id': 1,
    'name': 'Comprar leche',
    'priority': 1,
    'tags': ['shopping', 'home']
})

planner['addTask']({
    'id': 2,
    'name': 'Llamar a Juan',
    'priority': 3,
    'tags': ['personal']
})

print(planner['filterTasksByTag']('shopping'))"""