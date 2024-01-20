import pygame


def draw_a_cube(x, y):
    pass


def floor(screen):
    print('floor')
    screenSizeX, screenSizeY = screen.get_size()
    pygame.draw.rect(screen, 'red', (0, screenSizeX, 100, 50))
