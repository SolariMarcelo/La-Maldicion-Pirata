import pygame
import sys
from settings import IMAGES, SOUNDS, BLUE, WHITE, RED, FPS, SCREEN_HEIGHT, SCREEN_WIDTH,MENU_MARGIN
#.scene porque esta dentro del mismo paquete
from .scene import Scene

class Menu(Scene):
    def __init__(self, screen):
        super().__init__(screen) 
        self.screen = screen
        self.clock = pygame.time.Clock() # Velocidad de actualización (FPS).
        self.options = ["Iniciar Partida","Opciones", "Salir"]  # Opciones
        self.selected_index = 0 # Opcion seleccionada
        self.background = pygame.image.load(IMAGES["menu_bg"]).convert_alpha()
        self.background = pygame.transform.scale(self.background, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.init_audio()

    # dibujar menu
     # dibujar menu con sombra
     # dibujar menu con caja semitransparente
    # dibujar menu
    def draw(self):
        self.screen.blit(self.background, (0, 0))
        option_height = self.font.get_height()  # altura del texto
        total_height = len(self.options) * option_height + (len(self.options) - 1) * MENU_MARGIN
        start_y = (SCREEN_HEIGHT - total_height) // 2 + 200

        for index, option in enumerate(self.options):
            color = BLUE if index == self.selected_index else RED
            self.draw_text_with_outline(
                option,
                self.font,
                color,
                (0, 0, 0),  # contorno negro
                SCREEN_WIDTH // 2,
                start_y + index * (option_height + MENU_MARGIN)
            )

    # función auxiliar para texto con contorno
    def draw_text_with_outline(self, text, font, text_color, outline_color, x, y):
        base = font.render(text, True, text_color)
        outline = font.render(text, True, outline_color)
        rect = base.get_rect(center=(x, y))
        # Dibuja contorno alrededor
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1), (1,1), (-1,-1), (1,-1), (-1,1)]:
            self.screen.blit(outline, rect.move(dx, dy))
        # Texto principal encima
        self.screen.blit(base, rect)

    def init_audio(self):
        # Solo inicializa si no se hizo ya
        if not pygame.mixer.get_init():
            pygame.mixer.init()
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.load(SOUNDS["menu_music"])
        pygame.mixer.music.play(-1)
        self.move_sound = pygame.mixer.Sound(SOUNDS["menu_move"])
        self.move_enter = pygame.mixer.Sound(SOUNDS["menu_enter"])
        self.move_salir = pygame.mixer.Sound(SOUNDS["menu_salir"])
    
    # Eventos de teclas
    def handle_events(self):
        for event in pygame.event.get():
            self.handle_global_events(event) 
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.selected_index = (self.selected_index - 1) % len(self.options)
                    self.move_sound.play()
                elif event.key == pygame.K_DOWN:
                    self.selected_index = (self.selected_index + 1) % len(self.options)
                    self.move_sound.play()
                elif event.key == pygame.K_RETURN:
                    self.select_option()

    def select_option(self):
        match self.selected_index:
            case 0:
                print("Iniciar partida")
                self.move_enter.play()
            case 1:
                pass
            case 2:
                self.move_salir.play()
                # Esperar a que termine el sonido
                while pygame.mixer.get_busy():
                    pygame.time.delay(50)  # pequeña pausa para no sobrecargar el CPU
                pygame.quit()
                sys.exit()

    def run(self):
        running = True
        while running:
            self.handle_events()  # manejar eventos de teclas
            self.draw() # Dibuja
            pygame.display.flip() # Actualiza 
            self.clock.tick(FPS) # velocidad del bucle 60 FPS (frames por segundo).