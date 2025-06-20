import pygame, sys, random
from player import player
from tuberias import Tuberia


pygame.init()
pygame.mixer.init()

#Colores
BLACK =(0,    0,  0)
WHITE =(255,255,255)
RED =  (255,   0, 0)
GREEN = (0,   255, 0)
BLUE = (0,   0, 255)
#Venta
size = (800, 518)  #tupla

#Crear ventana
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Bird Jump")

#Inicializaciones 
imagen_tubo = pygame.image.load("img/tuberia.png").convert_alpha()
imagen_tubo = pygame.transform.scale(imagen_tubo, (80, 4000))

clock = pygame.time.Clock()
FPS = 60
fondo = pygame.image.load("img/fondo.jpg").convert()
posicion_fondo = 0

#Constantes de tuberias
grupo_tuberias = []
ESPACIO_TUBERIAS = 250
EVENTO_NUEVA_TUBERIA = pygame.USEREVENT
pygame.time.set_timer(EVENTO_NUEVA_TUBERIA, 1500)
fuente = pygame.font.SysFont(None, 60)

#Variables del jugador 
todos_los_sprites = pygame.sprite.Group()
jugador = player()
todos_los_sprites.add(jugador)
puntuacion = 0
#REINICIO DE JUEGO
def reiniciar_juego():
    global grupo_tuberias
    grupo_tuberias.clear()
    jugador.rect.center=(100,300)
    jugador.velocidad = 0
    

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == EVENTO_NUEVA_TUBERIA:
            nueva_tuberia = Tuberia(800, ESPACIO_TUBERIAS, imagen_tubo)
            grupo_tuberias.append(nueva_tuberia)

    posicion_fondo -=2
    if posicion_fondo <=-800:
        posicion_fondo = 0

    screen.blit(fondo, (posicion_fondo,0))
    screen.blit(fondo, (posicion_fondo +800,0))

    for tuberia in grupo_tuberias:
        tuberia.mover()
        tuberia.draw(screen)

    #Validacion de puntos (si el borde izq de la tueria ya paso al borde derecho del jugador)
    for tuberia in grupo_tuberias:
        if tuberia.tubo_arriba.right < jugador.rect.left and not tuberia.contador:
            puntuacion += 1
            tuberia.contador = True

    grupo_tuberias = [t for t in grupo_tuberias if not t.fuera_de_pantalla()]

    todos_los_sprites.update()
    ### ---- LOGICA

    ### ---- START ZONA DE DIBUJO
    todos_los_sprites.draw(screen)
    ### ---- END ZONA DE DIBUJO
    #Validacion de choque
    for tuberia in grupo_tuberias:
        if tuberia.tubo_arriba.colliderect(jugador.rect) or tuberia.tubo_abajo.colliderect(jugador.rect):
            reiniciar_juego()
            puntuacion = 0
    #Que el jugador no se salga
    if jugador.rect.top <= 0 or jugador.rect.bottom >=518:
        reiniciar_juego()
        puntuacion = 0

    if puntuacion ==5:
        FPS = 80
    if puntuacion ==10:
        FPS = 90
    texto = fuente.render(f"Puntuación: {puntuacion}", True, BLACK)
    screen.blit(texto, (20,20))
    #actualizar pantalla
    pygame.display.flip()
    clock.tick(FPS)