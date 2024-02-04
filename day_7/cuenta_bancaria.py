from os import system

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self,nombre,apellido,numero_cuenta,balance):
        super().__init__(nombre,apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance
    
    def __str__(self):
        return f" NOMBRE: {self.nombre} {self.apellido}\n NUM_CUENTA: {self.numero_cuenta}\n BALANCE: {self.balance}"

    def depositar(self, deposito):
        self.balance += deposito

    def retirar(self,retiro):
        self.balance = retiro

def crear_cliente(nombre,apellido, cuenta):
    cliente = Cliente(nombre,apellido,cuenta,0)

    return cliente

def inicio():
    parar = False
    existe_cliente = False

    while not parar:
        print("CUENTA BANCARIA")
        print("[1] - Crear cliente")
        print("[2] - Imprimir Informacion del cliente")
        print("[3] - Depositar")
        print("[4] - Retirar")
        print("[5] - Salir")

        eleccion = 'x'
        while not eleccion.isnumeric() or int(eleccion) not in range(1,6):
            eleccion = input("\nIngrese una opcion: ")

        system("clear")
        eleccion = int(eleccion)

        if eleccion == 1:
            nombre_cliente = input("Ingrese el nombre del cliente: ")
            apellido_cliente = input("Ingrese el apellido del cliente: ")
            cuenta_cliente = input("Ingrese el numero de cuenta del cliente: ")


            cliente = crear_cliente(nombre_cliente,apellido_cliente,cuenta_cliente)

            existe_cliente = True

        elif existe_cliente == True:
            if eleccion == 2:
                print(cliente)

                volver = 'x'
                while volver != 'v':
                    volver = input("\nIngrese v para volver: ")

            elif eleccion == 3:
                cantidad_deposito = 'x'
                while not cantidad_deposito.isnumeric() or int(cantidad_deposito) < 0:
                    cantidad_deposito = input("Ingrese la cantidad a depositar: ")
                
                cliente.depositar(int(cantidad_deposito))

                print(f"Ha depositado {cantidad_deposito}")

                volver = 'x'
                while volver != 'v':
                    volver = input("\nIngrese v para volver: ")

            elif eleccion == 4:
                cantidad_retiro = 'x'
                es_mayor = False

                while not es_mayor:
                    while not cantidad_retiro.isnumeric() or int(cantidad_retiro) < 0:
                        cantidad_retiro = input("Ingrese la cantidad a depositar: ")

                    if int(cantidad_retiro) > cliente.balance:
                        print("Balance Insuficiente.")
                    else:
                        es_mayor = True
                
                cliente.retirar(int(cantidad_retiro))

                print(f"Ha retirado {cantidad_retiro}")

                volver = 'x'
                while volver != 'v':
                    volver = input("\nIngrese v para volver: ")

            elif eleccion == 5:
                parar = True
        else:
            print("Por favor cree un cliente.")

            volver = 'x'
            while volver != 'v':
                volver = input("\nIngrese v para volver: ")
        
        system("clear")

inicio()