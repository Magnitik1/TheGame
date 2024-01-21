import pygame



def draw_a_cube(x, y):
    pass


def floor(screen):
    screenSizeX, screenSizeY = screen.get_size()
    pygame.draw.rect(screen, 'red', (0, screenSizeY-screenSizeY/10, screenSizeX, screenSizeY/10))

y_position = 100


def draw_character(screen):
    screenSizeX, screenSizeY = screen.get_size()
    pygame.draw.rect(screen, 'green', (screenSizeX/2 - screenSizeX / 15, y_position, screenSizeX / 15, screenSizeX / 15)) # x, y, width, height

    pass



