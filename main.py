import pygame, sys
from pygame import *
from animation import *
from player_class import Player
# Name: DUNGEON EXPLORER
"""Story line: You are a dungeon explorer, find the way out before it's too late"""
'''Mechanics: Dashing, Attacking and Looting and Equipping'''
'''Map: 5 rooms per map'''

# Variables name
pygame.init()
window_size = (1280, 720)
display_size = (480, 360)
clock = pygame.time.Clock()
background = pygame.image.load('background_red.png')
image_okay = 0


player = Player(50, 100, 60, 100, 10)

screen = pygame.display.set_mode(window_size, pygame.FULLSCREEN, 32)
display = pygame.Surface(display_size)
map = [[0, 0, 0, 1, 0, 1, 0, 0],
       [0, 0, 0, 0, 1, 0, 0, 0],
       [1, 1, 1, 1, 0, 1, 1, 1]]

while True:
    display.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_LEFT:
                player.m_left, player.face_left, player.face_right = True, True, False
            if event.key == K_RIGHT:
                player.face_left, player.face_right, player.m_right = False, True, True

        if event.type == pygame.KEYUP:
            if event.key == K_LEFT:
                player.m_left, player.walk_left[3], player.walk_left[2] = False, 0, 0
            if event.key == K_RIGHT:
                player.m_right, player.walk_right[3], player.walk_right[2] = False, 0, 0
    player.rect = pygame.Rect(player.x, player.y, player.width, player.height)
    if not player.m_left and not player.m_right:
        if player.face_right:
            player.animate(display, player.stand_right)
        if player.face_left:
            player.animate(display, player.stand_left)
    else:
        if player.m_right and player.m_left:
            if player.face_left and not player.face_right:
                player.animate(display, player.stand_right)
            if player.face_right and not player.face_left:
                player.animate(display, player.stand_left)
        else:
            if player.m_right:
                player.animate(display, player.walk_right)
                player.x += 2
            if player.m_left:
                player.animate(display, player.walk_left)
                player.x -= 2

    screen.blit(pygame.transform.scale(display, window_size), (0, 0))
    pygame.display.update()
    clock.tick(60)
