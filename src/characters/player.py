# player.py
import pygame
from settings import IMAGES
from .character import Character

class Player(Character):
    def __init__(self, x, y, ground):
        super().__init__(IMAGES["player"], x, y, width=100, height=100, speed=350)
        self.vel_y = 0
        self.gravity = 3000
        self.jump_strength = -900
        self.on_ground = False
        self.ground_y = ground
       
    def handle_input(self, dt):
        keys = pygame.key.get_pressed()
        dx = 0
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            dx = -1
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            dx = 1
        self.move(dx, 0, dt)
        if (keys[pygame.K_w] or keys[pygame.K_UP]) and self.on_ground:
            self.vel_y = self.jump_strength
            self.on_ground = False
    
    def apply_gravity(self, dt):
        self.vel_y += self.gravity * dt
        self.rect.y += self.vel_y * dt
        if self.rect.bottom >= self.ground_y:
            self.rect.bottom = self.ground_y
            self.vel_y = 0
            self.on_ground = True

    def update(self, dt):
        self.handle_input(dt)
        self.clamp_to_screen()
        self.apply_gravity(dt)
