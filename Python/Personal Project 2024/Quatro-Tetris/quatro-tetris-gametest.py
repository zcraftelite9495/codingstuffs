import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Quatro Tetris")

class Button:
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text

    def draw(self):
        pygame.draw.rect(screen, (0, 255, 255), self.rect)
        font = pygame.font.Font(None, 40)
        text = font.render(self.text, True, (255, 0, 255))
        text_rect = text.get_rect(center=self.rect.center)
        screen.blit(text, text_rect)

start_button = Button(250, 250, 300, 100, "Start")
exit_button = Button(250, 400, 300, 100, "Exit")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if start_button.rect.collidepoint(event.pos):
                # Start button action
                # Insert your code to start the game here
                pass
            elif exit_button.rect.collidepoint(event.pos):
                pygame.quit()
                sys.exit()

    screen.fill((0, 0, 0))

    # Draw the logo
    font = pygame.font.Font(None, 100)
    logo_line1 = font.render("Quatro", True, (255, 255, 255))
    logo_line2 = font.render("Tetris", True, (255, 255, 255))
    logo_rect1 = logo_line1.get_rect(center=(screen.get_width() // 2, 100))
    logo_rect2 = logo_line2.get_rect(center=(screen.get_width() // 2, 200))
    screen.blit(logo_line1, logo_rect1)
    screen.blit(logo_line2, logo_rect2)

    # Draw the buttons
    start_button.draw()
    exit_button.draw()

    pygame.display.flip()

