"""
Este modulo contiene el programa principal
Un sistema de asignacion de turnos para los clientes 
de 3 departamentos: Perfumes, farmacia y cosmeticos
"""


import numeros
from os import system


def tomar_turno(rubro):
    """
    Esta funcion esta encargada de mostrarle al usuario su turno
    
    Args:
        rubro (string): hace referencia al departamento
    """
    
    if rubro == "P":
        nombre_rubro = "perfumes"
    elif rubro == "F":
        nombre_rubro = "farmacia"
    else:
        nombre_rubro = "cosmeticos"
    
    while True:
        seleccion = input(f"¿Quiere un número para el departamento de {nombre_rubro}? (Y/N)")
        
        if seleccion == "y" or seleccion == "Y":
            system("clear")
            numeros.decorador(rubro)
        elif seleccion == "n" or seleccion == "N":
            break
        else:
            print("Ingrese 'Y' o 'N'")


def menu():
    """
    El cuerpo principal del programa
    Crea un menu de opciones para que el usuario elija
    a cual departamento quiere acceder
    """
    
    while True:
        print("[1] - Perfumes")
        print("[2] - Farmacia")
        print("[3] - Cosmetico")
        print("[4] - Salir")
        
        while True:
            try:
                eleccion = int(input("Selecciones una opcion: "))
            except:
                print("Ingrese un numero.")
            else:
                if 1 <= eleccion <= 4:
                    break
                else:
                    print("Ingrese un numero valido.")
        
        system("clear")
        
        if eleccion == 1:
            tomar_turno("P")
        elif eleccion == 2:
            tomar_turno("F")
        elif eleccion == 3:
            tomar_turno("C")
        else:
            break
        
        system("clear")


menu()
