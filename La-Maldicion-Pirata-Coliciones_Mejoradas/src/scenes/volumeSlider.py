import pygame
from .scene import Scene
from settings import FPS
import sys
class Volume(Scene):
    def __init__(self, screen):
        super().__init__(screen)
        self.screen = screen
        self.sliderX = 500
        self.sliderY = 500
        self.clock = pygame.time.Clock()
        self.sliderWidth = 200
        self.sliderHeight = 10
        self.knobRadius = 10
        self.volume = pygame.mixer.music.get_volume()
        self.actualVolume = self.sliderX + int(self.volume * self.sliderWidth)
        self.dragState = False

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = event.pos
                if (self.actualVolume - self.knobRadius <= mx <= self.actualVolume + self.knobRadius and self.sliderY - 10 <= my <= self.sliderY + 10):
                    self.dragState = True
            elif event.type == pygame.MOUSEBUTTONUP:
                self.dragState = False
                return True
            elif event.type == pygame.MOUSEMOTION and self.dragState:
                mx, _ = event.pos
                self.actualVolume = max(self.sliderX, min(mx, self.sliderX + self.sliderWidth))
                self.volume = (self.actualVolume - self.sliderX) / self.sliderWidth 
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return True
                if event.key == pygame.K_RIGHT:
                    self.volume = self.volume + 0.1
                    pygame.mixer.music.set_volume(self.volume)
                    self.actualVolume = self.sliderX + int(self.volume * self.sliderWidth)
                    print(self.volume)
                if event.key == pygame.K_LEFT:
                    self.volume = self.volume - 0.1
                    pygame.mixer.music.set_volume(self.volume)
                    self.actualVolume = self.sliderX + int(self.volume * self.sliderWidth)
                    print(self.volume)

    def handleVolume(self):
        if self.volume >= 1.0:
            self.volume = 1
        elif self.volume <= 0:
            self.volume = 0.0
    def draw(self):
        self.screen.fill((250, 250, 250))
        pygame.draw.rect(self.screen, (250, 0, 0),
        (self.sliderX, self.sliderY - self.sliderHeight // 2, self.sliderWidth - self.sliderHeight, self.sliderHeight))
        pygame.draw.rect(self.screen, (0, 0, 250), 
        (self.sliderX, self.sliderY - self.sliderHeight // 2, self.actualVolume - self.sliderX, self.sliderHeight))
        pygame.draw.rect(self.screen, (220, 220, 220), 
        (self.actualVolume, self.sliderY, self.knobRadius, self.sliderHeight))
        
    def run(self):
        running = True
        while running:
            pressedKey = self.handleEvents()
            print(self.volume)
            self.draw()
            self.handleVolume()
            pygame.display.update((500, 500, self.sliderWidth, self.sliderHeight))
            self.clock.tick(FPS)
            if pressedKey:
                running = False
