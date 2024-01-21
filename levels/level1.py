import pygame
import levels.gameBasics as gameBasics


def start(screen):
    gameBasics.floor(screen)
    gameBasics.draw_character(screen)
    print('You are playing level 1!')