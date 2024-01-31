# Displaying Images on a Surface, Gavin Kloeckner, v0.0.2

import pygame

pygame.init
screen = pygame.display.set_mode((890,410))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()

test_surface = pygame.Surface((840, 100))
test_surface.fill('Red')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(test_surface, (0, 300))

    pygame.display.update()
    clock.tick(60)
