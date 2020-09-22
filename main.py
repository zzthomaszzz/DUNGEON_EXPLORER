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


def do_animation_1(surface, animation, coordinate_and_size, tick_count, tick, restart):
    global image_okay
    if tick_count == tick:
        image_okay += 1
        tick_count = 0
    if image_okay == len(animation) or restart:
        image_okay = 0
    surface.blit(animation[image_okay], coordinate_and_size)
    tick_count += 1
    return tick_count


player = Player(50, 100, 20, 20, 10)

screen = pygame.display.set_mode(window_size, pygame.FULLSCREEN, 32)
display = pygame.Surface(display_size)
map = [[0, 0, 0, 1, 0, 1, 0, 0],
       [0, 0, 0, 0, 1, 0, 0, 0],
       [1, 1, 1, 1, 0, 1, 1, 1]]

while True:
    display.blit(background, (0, 0))
    y = 0
    for tile in map:
        x = 0
        for number in tile:
            if number == 1:
                pygame.draw.rect(display, (255, 255, 0), (x * 20, y * 20, 20, 20))
            x += 1
        y += 1
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_DOWN:
                player.m_down = True
            if event.key == K_UP:
                player.m_up = True
            if event.key == K_LEFT:
                player.m_left = True
                player.face_left = True
                player.face_right = False
            if event.key == K_RIGHT:
                player.m_right = True
                player.face_left = False
                player.face_right = True

        if event.type == pygame.KEYUP:
            if event.key == K_DOWN:
                player.m_down = False
            if event.key == K_UP:
                player.m_up = False
            if event.key == K_LEFT:
                player.m_left = False
                player.walk_left[3] = 0
                player.walk_left[2] = 0
            if event.key == K_RIGHT:
                player.m_right = False
                player.walk_right[3] = 0
                player.walk_right[2] = 0
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
    if player.m_up:
        player.y -= 2
    if player.m_down:
        player.y += 2

    screen.blit(pygame.transform.scale(display, window_size), (0, 0))
    pygame.display.update()
    clock.tick(60)
