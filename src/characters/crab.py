import pygame
import random
from settings import IMAGES_LVL1 as ENEMIES


class Crab(pygame.sprite.Sprite):
    def __init__(self, x, ground):
        super().__init__()
        self.image = pygame.image.load(ENEMIES["enemy_crab"]).convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect(topleft=(x, -200))
        self.vel_y = 0
        self.gravity = 90
        self.on_ground = False
        self.ground_y = ground

    def apply_gravity(self, dt):
        self.vel_y += self.gravity * dt
        self.rect.y += self.vel_y * dt
        if self.rect.bottom >= self.ground_y:
            self.rect.bottom = self.ground_y
            self.vel_y = 0
            self.on_ground = True

    def update(self, dt):
        self.apply_gravity(dt)

   

    