import pygame
import sys
import time
import home
import props
import play
import levels.level1 as level1
import levels.level2 as level2
import levels.level3 as level3
import levels.level4 as level4
import levels.level5 as level5
import levels.level6 as level6
import skins
import levels.gameBasics as gameBasics

import settings
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
textRect.center = (screenSizeX / 2, screenSizeY / 5.5)

resize_ability = True

colorR = 190
colorG = 170
colorB = 160
cr = 4
cg = 3
cb = 2

# custom user event to change color
CHANGE_COLOR = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOR, 60)

GRAVITY_event = pygame.USEREVENT + 2
pygame.time.set_timer(GRAVITY_event, 1)

y_position = 0
is_full_screen = False
can_jump = True
in_mid_jump = False
speed = 0.0010
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()
        screenSizeX, screenSizeY = screen.get_size()

        if event.type == 32781:  # if make it fullscreen
            screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            screenSizeX, screenSizeY = screen.get_size()
            resize_ability = False
            is_full_screen = True

        if 'level' in props.page:
            if event.type == GRAVITY_event and not in_mid_jump:
                if y_position < screenSizeY - screenSizeY / 5 - screenSizeX / 100:
                    y_position += screenSizeY * speed
                    speed += 0.0001
                    can_jump = False
                else:
                    can_jump = True
                    speed = 0.0010
            if can_jump and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                in_mid_jump = True
            if in_mid_jump:
                if y_position > screenSizeY / 2.8:
                    y_position -= screenSizeY * speed
                    speed += 0.0001
                else:
                    speed = 0.0010
                    in_mid_jump = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if full_back_button["backBoxL"].collidepoint(event.pos):
                    playMark = 1
                    props.page = 'play'
                    print("back1")
                    if not is_full_screen:
                        pygame.display.set_mode((screenSizeX, screenSizeY), pygame.RESIZABLE)
            if event.type == pygame.MOUSEMOTION:
                gameBasics.checkBackButtons(event.pos, screen, full_back_button)


        if props.page == 'home':
            # change text color each XX ms
            if event.type == CHANGE_COLOR:
                # screenSizeX, screenSizeY = screen.get_size()
                font = pygame.font.Font(props.globalFont, int(screenSizeX / 11))
                textRect.center = (screenSizeX / 2, screenSizeY / 5.5)
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
                home.home_resized(screen)

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
                    props.page = 'settings'
                    print("Settings")
            if event.type == pygame.MOUSEMOTION:
                home.checkHomeButtons(event.pos, screen)
                screen.blit(text, textRect)
    if props.page == 'play':
        play.play_button_pressed(screen, home.create_back_button)
    if 'level' in props.page:
        if resize_ability:
            pygame.display.set_mode((screenSizeX, screenSizeY))
            resize_ability = False
        lvl = int(props.page.replace('level', ''))
        match lvl:
            case 1:
                level1.start(screen, y_position, full_back_button)
            case 2:
                level2.start(screen, y_position, full_back_button)
            case 3:
                level3.start(screen, y_position, full_back_button)
            case 4:
                level4.start(screen, y_position, full_back_button)
            case 5:
                level5.start(screen, y_position, full_back_button)
            case 6:
                level6.start(screen, y_position, full_back_button)

    if props.page == 'settings':
        settings.settings_button_pressed(screen)
    if props.page == 'skins':
        skins.skins_button_pressed(screen, home.create_back_button)

    pygame.display.update()
