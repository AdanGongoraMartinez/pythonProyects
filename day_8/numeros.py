"""
Este modulo contiene los generadores y los decoradores
para el proyecto del dia 8
"""


def generador_perfumes():
    """
    Este generador muestra el turno que le corresponde a un cliente 
    para el departamento de perfumes
    """
    
    turno = 0
    
    while True:
        turno += 1
        yield f"P-{turno}"
    

def generador_farmacia():
    """
    Este generador muestra el turno que le corresponde a un cliente 
    para el departamento de farmacia
    """
    
    turno = 0
    
    while True:
        turno += 1
        yield f"F-{turno}"


def generador_cosmeticos():
    """
    Este generador muestra el turno que le corresponde a un cliente 
    para el departamento de cosmeticos
    """
    
    turno = 0
    
    while True:
        turno += 1
        yield f"C-{turno}"


p = generador_perfumes()
f = generador_farmacia()
c = generador_cosmeticos()



def decorador(rubro):
    """
    Este decorador imprime el turno del cliente en un formato entendible por el mismo

    Args:
        generador (): cualquier generador
    """
    
    print("*"*23)
    print("Su turno es:")
    
    if rubro == "P":
        print(next(p))
    elif rubro == "F":
        print(next(f))
    else:
        print(next(c))
    
    print("Aguarde y será atendido")
    print("*"*23)
