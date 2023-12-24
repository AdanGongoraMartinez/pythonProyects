# Ejercicio 1
""" Crea una función llamada devolver_distintos() que reciba 3
integers como parámetros.
Si la suma de los 3 numeros es mayor a 15, va a devolver el
número mayor.
Si la suma de los 3 numeros es menor a 10, va a devolver el
número menor.
Si la suma de los 3 números es un valor entre 10 y 15
(incluidos) va a devolver el número de valor intermedio."""

def devolver_distintos(entero1,entero2,entero3):
    numeros = [entero1+entero2+entero3]
    suma = 0

    for numero in numeros:
        suma += numero

    if suma > 15:
        return max(numeros)
    elif suma < 10:
        return min(numeros)
    else:
        numeros = sorted(numeros)
        return numeros[1]