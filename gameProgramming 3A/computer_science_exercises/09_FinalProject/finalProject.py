# Ariel Combat Sim, Gavin Kloeckner, v0.0

import pygame
from sys import exit
from random import randint   

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)
gameActive = False
startTime = 0
sky = 0


if sky == 0:
    sky_surf = pygame.image.load
else:
    sky_surf = pygame.image.load
