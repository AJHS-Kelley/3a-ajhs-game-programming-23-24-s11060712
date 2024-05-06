# Arial Combat Sim, Gavin Kloeckner, v0.1.3b

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

sky_surface = pygame.image.load('img/bluesky.png')

gameActive = True


f35b_surface = pygame.image.load('img/F35B.png')
f35b_x = 440
f35b_speed = 3
part_one = True
# x_direction = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if part_one:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and f35b_x > 1:
                f35b_x += -1
            elif event.key == pygame.K_RIGHT and f35b_x > 90:
                f35b_x += 1
        # if event.type == pygame.KEYUP:
        #     if event.key == pygame.K_LEFT:
        #         f35b_x = 0
        #     if event.key == pygame.K_RIGHT:
        #         f35b_x = 0

    # if part_one:
    #     f35b_x += f35b_speed  * x_direction



    screen.blit(sky_surface, (0,0))
    screen.blit(f35b_surface,(f35b_x, 390))
    screen.blit(gameName, gameName_rect)
    screen.blit(gameMessage, gameMessage_rect)
    screen.blit(gameMessage2, gameMessage2_rect)

    pygame.key.get_pressed()

    pygame.display.update()
    clock.tick(90)


    






