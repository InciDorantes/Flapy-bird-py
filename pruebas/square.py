import pygame, sys, random
pygame.init()

#Colores
BLACK =(0,    0,  0)
WHITE =(255,255,255)
RED =  (255,   0, 0)
GREEN = (0,   255, 0)
BLUE = (0,   0, 255)
#Venta
size = (800, 500)  #tupla

#Crear ventana
screen = pygame.display.set_mode(size)

#Variables
clock = pygame.time.Clock()
cord_x = 400
cord_y = 200
speed_x = 3
speed_y = 3


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    ### ---- LOGICA
    if (cord_x > 720 or cord_x <0):
        speed_x*=-1 
    if (cord_y > 380 or cord_y < 0):
        speed_y*=-1 

    #Movimiento
    cord_x += speed_x 
    cord_y += speed_y 
    screen.fill(WHITE)
    ### ---- START ZONA DE DIBUJO
    pygame.draw.rect(screen, GREEN, (cord_x, cord_y, 80,80))
    ### ---- END ZONA DE DIBUJO

    #actualizar pantalla
    pygame.display.flip()
    clock.tick(60)