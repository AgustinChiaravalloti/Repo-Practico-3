#Ejercicio 9

cantidad = 10

suma = 0

for i in range(cantidad):
    num = int(input("Ingresá un número: "))
    suma += num

media = suma / cantidad

print("La media de los", cantidad, "números ingresados es:", media)