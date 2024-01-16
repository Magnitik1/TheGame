import pygame
import home
import props
import sys
def create_Select_level_button(screen, x, y, x_pos, y_pos):
    screenSizeX, screenSizeY = screen.get_size()

    global levelS
    global levelBoxS
    global levelL
    global levelBoxL

    imp = pygame.image.load(f".\\imgs\\level{x*y+x+1}.png")
    levelS = pygame.transform.scale(imp, (screenSizeX / 5.5, screenSizeX / 6.5))
    levelBoxS = levelS.get_rect()
    levelBoxS.center = (x_pos, y_pos)
    levelL = pygame.transform.scale(imp, (screenSizeX / 5.5, screenSizeX / 5.5))
    levelBoxL = levelL.get_rect()
    levelBoxL.center = (screenSizeX / 4, screenSizeY / 1.85)
    screen.blit(levelS, levelBoxS)


def play_button_pressed(screen, full_back_button):
    screenSizeX, screenSizeY = screen.get_size()
    t = 40
    w = screenSizeX / 3 - t
    h = screenSizeY / 2 - 2 * t
    marTop = 6 * t
    screen.fill('purple')
    for i in range(2):
        marLeft = 6*t
        for j in range(3):
            create_Select_level_button(screen, j, i, marLeft, marTop)
            marLeft += w
        marTop += h
    screen.blit(full_back_button['backS'], full_back_button['backBoxS'])
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            home.checkPlayButtons(event.pos)
            if props.page != 'play':
                home.checkHomeButtons((0, 0), screen)