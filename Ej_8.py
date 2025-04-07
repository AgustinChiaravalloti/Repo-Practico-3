#Ejercicio 8

pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(4):
    num = int(input("Ingresá un número: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

    if num > 0:
     positivos += 1
    elif num < 0:
     negativos += 1
     
print("Pares:", pares)
print("Impares:", impares)
print("Positivos:", positivos)
print("Negativos:", negativos)