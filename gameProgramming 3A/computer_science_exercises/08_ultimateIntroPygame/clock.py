# Displaying Images on a Surface, Gavin Kloeckner, v0.1.6

import pygame
from sys import exit
from random import randint

def displayScore():
    currentTime = int(pygame.time.get_ticks() / 1000) - startTime
    scoreSurf = test_font.render(f'Score: {currentTime}', False, 'Dark Green')
    scoreRect = scoreSurf.get_rect(center = (400, 50))
    screen.blit(scoreSurf, scoreRect)
    return currentTime

def obstacleMovement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            screen.blit(alligator_surf, obstacle_rect)

            obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

        return obstacle_list
    else: return []

def collisions(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect): return False
    return True
    

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)
gameActive = False
startTime = 0
score = 0


ground_surf = pygame.image.load('graphics/red_stone.jpg').convert()
sky_surf = pygame.image.load('graphics/blue_sky.jpg').convert()

# .convert() will modify an image file to make it easier to work with in Pygame

# score_surf = test_font.render('My Game', True, 'Dark Green')
# score_rect = score_surf.get_rect(center = (400, 50))

alligator_surf = pygame.image.load('graphics/Alligator.png').convert_alpha()
alligator_rect = alligator_surf.get_rect(bottomright = (600, 300))
alligator_x_pos = 800

obstacle_rect_list = []

player_surf = pygame.image.load('graphics/steve_walk.png').convert_alpha()
player_x_pos = 200
player_rect = player_surf.get_rect(midbottom = (50,300))
player_gravity = 0
playerStand = pygame.image.load('graphics/steve_stand.png').convert_alpha()
playerStandScaled = pygame.transform.rotozoom(playerStand, 0,3)
playerStand_rect = playerStand.get_rect(center = (400, 160))

gameName = test_font.render('Pixel Runner', True, 'Lime')
gameName_rect = gameName.get_rect(center = (410, 120))
gameMessage = test_font.render('Press space to run the game', True, 'Lime')
gameMessage_rect = gameMessage.get_rect(center = (400, 270))

obstacleTimer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacleTimer, 1800)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if gameActive:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                    player_gravity = -10.6
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -10.6
            
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                gameActive = True
                alligator_rect.left = 800
                startTime = int(pygame.time.get_ticks() / 1000)
        
        if event.type == obstacleTimer and gameActive:
            obstacle_rect_list.append(alligator_surf.get_rect(bottomright = (randint(900, 1100), 300)))


    if gameActive:
        screen.blit(sky_surf, (0, 0))
        screen.blit(ground_surf, (0, 300))
        # pygame.draw.rect(screen, 'Green', score_rect, 17, 15)
        # screen.blit(score_surf, score_rect)
        score = displayScore()

        # alligator_rect.x -= 3 
        # screen.blit(alligator_surf, alligator_rect)

        player_gravity += 0.3
        player_rect.y += player_gravity
        if player_rect.bottom >= 300: player_rect.bottom = 300
        screen.blit(player_surf, player_rect)

        obstacle_rect_list = obstacleMovement(obstacle_rect_list)

        gameActive = collisions(player_rect, obstacle_rect_list)

        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_SPACE]:
        #     print('jump ')

        # if player_rect.colliderect(alligator_rect):
        #     print('Collision Detected!')
    
        # mouse_pos = pygame.mouse.get_pos()
        # if player_rect.collidepoint((mouse_pos)):
        #     print(pygame.mouse.get_pressed())


    else:
        screen.fill('Cyan')
        screen.blit(playerStandScaled, playerStand_rect)
        obstacle_rect_list.clear()

        scoreMessage = test_font.render(f'Your score is: {score}', True, 'Lime')
        scoreMessage_rect = scoreMessage.get_rect(center = (400, 330))
        screen.blit(gameName, gameName_rect)

    if score == 0: screen.blit(gameMessage, gameMessage_rect)
    else: screen.blit(scoreMessage, scoreMessage_rect)


    pygame.display.update()
    clock.tick(70)
