#Ejercicio 8

nombre = input("Ingrese su nombre: ")

print("Seleccione una opción:")
print("1. Convertir el nombre a MAYÚSCULAS")
print("2. Convertir el nombre a minúsculas")
print("3. Convertir el nombre con la primera letra en mayúscula")

opcion = input("Ingrese 1, 2 o 3 según su elección: ")

if opcion == "1":
    print("Resultado:", nombre.upper())
elif opcion == "2":
    print("Resultado:", nombre.lower())
elif opcion == "3":
    print("Resultado:", nombre.title())
else:
    print("Opción no válida. Por favor, ingrese 1, 2 o 3.")
