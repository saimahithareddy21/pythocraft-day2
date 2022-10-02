import pygame
import random

pygame.init()
chick_positions = [(680, 50), (720, 100), (670, 150), (720, 200)]
screen = pygame.display.set_mode((800, 700))
# icon and caption
pygame.display.set_caption('poulterer')
icon = pygame.image.load('001-chicken.png')
pygame.display.set_icon(icon)

# chick
chicks = [pygame.image.load('001-chickenimg.png')] * 4
chickX = 900
chickY = 100
# player
playerImg = pygame.image.load('001-man.png')
playerX = 370
playerY = 520
playerX_change = 0
# enemy
enemyImg = pygame.image.load('001-fox.png')
enemyX = random.randint(30, 600)
enemyYpos = [50, 100, 150, 200]
enemyY = random.choice(enemyYpos)
enemyX_change = 0.3
enemyY_change = 0.5
# ballon throwing
ballonImg = pygame.image.load('001-water-balloons.png')
ballon_state = 'ready'
ballonX = playerX
ballonY = playerY - 16
ballonX_change = 0
ballonY_change = 0.5
ballon_state = 'ready'


def player(x, y):
    screen.blit(playerImg, (x, y))


def throw_balloons(x, y):
    global ballon_state
    ballon_state = 'fire'
    screen.blit(ballonImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


running = True
while running:
    screen.fill((153, 255, 153))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -1
            if event.key == pygame.K_RIGHT:
                playerX_change = 1
            if event.key == pygame.K_SPACE:
                ballonX = playerX
                throw_balloons(ballonX, ballonY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change
    if playerX >= 686:
        playerX = 686
    if playerX <= -20:
        playerX = -20
    i = 0
    for chick in chicks:
        # there are many chicks , here I have taken if you have only 4 chicks
        screen.blit(chick, (chick_positions[i]))
        i += 1
    if ballonY <= 0:
        ballon_state = 'ready'
        ballonY = playerY - 16
    if ballon_state == 'fire':
        ballonY -= ballonY_change
        throw_balloons(ballonX + 78, ballonY)
    enemyX += enemyX_change
    enemy(enemyX, enemyY)
    if enemyX >= 620:
        # every time fox goes near chick it eats that and it goes away ,so chicks decreses
        # there are many foxes to come but as of now I have created only one fox and after it goes away another fox comes
        if len(chicks) > 1:
            # game is over if foxes eats all the chicks
            chicks.remove(chicks[enemyYpos.index(enemyY)])
            chick_positions.remove(chick_positions[enemyYpos.index(enemyY)])
            enemyYpos.remove(enemyY)

        else:

            running = False
        enemyX = 20
        enemyY = random.choice(enemyYpos)

    player(playerX, playerY)
    pygame.display.update()
