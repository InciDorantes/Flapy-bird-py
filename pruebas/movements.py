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

clock = pygame.time.Clock()
#pygame.mouse.set_visible(0)

#Variables
x = 10
y = 10
speed_x = 0
speed_y = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        ##evento del teclado
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed_x = -3
            if event.key == pygame.K_RIGHT:
                speed_x = 3
            if event.key == pygame.K_DOWN:
                speed_y = 3
            if event.key == pygame.K_UP:
                speed_y = -3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                speed_x = 0
            if event.key == pygame.K_RIGHT:
                speed_x = 0
            if event.key == pygame.K_DOWN:
                speed_y = 0
            if event.key == pygame.K_UP:
                speed_y = 0

    ### ---- LOGICA
    # mouse_pos = pygame.mouse.get_pos()
    # x = mouse_pos[0]
    # y = mouse_pos[1]
    screen.fill(WHITE)
    x += speed_x
    y += speed_y
    
    if (x > 720 or x <0):
        x*=-1 
    if (y > 380 or y < 0):
        y*=-1 
    ### ---- START ZONA DE DIBUJO
    pygame.draw.rect(screen, RED, (x,y,100,100))
    ### ---- END ZONA DE DIBUJO

    #actualizar pantalla
    pygame.display.flip()
    clock.tick(60)