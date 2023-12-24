# Ejercicio 4
"""Escribe una función llamada contar_primos() que requiera un
solo argumento numérico.
Esta función va a mostrar en pantalla todos los números
primos existentes en el rango que va desde cero hasta ese
número incluido, y va a devolver la cantidad de números
primos que encontró.
Aclaración, por convención el 0 y el 1 no se consideran primos."""

def es_primo(numero):
    """Verifica si un número es primo."""
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def contar_primos(fin):
    """Cuenta cuántos números primos hay en un rango."""
    cantidad_primos = 0
    for num in range(fin + 1):
        if es_primo(num):
            cantidad_primos += 1
    return cantidad_primos

print(contar_primos(8))