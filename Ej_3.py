#Ejercicio 3
contador = 0
valor_1 = int(input("ingrese el primer valor: "))
valor_2 = int(input("ingrese el segundo valor: "))

for i in range(min(valor_1,valor_2)+ 1, max(valor_1, valor_2)):
    contador= contador + 1
    
    
print("Cantidad de números entre los valores:", contador)