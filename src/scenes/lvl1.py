import pygame
import sys
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, IMAGES_LVL1
from .scene import Scene
from characters.player import Player

class Level1(Scene):
    def __init__(self, screen):
        super().__init__(screen)
        self.clock = pygame.time.Clock()
        self.background = pygame.image.load(IMAGES_LVL1["level1_bg"]).convert()
        self.background = pygame.transform.scale(self.background, (SCREEN_WIDTH, SCREEN_HEIGHT))

        # Grupo de sprites
        self.all_sprites = pygame.sprite.Group()
        self.player = Player(100, 100)
        self.all_sprites.add(self.player)

        # Falta descargar el audio
        #self.init_audio()

    def handle_events(self):
        for event in pygame.event.get():
            self.handle_global_events(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def init_audio(self):
        if not pygame.mixer.get_init():
            pygame.mixer.init()
        pygame.mixer.music.set_volume(0.3)
        # Agregarlo a settings
        pygame.mixer.music.load("assets/sounds/level1_music.mp3")
        pygame.mixer.music.play(-1)

    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.all_sprites.draw(self.screen)   
        self.draw_cursor()

    def run(self):
        running = True
        while running:
            self.handle_events()
            self.draw()
            self.update()  
            pygame.display.flip()
            self.clock.tick(FPS)