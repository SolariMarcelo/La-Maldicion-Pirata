import pygame
import sys
from scenes.menu import Menu
from settings import SCREEN_HEIGHT, SCREEN_WIDTH, IMAGES
def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("La maldición pirata")

    icon = pygame.image.load(IMAGES["icon"]) 
    pygame.display.set_icon(icon)

    menu = Menu(screen)
    menu.run()
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()