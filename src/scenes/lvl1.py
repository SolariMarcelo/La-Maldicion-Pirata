# lvl1.py
import random
import time
import pygame
import sys
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, IMAGES_LVL1, SOUNDS_LVL1, LVL1_GROUND_Y, WHITE, FONTS
from .scene import Scene
from characters.player import Player
from characters.crab import Crab 

class Level1(Scene):
    def __init__(self, screen):
        super().__init__(screen)
        self.clock = pygame.time.Clock()
        self.background = pygame.image.load(IMAGES_LVL1["level1_bg"]).convert()
        self.background = pygame.transform.scale(self.background, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.mouse_visible = False
        self.init_audio()

        self.all_sprites = pygame.sprite.Group()
        self.all_crabs = pygame.sprite.Group()

        self.player = Player(SCREEN_WIDTH/2 - 140, LVL1_GROUND_Y, LVL1_GROUND_Y)
        self.all_sprites.add(self.player)

        self.time_trascurrido = pygame.time.get_ticks()

        self.create_npc()


    def create_npc(self):
        self.spawn_positions = [random.randint(0, SCREEN_WIDTH - 100) for _ in range(10)]
        self.spawn_interval = random.randint(200, 300) # tiempo de reaparicion 
        self.last_spawn = pygame.time.get_ticks()  # tiempo en que aparecio el ultimo
        self.spawn_index = 0  
            
    def handle_events(self):
        for event in pygame.event.get():
            self.handle_global_events(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update(self, dt):
        self.all_sprites.update(dt)
        self.all_crabs.update(dt)

        # Generacion de cangrejos
        now = pygame.time.get_ticks()
        if self.spawn_index < len(self.spawn_positions) and now - self.last_spawn >= self.spawn_interval:
            x = self.spawn_positions[self.spawn_index]  
            crab = Crab(x, LVL1_GROUND_Y)             
            self.all_crabs.add(crab)                    
            self.all_sprites.add(crab)                
            self.spawn_index += 1                       
            self.last_spawn = now                        # actualizamos el tiempo del último spawn
            self.spawn_interval = random.randint(500, 1500)  # el próximo sale en un tiempo aleatorio entre 0,5 y 2 seg

        # Colisiones
        hits = pygame.sprite.spritecollide(self.player, self.all_crabs, False)
        if hits:
            print("¡El jugador chocó con un cangrejo!")  
            
        time_init = (pygame.time.get_ticks() - self.time_trascurrido) // 1000
        minutes, seconds = divmod(time_init, 60)
        time_text = f"{minutes:02d}:{seconds:02d}"

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
