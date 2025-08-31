import pygame
import sys
from scenes.menu import Menu
from settings import SCREEN_HEIGHT, SCREEN_WIDTH
def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Piratas")
    menu = Menu(screen)
    menu.run()
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()