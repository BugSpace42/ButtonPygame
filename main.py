import pygame

pygame.init()
screen_width = 600
screen = pygame.display.set_mode((screen_width, screen_width))
pygame.display.set_caption("Счётчик")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()