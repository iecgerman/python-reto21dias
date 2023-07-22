# 08 - Averigua si un año es bisiesto

def is_leap_year():

  year = float(input("Cual es el año: "))
  
  if (year % 4 == 0) or (year % 100 == 0):
  
    print(f"el año {year} es bisiesto")

  elif (year % 100 == 0) and (year % 400 == 0):
    print(f"el año {year} es bisiesto")

  else:
    print(f"El año {year} no es bisiesto")

is_leap_year()



# solucion de platzi
"""
def is_leap_year(year):
    if year % 1 != 0 or year <=0:
      return False
    
    if year % 4 == 0:
      if year % 100 == 0 and year % 400 == 0:
         return True

      if year % 100 == 0:
         return False
      
      return True
    
    return False
       

response = is_leap_year(2000)
print(response)
"""