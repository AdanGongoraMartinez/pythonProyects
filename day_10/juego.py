import pygame
import random
import math
from pygame import mixer

# Inicializar Pygame
pygame.init()

# Crar pantalla
pantalla = pygame.display.set_mode((800, 600))

# titulo e icono
pygame.display.set_caption("Space invader")
icono = pygame.image.load("/home/adan/Documentos/github - local/pythonProyects/day_10/alien.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load('/home/adan/Documentos/github - local/pythonProyects/day_10/fondo.jpg')

# agregar musica
mixer.music.load('/home/adan/Documentos/github - local/pythonProyects/day_10/MusicaFondo.mp3')
mixer.music.set_volume(0.3)
mixer.music.play(-1)


# Variables jugador
imagen_jugador = pygame.image.load("/home/adan/Documentos/github - local/pythonProyects/day_10/nave-espacial.png")
jugador_x = 368
jugador_y = 536
jugador_x_cambio = 0
jugador_y_cambio = 0

# Variables enemigo
imagen_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 8

for e in range(cantidad_enemigos):
    imagen_enemigo.append(pygame.image.load("/home/adan/Documentos/github - local/pythonProyects/day_10/ovni.png"))
    enemigo_x.append(random.randint(0,736))
    enemigo_y.append(random.randint(50,200))
    enemigo_x_cambio.append(0.8)
    enemigo_y_cambio.append(50)

# Variables bala
imagen_bala = pygame.image.load("/home/adan/Documentos/github - local/pythonProyects/day_10/laser.png")
bala_x = 0
bala_y = 536
bala_x_cambio = 0
bala_y_cambio = 1
bala_visible = False

# variable de puntaje
puntaje = 0
fuente = pygame.font.Font('freesansbold.ttf',32)
texto_x = 10
texto_y = 10

#texto final de juego
fuente_final = pygame.font.Font('freesansbold.ttf',60)


def texto_final():
    mi_funete_final = fuente_final.render("JUEGO TERMINADO",True, (255,255,255))
    pantalla.blit(mi_funete_final, (100,200))


# funcion para mostrar puntaje
def mostrar_puntaje(x, y):
    texto = fuente.render(f"Puntos: {puntaje}", True,(255,255,255))
    pantalla.blit(texto, (x,y))


#funcion jugador
def jugador(x, y):
    pantalla.blit(imagen_jugador, (x, y))

  
#funcion enemigo
def enemigo(x, y, ene):
    pantalla.blit(imagen_enemigo[ene], (x, y))


#funcion disparar bala
def disparar_bala(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(imagen_bala,(x +16, y +10))


# detectar coliciones
def hay_colision(x1,y1,x2,y2):
    distancia = math.sqrt(math.pow((x1 - x2),2) + math.pow((y1 - y2),2))
    
    if distancia < 27:
        return True
    else:
        return False


# loop del juego
se_ejecuta = True

while se_ejecuta:
    
    # fondo pantalla
    pantalla.blit(fondo, (0,0))
    
    # iterar eventos
    for evento in pygame.event.get():
        # evento cerrar
        if evento.type == pygame.QUIT:
            se_ejecuta = False
        
        # evento presionar teclas
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -0.5
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0.5
            if evento.key == pygame.K_SPACE:
                sonido_bala = mixer.Sound('/home/adan/Documentos/github - local/pythonProyects/day_10/disparo.mp3')
                sonido_bala.play()
                
                if not bala_visible:
                    bala_x = jugador_x
                    disparar_bala(bala_x, bala_y)
        
        # evento soltar felchas
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0
    
    # modificar la ubicacion del jugador
    jugador_x += jugador_x_cambio
    
    # mantener al jugador dentro de los bordes
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736
    
    # modificar la ubicacion del enemigo
    for e in range(cantidad_enemigos):
        
        #fin del juego
        if enemigo_y[e] > 500:
            for k in range(cantidad_enemigos):
                enemigo_y[k] = 1000
            texto_final()
            break
        
        enemigo_x[e] += enemigo_x_cambio[e]
    
        # mantener al enemigo dentro de los bordes
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 0.8
            enemigo_y[e] += enemigo_y_cambio[e]
        elif enemigo_x[e] >= 736:
            enemigo_x_cambio[e] = -0.8
            enemigo_y[e] += enemigo_y_cambio[e]
        
        # Comprobar colicion
        colision = hay_colision(enemigo_x[e], enemigo_y[e], bala_x, bala_y)
        if colision:
            sonido_colision = mixer.Sound('/home/adan/Documentos/github - local/pythonProyects/day_10/Golpe.mp3')
            sonido_colision.play()
            
            bala_y = 500
            bala_visible = False
            puntaje += 1
            enemigo_x[e] = random.randint(0,736)
            enemigo_y[e] = random.randint(50,200)
        
        enemigo(enemigo_x[e], enemigo_y[e], e)
    
    #movimiento de la bala
    if bala_y <= -64:
        bala_y = 500
        bala_visible = False
    
    if bala_visible:
        disparar_bala(bala_x    , bala_y)
        bala_y -= bala_y_cambio
    
    
    
    #crear entidades
    jugador(jugador_x, jugador_y)
    
    #mostrar puntaje
    mostrar_puntaje(texto_x, texto_y)
    
    #actualizar
    pygame.display.update()