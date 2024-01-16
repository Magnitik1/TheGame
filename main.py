import pygame
import sys
import time
import home
import props
import play

pygame.init()

# screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen = pygame.display.set_mode((1300, 700))
pygame.display.set_caption('The Game')
screenSizeX, screenSizeY = screen.get_size()
screen.fill(props.backgroundColor)
home.create_play_button(screen)
home.create_skins_button(screen)
home.create_settings_button(screen)
full_back_button = home.create_back_button(screen)

font = pygame.font.Font('freesansbold.ttf', 100)
text = font.render('The Game', True, 'green')
textRect = text.get_rect()
textRect.center = (screenSizeX / 2, 150)
colorR = 190
colorG = 170
colorB = 160
cr = 0.12
cg = -0.09
cb = 0.06
while True:
    if props.page == 'home':
        text = font.render('The Game', True, (colorR, colorG, colorB))
        colorR += cr
        colorG += cg
        colorB += cb
        if colorR >= 250 or colorR <= 160:
            cr = -cr
        if colorG >= 250 or colorG <= 160:
            cg = -cg
        if colorB >= 250 or colorB <= 160:
            cb = -cb
        screen.blit(text, textRect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if home.playBoxL.collidepoint(event.pos):
                    print("Play")
                    props.page = 'play'
                    break
                if home.skinsBoxL.collidepoint(event.pos):
                    print("Skins")
                if home.settingsBoxL.collidepoint(event.pos):
                    print("Settings")
            if event.type == pygame.MOUSEMOTION:
                home.checkHomeButtons(event.pos, screen)
                screen.blit(text, textRect)
    if props.page == 'play':
        play.play_button_pressed(screen, full_back_button)

    pygame.display.update()
