#Ejercicio 5

import random
num_secreto = random.randint(0,9)
contador= 0

while True:
  intento= int(input("Ingrese un numero aleatorio entre 0 y 9: "))
  contador += 1
   
  if intento == num_secreto:
       break
   

print("¡Adivinaste el número en", contador, "intento(s)!")