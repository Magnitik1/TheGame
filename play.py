import pygame
import home
import props
import sys

all_levels = []


def create_Select_level_button(screen, c, x_pos, y_pos):
    screenSizeX, screenSizeY = screen.get_size()

    imp = pygame.image.load(f".\\imgs\\level{c}.png")

    levelS = pygame.transform.scale(imp, (screenSizeX / 4.2, screenSizeY / 3.3))
    levelBoxS = levelS.get_rect()
    levelBoxS.center = (x_pos, y_pos)

    levelL = pygame.transform.scale(imp, (screenSizeX / 3.5, screenSizeY / 2.8))
    levelBoxL = levelL.get_rect()
    levelBoxL.center = (x_pos, y_pos)

    all_levels.append(
        {"number": c, 'levelBoxL': levelBoxL, 'levelBoxS': levelBoxS, 'levelL': levelL,
         'levelS': levelS})  # add level BOXES small and large and IMAGES

    screen.blit(levelS, levelBoxS)


playMark = 1

levelsMark = [1 for i in range(6)]

def checkPlayButtons(pos, screen):
    global playMark
    global levelsMark
    if full_back_button['backBoxS'].collidepoint(pos) and playMark == 1:  # HOVERED
        playMark = 0
    elif not full_back_button['backBoxL'].collidepoint(pos) and playMark == 0:
        playMark = 1
    for i in range(6):
        if all_levels[i]['levelBoxS'].collidepoint(pos) and levelsMark[i] == 1:
            levelsMark[i] = 0
        elif not all_levels[i]['levelBoxL'].collidepoint(pos) and levelsMark[i] == 0:
            levelsMark[i] = 1


def play_button_pressed(screen, create_back_button):
    global full_back_button
    global all_levels
    global playMark
    screenSizeX, screenSizeY = screen.get_size()
    full_back_button = create_back_button(screen)
    w = screenSizeX / 3.7
    h = screenSizeY / 2.8
    margin_top = screenSizeY / 2.6
    screen.fill(props.backgroundColor)
    c = 1
    all_levels = []
    for i in range(2):
        margin_left = screenSizeX / 4
        for j in range(3):
            create_Select_level_button(screen, c, margin_left, margin_top)
            c += 1
            margin_left += w
        margin_top += h
    if playMark == 1:
        screen.blit(full_back_button['backS'], full_back_button['backBoxS'])
    if playMark == 0:
        screen.blit(full_back_button['backL'], full_back_button['backBoxL'])
    for i in range(6):
        if levelsMark[i] == 1:
            screen.blit(all_levels[i]['levelS'], all_levels[i]['levelBoxS'])
        if levelsMark[i] == 0:
            screen.blit(all_levels[i]['levelL'], all_levels[i]['levelBoxL'])
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(6):
                if all_levels[i]['levelBoxL'].collidepoint(event.pos):
                    print(f'level{i + 1}')
                    break
                # props.page = f'level{i}'
            if full_back_button["backBoxL"].collidepoint(event.pos):
                playMark = 1
                props.page = 'home'
                home.checkHomeButtons((0, 0), screen)
                print("back")
        if event.type == pygame.MOUSEMOTION:
            checkPlayButtons(event.pos, screen)
