# Proyecto de juego de adivinacion
# uso de la libreria random
# uso de loops (for)
# uso de if, elif y else

from random import *

print("Intente adivinar el número entero que elegí, tiene 8 intentos.")

#aleatorio = int(random()*100)
aleatorio = randint(0,100)

print(aleatorio)

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
        print(f"Intentos: {intento} \nNúmero: {aleatorio}")
        break

if intento == 8 and numero != aleatorio:
    print(f"Número: {aleatorio}")