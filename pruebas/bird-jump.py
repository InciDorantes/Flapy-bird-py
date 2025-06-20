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

#Variables
tubos = [{'x': 400, 'alto': random.randint(150, 400)}]
x = 20
y = 380
speed_x = 3
speed_y = 0
salto_fuerza = -15
gravedad = 1
suelo = 380
#Funciones de dibujo
def pajaro (x,y):
    pygame.draw.circle(screen, GREEN, (x,y), 20)
def dibujar_tubos(tubos):
    for tubo in tubos:
        pygame.draw.rect(screen, GREEN, (tubo['x'], 0, 60, tubo['alto']))
        pygame.draw.rect(screen, GREEN, (tubo['x'], tubo['alto'] + 150, 60, 600))

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        ##evento del teclado
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if y >= suelo:
                    speed_y= salto_fuerza 

    speed_y += gravedad  # gravedad
    y += speed_y
    #limitamos al suelo
    ### ---- LOGICA
    if y >=suelo:
        y = suelo
        speed_y = 0

    if (x > 720 or x <0):
        speed_x*=-1 

    x += speed_x 
    screen.fill(WHITE)
    ### ---- START ZONA DE DIBUJO
    pajaro (x,y)
    dibujar_tubos(tubos)
    ### ---- END ZONA DE DIBUJO

    #actualizar pantalla
    pygame.display.flip()
    clock.tick(60)