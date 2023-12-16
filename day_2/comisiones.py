#Proyecto para calcular las comiones de un empleado mediante sus ventas

#Transforacion de tipos de datos e impresion de variables
#usando formateo de strings

nombre = input("Por favor, dime tu nombre: ")
ventas = int(input("Diga sus ventas totales del mes: "))

comision = round(ventas * 0.13, 2)

print(f"Hola {nombre}, tus comisiones de este mes son de ${comision}")
