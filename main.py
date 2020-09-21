# Name: DUNGEON EXPLORER
"""Story line: You are a dungeon explorer, find the way out before it's too late"""
'''Mechanics: Dashing, Attacking and Looting and Equipping'''
'''Map: 5 rooms per map'''

# Variables name
import pygame, sys
from pygame import *
from animation import *
pygame.init()
window_size = (1280, 720)
display_size = (480, 360)
clock = pygame.time.Clock()
background = pygame.image.load('background_red.png')
image_okay = 0


class Player:
    def __init__(self, x, y, width, height, velocity, run=0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.walking = False
        self.standing = False
        self.action = False
        self.m_left = False
        self.m_right = False
        self.m_up = False
        self.m_down = False
        self.vel = velocity
        self.run = run
        self.run_1 = self.run
        self.running = False
        self.q_cool_down = 600
        self.q_up = True
        self.q_duration = 300
        self.q_tick = 0
        self.coor = (self.x, self.y, self.width, self.height)
        self.rect = pygame.Rect(int(self.x), int(self.y), self.width, self.y)
        self.image, self.tick = load_animation("Data/image/walking")
        self.okay = 0

    def check_buff(self):
        if self.running:
            self.q_tick += 1
            if self.q_tick != self.q_duration:
                self.run = self.run_1
                self.action = True
                self.q_up = False
            else:
                self.running = False
                self.q_tick = 0
        else:
            if not self.q_up:
                self.q_tick += 1
                if self.q_tick == self.q_cool_down:
                    self.q_up = True
                    self.q_tick = 0
            self.run = 0
            self.action = False


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


player = Player(50, 100, 20, 20, 1, 3)
bot, bot_tick = load_animation("testing_run")
bot_location = (400, 50, 20, 20)

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
            if event.key == K_RIGHT:
                player.m_right = True
            if event.key == K_q and player.q_up:
                player.running = True

        if event.type == pygame.KEYUP:
            if event.key == K_DOWN:
                player.m_down = False
            if event.key == K_UP:
                player.m_up = False
            if event.key == K_LEFT:
                player.m_left = False
            if event.key == K_RIGHT:
                player.m_right = False
    player.check_buff()

    if player.m_right:
        player.x += (player.vel + player.run)
    if player.m_left:
        player.x -= (player.vel + player.run)
    if player.m_down:
        player.y += (player.vel + player.run)
    if player.m_up:
        player.y -= (player.vel + player.run)

    player.rect = pygame.Rect(int(player.x), int(player.y), player.width, player.height)
    player.coor = (player.x, player.y, player.width, player.height)
    if player.m_right:
        player.tick = do_animation_1(display, player.image, player.coor, player.tick, 5, False)
    else:
        display.blit(pygame.image.load('testing_run.png'), player.coor)
    screen.blit(pygame.transform.scale(display, window_size), (0, 0))
    pygame.display.update()
    clock.tick(60)
