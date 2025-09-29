import pygame
from settings import IMAGES, LVL1_GROUND_Y, FPS
from .character import Character

class Player(Character):
    def __init__(self, x, y,ground,dt):
        super().__init__(IMAGES["player"], x, y, width=100, height=100, speed=5)
        self.vel_y = 0
        self.gravity = 1     
        self.jump_strength = -15  # impulso del salto (negativo porque sube)
        self.on_ground = False
        self.ground_y = ground
        self.posX = 50.0
        self.speed = 25.0
       
    def handle_input(self,dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            print(dt)
            print(self.posX)
    
            self.posX = -(self.speed * dt)
            print(dt)
            print(self.posX)
    
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            print(dt)
            print(self.posX)
    
            self.posX = (self.speed * dt)
            print(dt)
            print(self.posX)
        
        if (keys[pygame.K_w] or keys[pygame.K_UP]) and self.on_ground:
            self.vel_y = self.jump_strength
            self.on_ground = False

        if self.posX:
            self.move(self.posX,0)
    
    def apply_gravity(self):
        """Aplica gravedad y limita el suelo"""
        self.vel_y += self.gravity
        self.rect.y += self.vel_y

        # Colisión con el suelo
        if self.rect.bottom >= self.ground_y:
            self.rect.bottom = self.ground_y
            self.vel_y = 0
            self.on_ground = True

    def update(self,dt):
        self.handle_input(dt)
        self.clamp_to_screen()
        self.apply_gravity()

