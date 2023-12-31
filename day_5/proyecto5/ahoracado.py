#Dia 5
"""Proyecto del juego del ahoracado
Uso de funciones y metodos"""

from random import *

def validar_ingreso():
    """Validar que el usuario este ingresando una letra del alfabeto"""

    while True:
        ingreso = input("Ingrese una letra: ")
        ingreso = ingreso.lower()

        if len(ingreso) > 1:
            print("Ingrese solo una letra.")
        elif 'a' <= ingreso <= 'z':
            return ingreso
        else:
            print("No se a ingresado una letra valida.")
        
        print("")

def elegir_palabra():
    """Elegir una palabra aleatoria de una lista"""

    palabras = ["python", "programacion", "aleatorio", "ejemplo", "lista"]
    return choice(palabras)

def preparar_palabra(palabra):
    """Crear una lista con los espacios a mostrar"""

    palabra_mostrar = []

    for i in enumerate(palabra):
        palabra_mostrar.append("_")
    
    return palabra_mostrar

def comprobar_resultados(palabra_mostrar):
    """Comprobar si la palanbra se ha completado"""

    if "_" in palabra_mostrar:
        return False
    else:
        return True

def restar_vidas(vidas):
    """funcion para restar y devolver las vidas"""

    return vidas - 1

def comprobar_victoria(vidas, palabra, palabra_mostrar):
    """Comprueba que el usuario tenga vidas y haya completado la palabra
    para determinar si el usuario ha ganado"""

    if vidas > 0 and comprobar_resultados(palabra_mostrar):
        print(f"Ganaste!\nTe quedaba(n) {vidas} vidas.\nLa palabra es {palabra}")
        vidas = 0
    elif vidas == 0:
        print(f"Has perdido!\nLa palabra es {palabra}")
    else:
        pass

    return vidas

def llenar_diccionario(vidas,palabra,palabra_mostrar):
    """Busca la letra dentro de la palabra y si la encuentra,
    reemplaza los '_' con la letra correspondiente"""

    ingreso = validar_ingreso()

    if ingreso in palabra:
        for indice,letra in enumerate(palabra):
            if letra == ingreso:
                palabra_mostrar[indice] = ingreso
    else:
        vidas = restar_vidas(vidas)
        print("La letra NO se encuentra en la palabra!\n")
    return vidas, palabra_mostrar

def mostrar_estado(vidas, palabra_mostrar):
    """Mostrar cuantas vidas tiene el jugador y mostrar cuantas
    letras han sido descubiertas"""
    
    print(f"Tiene: {vidas}")
    print(" ".join(palabra_mostrar))
    print("")

def empezar_juego(vidas):
    """Llamar a las demas funciones y crear un bucle que funcione hasta
    que el jugador se quede sin vidas o que complete la palabra"""

    print('*************************\n')
    palabra = elegir_palabra()
    palabra_mostrar = preparar_palabra(palabra)

    while vidas > 0:
        mostrar_estado(vidas, palabra_mostrar)
        vidas, palabra_mostrar = llenar_diccionario(vidas,palabra, palabra_mostrar)
        vidas = comprobar_victoria(vidas, palabra, palabra_mostrar)

        print('*************************\n')

if __name__ == "__main__":
    empezar_juego(5)