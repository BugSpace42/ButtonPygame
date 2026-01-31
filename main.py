import pygame

pygame.init()
screen_width = 600
screen = pygame.display.set_mode((screen_width, screen_width))
pygame.display.set_caption("Счётчик")

counter = 0
MIN_VALUE = 0
MAX_VALUE = 10

font = pygame.font.Font(None, 48)
label_font = pygame.font.Font(None, 36)

# Кнопка + 1
plus_button = pygame.Rect(screen_width//8, screen_width*3//4, screen_width//4, screen_width//8)
# Кнопка - 1
minus_button = pygame.Rect(screen_width*5//8, screen_width*3//4, screen_width//4, screen_width//8)

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    plus_color = (0, 200, 0)
    pygame.draw.rect(screen, plus_color, plus_button)
    pygame.draw.rect(screen, (0, 0, 0), plus_button, 2)  # Обводка

    minus_color = (200, 0, 0)
    pygame.draw.rect(screen, minus_color, minus_button)
    pygame.draw.rect(screen, (0, 0, 0), minus_button, 2)  # Обводка

    pygame.display.flip()

pygame.quit()