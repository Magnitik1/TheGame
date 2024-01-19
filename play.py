import pygame
import home
import props
import sys

all_levels = []
def create_Select_level_button(screen, x, y, x_pos, y_pos):
    global all_levels
    global levelS
    global levelBoxS
    global levelL
    global levelBoxL
    screenSizeX, screenSizeY = screen.get_size()

    imp = pygame.image.load(f".\\imgs\\level{x*y+x+1}.png")

    levelS = pygame.transform.scale(imp, (screenSizeX / 4.2, screenSizeY / 3.3))
    levelBoxS = levelS.get_rect()
    levelBoxS.center = (x_pos, y_pos)

    levelL = pygame.transform.scale(imp, (screenSizeX / 3, screenSizeY / 2))
    levelBoxL = levelL.get_rect()
    levelBoxL.center = (x_pos, y_pos)

    all_levels.append({"number": x*y+x+1, }) #add level BOXES small and large and IMAGES

    screen.blit(levelS, levelBoxS)


def checkPlayButtons(pos, screen):
    if full_back_button['backBoxS'].collidepoint(pos):  # HOVERED
        screen.blit(full_back_button['backL'], full_back_button['backBoxL'])
    # for i in range(6):
    #     if all_levels[i]['number']
        # props.page = 'home'
def play_button_pressed(screen, create_back_button):
    global full_back_button
    screenSizeX, screenSizeY = screen.get_size()
    full_back_button = create_back_button(screen)
    w = screenSizeX / 3.7
    h = screenSizeY / 2.8
    margin_top = screenSizeY / 2.6
    screen.fill('purple')
    for i in range(2):
        margin_left = screenSizeX/4
        for j in range(3):
            create_Select_level_button(screen, j, i, margin_left, margin_top)
            margin_left += w
        margin_top += h
    screen.blit(full_back_button['backS'], full_back_button['backBoxS'])
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            checkPlayButtons(event.pos, screen)
            if props.page != 'play':
                home.checkHomeButtons((0, 0), screen)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if home.playBoxL.collidepoint(event.pos):
                for i in range(1,7):
                    print(f'level{i}')
                    props.page = f'level{i}'
                    break
            if full_back_button["backBoxS"].collidepoint(event.pos):
                props.page = 'home'
                print("back")
        if event.type == pygame.MOUSEMOTION:
            checkPlayButtons(event.pos, screen)