import pygame
from settings import IMAGES, LVL1_GROUND_Y
from .character import Character

class Player(Character):
    def __init__(self, x, y,ground):
        super().__init__(IMAGES["player"], x, y, width=150, height=150, speed=5)
        self.vel_y = 0
        self.gravity = 1     
        self.jump_strength = -15  # impulso del salto (negativo porque sube)
        self.on_ground = False
        self.ground_y = ground
       
    def handle_input(self):
        keys = pygame.key.get_pressed()
        dx = 0

        # if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        #     dx = -1
        # if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        #     dx = 1
        
        if (keys[pygame.K_w] or keys[pygame.K_UP]) and self.on_ground:
            self.vel_y = self.jump_strength
            self.on_ground = False

        if dx:
            self.move(dx,0)
    
    def apply_gravity(self):
        """Aplica gravedad y limita el suelo"""
        self.vel_y += self.gravity
        self.rect.y += self.vel_y

        # Colisión con el suelo
        if self.rect.bottom >= self.ground_y:
            self.rect.bottom = self.ground_y
            self.vel_y = 0
            self.on_ground = True

    def update(self):
        self.handle_input()
        self.clamp_to_screen()
        self.apply_gravity()

