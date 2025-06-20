import pygame

class player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.imagen_original = pygame.image.load("img/bird.png").convert_alpha()
        self.image =pygame.transform.scale(self.imagen_original, (60,60))
        self.rect = self.image.get_rect()
        self.rect.center = (200,300)

        self.velocidad = 0
        self.gravedad = 0.1
        self.salto = - 4
    
    def update(self):
        self.velocidad += self.gravedad
        self.rect.y += self.velocidad

        teclas = pygame.key.get_pressed()
        if teclas [pygame.K_SPACE]:
            self.velocidad = self.salto
