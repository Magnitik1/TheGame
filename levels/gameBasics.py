import pygame
import sys
import props
import skins

pygame.init()


def draw_a_cube(x, y):
    pass

playMark = 1
def checkBackButtons(pos, screen, full_back_button):
    global playMark
    if full_back_button['backBoxS'].collidepoint(pos) and playMark == 1:  # HOVERED
        playMark = 0
    elif not full_back_button['backBoxL'].collidepoint(pos) and playMark == 0:
        playMark = 1


jumps = 0



def draw_character(screen, y_position, full_back_button):
    global playMark
    global jumps
    screen.fill(props.backgroundColor)
    screenSizeX, screenSizeY = screen.get_size()
    imp = pygame.image.load(f".\\imgs\\{skins.curren_skin}")
    skin = pygame.transform.scale(imp, (screenSizeX / 15, screenSizeX / 15))
    skinBox = skin.get_rect()
    skinBox.center = (screenSizeX / 2 - screenSizeX / 30, y_position + screenSizeX / 30 - 1)
    screen.blit(skin, skinBox)

    imp = pygame.image.load(f".\\imgs\\floor.png")
    floor = pygame.transform.scale(imp, (screenSizeX+1, screenSizeY / 10))
    floorBox = floor.get_rect()
    floorBox.center = (screenSizeX/2, screenSizeY - screenSizeY / 20,)
    screen.blit(floor, floorBox)

    font = pygame.font.Font(props.globalFont, int(screenSizeX / 30))
    text = font.render(f'Jumps amount: {jumps}', True, props.fontColor)
    textRect = text.get_rect()
    textRect.center = (screenSizeX / 1.5, screenSizeY / 4)
    screen.blit(text, textRect)

    # pygame.draw.rect(screen, 'red', (0, screenSizeY - screenSizeY / 10, screenSizeX, screenSizeY / 5)) # x, y, width, height
    if playMark == 1:
        screen.blit(full_back_button['backS'], full_back_button['backBoxS'])
    if playMark == 0:
        screen.blit(full_back_button['backL'], full_back_button['backBoxL'])
    pygame.display.update()



