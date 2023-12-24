# Ejercicio 2
"""Escribe una función (puedes ponerle cualquier nombre que
quieras) que reciba cualquier palabra como parámetro, y que
devuelva todas sus letras únicas (sin repetir) pero en orden
alfabético.
Por ejemplo si al invocar esta función pasamos la palabra
"entretenido", debería devolver ['d', 'e', 'i', 'n', 'o', 'r', 't']"""

def letras_utilizadas(palabra):
    letras = []

    for letra in palabra:
        letras.append(letra)
    
    letras = [letra for indice, letra in enumerate(letras) if letra not in letras[:indice]]

    return sorted(letras)
    
print(letras_utilizadas("entretenido"))