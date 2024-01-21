import pygame
import sys
import time
import home
import props
import play
import levels.level1 as level1
import levels.level2 as level2
import skins

pygame.init()

# screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen = pygame.display.set_mode((1300, 700), pygame.RESIZABLE)
pygame.display.set_caption('The Game')
screenSizeX, screenSizeY = screen.get_size()
screen.fill(props.backgroundColor)
home.create_play_button(screen)
home.create_skins_button(screen)
home.create_settings_button(screen)
full_back_button = home.create_back_button(screen)



font = pygame.font.Font(props.globalFont, int(screenSizeX / 11))
text = font.render('The Game', True, 'green')
textRect = text.get_rect()
textRect.center = (screenSizeX / 2, 150)
colorR = 190
colorG = 170
colorB = 160
cr = 4
cg = 3
cb = 2

# custom user event to change color
CHANGE_COLOR = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOR, 60)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()
        if props.page == 'home':
            # change text color each XX ms
            if event.type == CHANGE_COLOR:
                text = font.render('The Game', True, (colorR, colorG, colorB))
                colorR += cr
                colorG += cg
                colorB += cb
                if colorR >= 230 or colorR <= 160:
                    cr = -cr
                if colorG >= 230 or colorG <= 160:
                    cg = -cg
                if colorB >= 230 or colorB <= 160:
                    cb = -cb
                screen.blit(text, textRect)
            # on resize changes
            if event.type == pygame.VIDEORESIZE:
                screenSizeX, screenSizeY = screen.get_size()
                screen.fill(props.backgroundColor)
                home.create_play_button(screen)
                home.create_skins_button(screen)
                home.create_settings_button(screen)
                font = pygame.font.Font('freesansbold.ttf', int(screenSizeX / 11))
                text = font.render('The Game', True, 'green')
                textRect = text.get_rect()
                textRect.center = (screenSizeX / 2, screenSizeY / 5.5)
                screen.blit(text, textRect)

                pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if home.playBoxL.collidepoint(event.pos):
                    print("Play")
                    props.page = 'play'
                    break
                if home.skinsBoxL.collidepoint(event.pos):
                    props.page = 'skins'
                    print("Skins")
                if home.settingsBoxL.collidepoint(event.pos):
                    props.page = 'play'
                    print("Settings")
            if event.type == pygame.MOUSEMOTION:
                home.checkHomeButtons(event.pos, screen)
                screen.blit(text, textRect)
    if props.page == 'play':
        play.play_button_pressed(screen, home.create_back_button)
    if 'level' in props.page:
        lvl = int(props.page.replace('level', ''))
        match lvl:
            case 1:
                level1.start(screen)
            case 2:
                level2.start(screen)
            # case 3:
            #     level3.start()
            # case 4:
            #     level4.start()
            # case 5:
            #     level5.start()
            # case 6:
            #     level6.start()

    # if props.page == 'settings':
    #     settings.settings_button_pressed(screen, home.create_back_button)
    if props.page == 'skins':
        skins.skins_button_pressed(screen, home.create_back_button)


    pygame.display.update()
