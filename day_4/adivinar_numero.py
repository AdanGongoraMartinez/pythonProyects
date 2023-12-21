from random import *

print("Intente adivinar el número entero que elegí, tiene 8 intentos.")

aleatorio = int(random()*100)

for intento in range(1,9):
    print(f"Intento #{intento}")
    numero = int(input("Ingrese un número entre 0 y 100: "))

    if numero > 100 or numero < 0:
        print("El número ingresado no es válido.")
    elif numero < aleatorio:
        print("El número ingresado es menor.")
    elif numero > aleatorio:
        print("El número ingresado es mayor.")
    else:
        print("Adivinó el número!!")
        print(f"Intentos: {intento} \nNúmero: ")
        break