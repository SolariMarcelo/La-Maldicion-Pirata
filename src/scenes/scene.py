import pygame
import sys
from settings import FONTS, MENU_FONT_SIZE

# Padre de todas las pantallas, menu, nivel, pausa, etc
class Scene:
    def __init__(self, screen):
        self.screen = screen
        self.font = self.load_font()

    def load_font(self):
        try:
            return pygame.font.Font(FONTS["main_font"], MENU_FONT_SIZE)
        except FileNotFoundError:
            try:
                return pygame.font.SysFont("Arial", MENU_FONT_SIZE)
            except:
                return pygame.font.Font(None, MENU_FONT_SIZE)

    def handle_global_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F11:
                pygame.display.toggle_fullscreen()
            elif event.key == pygame.K_RETURN and (pygame.key.get_mods() & pygame.KMOD_ALT):
                pygame.display.toggle_fullscreen()

# pygame.key.get_mods() devuelve un número entero que representa todas las teclas modificadoras que están presionadas en ese momento.
# Las teclas modificadoras incluyen: Shift, Ctrl, Alt, Meta, etc.
# El operador & es un AND a nivel de bits. Compara el valor de get_mods() con la constante pygame.KMOD_ALT (que representa la tecla Alt).
# Si el resultado es distinto de cero, significa que Alt está siendo presionado.