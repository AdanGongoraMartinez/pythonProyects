import pygame
import random

# Inicializar Pygame
pygame.init()

# Definir colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AMARILLO = (255, 255, 0)
MAGENTA = (255, 0, 255)
CIAN = (0, 255, 255)

# Definir tamaño de la pantalla
ANCHO = 400
ALTO = 600

# Definir tamaño de bloque
TAMANO_BLOQUE = 30

# Definir grilla
ANCHO_GRILL = 10
ALTO_GRILL = 20

# Definir velocidad de caída de las piezas (en milisegundos)
VELOCIDAD_CAIDA = 500

# Definir formas de las piezas
formas = [
    [[1, 1, 1],
     [0, 1, 0]],
    [[1, 1],
     [1, 1]],
    [[1, 1, 0],
     [0, 1, 1]],
    [[0, 1, 1],
     [1, 1, 0]],
    [[1, 1, 1, 1]],
    [[1, 1, 1],
     [0, 0, 1]],
    [[1, 1, 1],
     [1, 0, 0]]
]

# Clase Pieza
class Pieza:
    def __init__(self, forma, color):
        self.forma = forma
        self.color = color
        self.x = ANCHO_GRILL // 2 - len(self.forma[0]) // 2
        self.y = 0

# Función principal del juego
def main():
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Tetris")
    reloj = pygame.time.Clock()

    grilla = [[None] * ANCHO_GRILL for _ in range(ALTO_GRILL)]

    pieza_actual = nueva_pieza()

    terminado = False
    tiempo_pasado = 0

    while not terminado:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                terminado = True
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    pieza_actual.x -= 1
                    if not validar_posicion(pieza_actual, grilla):
                        pieza_actual.x += 1
                elif evento.key == pygame.K_RIGHT:
                    pieza_actual.x += 1
                    if not validar_posicion(pieza_actual, grilla):
                        pieza_actual.x -= 1
                elif evento.key == pygame.K_DOWN:
                    pieza_actual.y += 1
                    if not validar_posicion(pieza_actual, grilla):
                        pieza_actual.y -= 1

        tiempo_pasado += reloj.tick()
        if tiempo_pasado > VELOCIDAD_CAIDA:
            pieza_actual.y += 1
            if not validar_posicion(pieza_actual, grilla):
                pieza_actual.y -= 1
                agregar_pieza_a_grilla(pieza_actual, grilla)
                pieza_actual = nueva_pieza()
            tiempo_pasado = 0

        pantalla.fill(NEGRO)

        dibujar_grilla(pantalla, grilla)
        dibujar_pieza(pantalla, pieza_actual)

        pygame.display.flip()

    pygame.quit()

# Función para crear una nueva pieza aleatoria
def nueva_pieza():
    forma = random.choice(formas)
    color = random.choice([AZUL, VERDE, ROJO, AMARILLO, MAGENTA, CIAN])
    return Pieza(forma, color)

# Función para dibujar una pieza en la pantalla
def dibujar_pieza(pantalla, pieza):
    forma = pieza.forma
    color = pieza.color
    for y, fila in enumerate(forma):
        for x, valor in enumerate(fila):
            if valor:
                pygame.draw.rect(pantalla, color, (pieza.x * TAMANO_BLOQUE + x * TAMANO_BLOQUE,
                                                    pieza.y * TAMANO_BLOQUE + y * TAMANO_BLOQUE,
                                                    TAMANO_BLOQUE, TAMANO_BLOQUE))

# Función para validar la posición de una pieza
def validar_posicion(pieza, grilla):
    forma = pieza.forma
    for y, fila in enumerate(forma):
        for x, valor in enumerate(fila):
            if valor:
                if (pieza.x + x < 0 or
                    pieza.x + x >= ANCHO_GRILL or
                    pieza.y + y >= ALTO_GRILL or
                    grilla[pieza.y + y][pieza.x + x]):
                    return False
    return True

# Función para agregar una pieza a la grilla
def agregar_pieza_a_grilla(pieza, grilla):
    forma = pieza.forma
    color = pieza.color
    for y, fila in enumerate(forma):
        for x, valor in enumerate(fila):
            if valor:
                grilla[pieza.y + y][pieza.x + x] = color

# Función para dibujar la grilla
def dibujar_grilla(pantalla, grilla):
    for y, fila in enumerate(grilla):
        for x, color in enumerate(fila):
            if color:
                pygame.draw.rect(pantalla, color, (x * TAMANO_BLOQUE, y * TAMANO_BLOQUE, TAMANO_BLOQUE, TAMANO_BLOQUE), 0)
                pygame.draw.rect(pantalla, BLANCO, (x * TAMANO_BLOQUE, y * TAMANO_BLOQUE, TAMANO_BLOQUE, TAMANO_BLOQUE), 1)

if __name__ == "__main__":
    main()
