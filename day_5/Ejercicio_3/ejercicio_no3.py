# Ejercicio 3
"""Escribe una función que requiera una cantidad indefinida de
argumentos. Lo que hará esta función es devolver True si en
algún momento se ha ingresado al numero cero repetido dos
veces consecutivas.
Por ejemplo:
(5,6,1,0,0,9,3,5) >>> True
(6,0,5,1,0,3,0,1) >>> False"""

def cero_consecutivo(*args):
    numeros = []

    respuesta = False

    for numero in args:
        numeros.append(numero)
    
    for indice in range(len(numeros)-1):
        if numeros[indice] == numeros[indice+1] and numeros[indice] == 0:
            respuesta = True
        else:
            pass
    
    return respuesta

print(cero_consecutivo(5,6,1,0,0,9,3,5))
print(cero_consecutivo(6,0,5,1,0,3,0,1))