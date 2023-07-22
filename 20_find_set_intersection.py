# Encuentre la intersección de conjuntos

def find_set_intersection(sets):
    if len(sets) == 0:
        return set()
    # recordemos que la varialbe sets es una lista de 3 conjuntos
    intersection = sets[0] # ejemplo: 
  #sets[0] = {1,2,3,4} 
  #sets[1] = {1,2,3,4,5}
  #sets[2] = {3, 4, 5, 6}
    
    for item in sets[1:]: # esto es del 1 al final
        intersection = intersection.intersection(item) # {1,2,3,4} & {2,3,4,5}
    
    return intersection


response = find_set_intersection([
    {1, 2, 3, 4},
    {2, 3, 4, 5},
    {3, 4, 5, 6}
])

print(response)