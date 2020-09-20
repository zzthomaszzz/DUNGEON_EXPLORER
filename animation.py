import pygame


def load_animation(path, tick_count=0):
    image_list = []
    n = 1
    loop = True
    while loop:
        try:
            image_list.append(pygame.image.load(path + f"_{n}" + ".png"))
            n += 1
        except pygame.error:
            break
    return image_list, tick_count


def do_animation(surface, animation, coordinate_and_size, tick_count, tick, restart, image):
    if tick_count == tick:
        image += 1
        tick_count = 0
    if image == len(animation) or restart:
        print(restart)
        image = 0
    surface.blit(animation[image], coordinate_and_size)
    tick_count += 1
    print(tick_count)
    print(image)
    return tick_count



