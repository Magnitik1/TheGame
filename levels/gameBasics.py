import pygame
import sys
import props

pygame.init()


def draw_a_cube(x, y):
    pass

playMark = 0
def checkBackButtons(pos, screen, full_back_button):
    global playMark
    if full_back_button['backBoxS'].collidepoint(pos) and playMark == 1:  # HOVERED
        playMark = 0
    elif not full_back_button['backBoxL'].collidepoint(pos) and playMark == 0:
        playMark = 1
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if full_back_button["backBoxL"].collidepoint(event.pos):
                playMark = 1
                props.page = 'play'
                # home.checkHomeButtons((0, 0), screen)
                print("back")


def draw_character(screen, y_position, full_back_button):
    global playMark
    screen.fill(props.backgroundColor)
    screenSizeX, screenSizeY = screen.get_size()

    pygame.draw.rect(screen, 'green', (screenSizeX / 2 - screenSizeX / 15, y_position, screenSizeX / 15,
                                       screenSizeX / 15))  # x, y, width, height
    pygame.draw.rect(screen, 'red', (0, screenSizeY - screenSizeY / 10, screenSizeX, screenSizeY / 5))
    if playMark == 1:
        screen.blit(full_back_button['backS'], full_back_button['backBoxS'])
    if playMark == 0:
        screen.blit(full_back_button['backL'], full_back_button['backBoxL'])
    pygame.display.update()



