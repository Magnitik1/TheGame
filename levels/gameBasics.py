import pygame
import sys

import props

pygame.init()


def draw_a_cube(x, y):
    pass




def draw_character(screen, y_position):
    screen.fill(props.backgroundColor)
    screenSizeX, screenSizeY = screen.get_size()
    pygame.draw.rect(screen, 'green', (screenSizeX / 2 - screenSizeX / 15, y_position, screenSizeX / 15,
                                       screenSizeX / 15))  # x, y, width, height
    pygame.draw.rect(screen, 'red', (0, screenSizeY - screenSizeY / 10, screenSizeX, screenSizeY / 5))
    pygame.display.update()
