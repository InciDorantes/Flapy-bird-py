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

cor_list=[]
for i in range(60):
        x = random.randint(0,800)
        y = random.randint(0,500)
        cor_list.append([x,y])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    ### ---- LOGICA
    screen.fill(WHITE)
    ### ---- START ZONA DE DIBUJO
    # pygame.draw.rect(screen, RED, (cord_x, cord_y, 80,80))
    for j in cor_list:
        x = j[0]
        y = j[1]
        pygame.draw.circle(screen, BLUE, (x,y), 2)
        j[1] +=1
        if j[1] > 500:
             j[1] = 0

    ### ---- END ZONA DE DIBUJO

    #actualizar pantalla
    pygame.display.flip()
    clock.tick(80)