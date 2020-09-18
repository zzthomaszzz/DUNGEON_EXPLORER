# Name: DUNGEON EXPLORER
"""Story line: You are a dungeon explorer, find the way out before it's too late"""
'''Mechanics: Dashing, Attacking and Looting and Equipping'''
'''Map: 5 rooms per map'''

# Variables name
import pygame, sys
from pygame import *

window_size = (1280, 720)
display_size = (480, 360)
clock = pygame.time.Clock()
background = pygame.image.load('background_red.png')


class Player:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.m_left = False
        self.m_right = False
        self.m_up = False
        self.m_down = False
        self.rect = pygame.Rect(int(self.x), int(self.y), self.width, self.y)


player = Player(50, 100, 60, 100)

screen = pygame.display.set_mode(window_size, pygame.FULLSCREEN, 32)
display = pygame.Surface(display_size)

while True:
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
            if event.key == K_RIGHT:
                player.m_right = True

        if event.type == pygame.KEYUP:
            if event.key == K_DOWN:
                player.m_down = False
            if event.key == K_UP:
                player.m_up = False
            if event.key == K_LEFT:
                player.m_left = False
            if event.key == K_RIGHT:
                player.m_right = False

    if player.m_right:
        player.x += 2
    if player.m_left:
        player.x -= 2
    if player.m_down:
        player.y += 2
    if player.m_up:
        player.y -= 2

    display.blit(background, (0, 0))
    player.rect = pygame.Rect(int(player.x), int(player.y), player.width, player.height)
    pygame.draw.rect(display, (0, 0, 0), player.rect)
    screen.blit(pygame.transform.scale(display, window_size), (0, 0))
    pygame.display.update()
    clock.tick(60)
