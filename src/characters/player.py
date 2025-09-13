import pygame
from settings import IMAGES
from .character import Character

class Player(Character):
    def __init__(self, x, y):
        super().__init__(IMAGES["player"], x, y, width=148, height=148, speed=5)

    def handle_input(self):
        keys = pygame.key.get_pressed()
        dx, dy = 0, 0

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            dy = -1
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            dy = 1
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            dx = -1
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            dx = 1

        if dx or dy:
            self.move(dx, dy)

    def update(self):
        self.handle_input()