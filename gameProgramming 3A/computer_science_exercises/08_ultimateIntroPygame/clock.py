# Displaying Images on a Surface, Gavin Kloeckner, v0.0.1

import pygame

pygame.init
screen = pygame.display.set_mode((890,410))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    # draw all of our elements
    # update everything
    pygame.display.update()
