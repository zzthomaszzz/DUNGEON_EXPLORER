import pygame


def load_animation(path):
    image_list = []
    n = 1
    loop = True
    while loop:
        try:
            image_list.append(pygame.image.load(path + f"_{n}" + ".png"))
            n += 1
        except pygame.error:
            break
    return image_list









