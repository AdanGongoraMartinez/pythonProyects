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
        if self.balance > retiro:
            print("SALDO INSUFICIENTE")
        else:
            self.balance = retiro

def crear_cliente(nombre,apellido):
    cliente = Cliente(nombre,apellido,888888,100)

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
            eleccion = input("\nIngrese una opcion")

        system("clear")
        eleccion = int(eleccion)

        if eleccion == 1:
            nombre_cliente = input("Ingrese el nombre del cliente")
            apellido_cliente = input("Ingrese el apellido del cliente")

            cliente = crear_cliente(nombre_cliente,apellido_cliente)

            existe_cliente = True
        elif eleccion == 2:
            if existe_cliente:
                pass
        elif eleccion == 3:
            pass
        elif eleccion == 4:
            pass
        elif eleccion == 5:
            parar = True

inicio()