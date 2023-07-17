# 06 - Calcular la propina

def calculate_tip(bill_amount, tipPercentage):
# aquí ojo porque no me salía, hasta que me dí cuenta que hay que hacer float las variables en la ecuación
    tip = float(bill_amount) * (float(tipPercentage) / 100)
    return round(tip, 2)

bill_amount = input("Captura el total de la cuenta a pagar: ") 
tipPercentage = input("¿Cuanto porcentaje de propina vas a dejar?: ")
print("Total a pagar: ", "$", bill_amount, "pesos")
print("Propina de un: ", tipPercentage, "%")

response = calculate_tip(bill_amount, tipPercentage)
print("Se dejó de propina de ", "$",response, "pesos")

"""
En este desafío tendrás que calcular la propina que deben dejar los clientes de un restaurante en función de su consumo.

La función calculate_tip recibirá dos parámetros, bill_amount que representa el costo total de lo que se haya consumido y tip_percentage que representa el porcentaje de propina a dejar. Ambos valores serán de tipo float y siempre serán positivos, incluyendo el 0. La función deberá devolver el valor de la propina como un número.

Recuerda que para redondear a dos decimales tendrás que hacer uso de round(numero, cantidad de decimales)

Tendrás inputs y outputs como los siguientes 👇

Ejemplo 1:


Input: calculate_tip(100, 10);
Output: 10;

Ejemplo 2:


Input: calculate_tip(1524.33, 25);
Output: 381.08;

# SOLUCION:

def calculate_tip(bill_amount, tipPercentage):
    tip = bill_amount * (tipPercentage / 100)
    return round(tip, 2)

response = calculate_tip(100, 10)
print(response)

"""