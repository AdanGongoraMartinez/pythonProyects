1# Analizador de texto
# Cuenta el numero de veces que se repiten 3 letras
# Cuenta la cantidad de palabras
# Muestra las letras de inicio y fin
# Muestra el texto con las palabras en orden inverso
# Muestra si se encontro la palabra python

texto = input("Ingrese un texto:")

letras = []

texto.lower()

letras.append(input("Ingresa la primera letra:"))
letras.append(input("Ingresa la segunda letra:"))
letras.append(input("Ingresa la tercera letra:"))

print("\n")
print("CANTIDAD DE LETRAS")
cantidad_letras1 = texto.count(letras[0])
cantidad_letras2 = texto.count(letras[1])
cantidad_letras3 = texto.count(letras[2])

print(f"Hemos encontrado la letra '{letras[0]}' repetida {cantidad_letras1} veces")
print(f"Hemos encontrado la letra '{letras[1]}' repetida {cantidad_letras2} veces")
print(f"Hemos encontrado la letra '{letras[2]}' repetida {cantidad_letras3} veces")

print("\n")
print("CANTIDAD DE PALABRAS")
palabras = texto.split()
print(f"Hemos encontrado {len(palabras)} palabras en tu texto")

print("\n")
print("LETRAS DE INICIO Y FIN")
letra_inicio = texto[0]
letra_final = texto[-1]
print(f"La letra inicial es {letra_inicio} y la letra final es {letra_final}")

print("\n")
print("TEXTO INVERTIDO")
palabras.reverse()
texto_invertido = ' '.join(palabras)
print(f"Si ordenas el texto al revésva a decir: \n'{texto_invertido}'")

print("\n")
print("BUSCAR PYTHON")
buscar_python = 'python' in texto
diccionario = {True:"SI", False:"NO"}
print(f"La palabra 'Python' {diccionario[buscar_python]} se encuentra en el texto")
