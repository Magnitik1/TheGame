import pygame
import home
import props


def play_button_pressed(screen, full_back_button):
    screenSizeX, screenSizeY = screen.get_size()
    t = 40
    w = screenSizeX / 3 - t
    h = screenSizeY / 2 - 2 * t
    marTop = 4 * t
    screen.fill('purple')
    for i in range(2):
        marLeft = 2 * t
        for j in range(3):
            pygame.draw.rect(screen, (0, 0, 255), [marLeft, marTop, w - t, h - t], 0)
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