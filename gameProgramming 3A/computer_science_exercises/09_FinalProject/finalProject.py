# Arial Combat Sim, Gavin Kloeckner, v0.1.1

import pygame
from sys import exit
from random import randint   

pygame.init()
screen = pygame.display.set_mode((1000,900))
pygame.display.set_caption('Arial Combat Sim')
clock = pygame.time.Clock()
screen.fill('Light Blue')
test_font = pygame.font.Font(None, 87)
test_font2 = pygame.font.Font(None, 67)
test_font3 = pygame.font.Font(None, 47)

gameName = test_font.render('Arial Combat Sim', False, 'Dark Gray')
gameName_rect = gameName.get_rect(center = (490, 130))
gameMessage = test_font2.render('Press the UP arrow to run the game', False, 'Dark Gray')
gameMessage_rect = gameMessage.get_rect(center = (490, 270))
gameMessage2 = test_font3.render('A Game by Gavin Kloeckner', False, 'Dark Green')
gameMessage2_rect = gameMessage2.get_rect(center =(490, 210))

gameActive = True


mig_surface = pygame.image.load('img/MiG21.png')
mig_y_pos = 300


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()



    screen.blit(mig_surface,(mig_y_pos, 30))
    # mig_y_pos -= 
    screen.blit(gameName, gameName_rect)
    screen.blit(gameMessage, gameMessage_rect)
    screen.blit(gameMessage2, gameMessage2_rect)

    pygame.display.update()
    clock.tick(90)


    






