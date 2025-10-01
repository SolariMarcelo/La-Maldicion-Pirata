# lvl1.py
import random
import time
import pygame
import sys
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, IMAGES_LVL1, SOUNDS_LVL1, LVL1_GROUND_Y, WHITE, FONTS
from .scene import Scene
from characters.player import Player
from characters.enemy import Crab 
class Level1(Scene):
    def __init__(self, screen):
        super().__init__(screen)
        self.clock = pygame.time.Clock()
        self.background = pygame.image.load(IMAGES_LVL1["level1_bg"]).convert()
        self.background = pygame.transform.scale(self.background, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.mouse_visible = False
        self.init_audio()
        self.all_sprites = pygame.sprite.Group()
        self.player = Player(SCREEN_WIDTH/2 - 140, 0, LVL1_GROUND_Y)
        self.all_sprites.add(self.player)
        self.time_trascurrido = pygame.time.get_ticks()
        self.all_crabs = pygame.sprite.Group()
        for _ in range(10):
            randomPos = random.randint(0, SCREEN_WIDTH - 100)  # Generar 10 NPCs
            crab = Crab(randomPos, LVL1_GROUND_Y)
            self.all_crabs.add(crab)
            
    def handle_events(self):
        for event in pygame.event.get():
            self.handle_global_events(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update(self, dt):
        self.all_sprites.update(dt)
        self.all_crabs.update(dt)
        time_init = (pygame.time.get_ticks() - self.time_trascurrido) / 1000
        time_text = f"{time_init:.0f}"

        self.text_font = self.load_font(size=40)
        self.time_surface = self.text_font.render(time_text, True, WHITE)
        time_rect = self.time_surface.get_rect(center=(SCREEN_WIDTH - 100, SCREEN_HEIGHT - 20))
        self.screen.blit(self.time_surface, time_rect)

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.all_sprites.draw(self.screen)
        self.draw_cursor()
        self.all_crabs.draw(self.screen)

    def init_audio(self):
        if not pygame.mixer.get_init():
            pygame.mixer.init()
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.load(SOUNDS_LVL1["level1_sound"])
        pygame.mixer.music.play(-1)

    def run(self):
        running = True
        while running:
            dt = self.clock.tick(FPS) / 1000
            self.draw()
            self.handle_events()
            self.update(dt)
            pygame.display.flip()
