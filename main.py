import pygame
import sys
import time

pygame.init()

# screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen = pygame.display.set_mode((1300, 700))
screenSizeX, screenSizeY = screen.get_size()
pygame.display.set_caption('The Game')

playMark = 0
skinsMark = 0
settingsMark = 0
backMark = 0

def play_button_pressed():
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
    screen.blit(back, backBoxS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            checkPlayButtons(event.pos)
            if page != 'play':
                checkHomeButtons((0, 0))
def checkHomeButtons(pos):
    # Play button
    global playS
    global playBoxL
    global playL
    global playBoxS
    global playMark
    global skinsS
    global skinsBoxL
    global skinsL
    global skinsBoxS
    global skinsMark
    global settingsS
    global settingsBoxL
    global settingsL
    global settingsBoxS
    global settingsMark

    if playBoxS.collidepoint(pos) and playMark == 1:  # HOVERED
        playMark = 0
        screen.fill(backgroundColor)
        screen.blit(playL, playBoxL)
        screen.blit(skinsS, skinsBoxS)
        screen.blit(settingsS, settingsBoxS)
    elif not playBoxL.collidepoint(pos) and playMark == 0:
        playMark = 1
        screen.fill(backgroundColor)
        screen.blit(playS, playBoxS)
        screen.blit(skinsS, skinsBoxS)
        screen.blit(settingsS, settingsBoxS)

    # Skins button

    if skinsBoxS.collidepoint(pos) and skinsMark == 1:  # HOVERED
        skinsMark = 0
        screen.fill(backgroundColor)
        screen.blit(skinsL, skinsBoxL)
        screen.blit(playS, playBoxS)
        screen.blit(settingsS, settingsBoxS)
    elif not skinsBoxL.collidepoint(pos) and skinsMark == 0:
        skinsMark = 1
        screen.fill(backgroundColor)
        screen.blit(skinsS, skinsBoxS)
        screen.blit(playS, playBoxS)
        screen.blit(settingsS, settingsBoxS)

    # Settings button

    if settingsBoxS.collidepoint(pos) and settingsMark == 1:  # HOVERED
        settingsMark = 0
        screen.fill(backgroundColor)
        screen.blit(settingsL, settingsBoxL)
        screen.blit(skinsS, skinsBoxS)
        screen.blit(playS, playBoxS)
    elif not settingsBoxL.collidepoint(pos) and settingsMark == 0:
        settingsMark = 1
        screen.fill(backgroundColor)
        screen.blit(settingsS, settingsBoxS)
        screen.blit(skinsS, skinsBoxS)
        screen.blit(playS, playBoxS)


def checkPlayButtons(pos):
    global backBoxS
    global page
    if backBoxS.collidepoint(pos):  # HOVERED
        page = 'home'


backgroundColor = 'white'
screen.fill(backgroundColor)

# Play button

imp = pygame.image.load(".\\imgs\\play.png")
playS = pygame.transform.scale(imp, (screenSizeX / 5, screenSizeX / 5))
playBoxS = playS.get_rect()
playBoxS.center = (screenSizeX / 2, screenSizeY / 1.85)
playL = pygame.transform.scale(imp, (screenSizeX / 4, screenSizeX / 4))
playBoxL = playL.get_rect()
playBoxL.center = (screenSizeX / 2, screenSizeY / 1.85)
screen.blit(playS, playBoxS)

# Skins button
imp = pygame.image.load(".\\imgs\\skins.png")
skinsS = pygame.transform.scale(imp, (screenSizeX / 6.5, screenSizeX / 6.5))
skinsBoxS = skinsS.get_rect()
skinsBoxS.center = (screenSizeX / 4, screenSizeY / 1.85)
skinsL = pygame.transform.scale(imp, (screenSizeX / 5.5, screenSizeX / 5.5))
skinsBoxL = skinsL.get_rect()
skinsBoxL.center = (screenSizeX / 4, screenSizeY / 1.85)
screen.blit(skinsS, skinsBoxS)

# Settings button
imp = pygame.image.load(".\\imgs\\settings.png")
settingsS = pygame.transform.scale(imp, (screenSizeX / 6.5, screenSizeX / 6.5))
settingsBoxS = settingsS.get_rect()
settingsBoxS.center = (screenSizeX / 1.25, screenSizeY / 1.85)
settingsL = pygame.transform.scale(imp, (screenSizeX / 5.5, screenSizeX / 5.5))
settingsBoxL = settingsL.get_rect()
settingsBoxL.center = (screenSizeX / 1.25, screenSizeY / 1.85)
screen.blit(settingsS, settingsBoxS)

# Back button

imp = pygame.image.load(".\\imgs\\back.webp")
imp = pygame.transform.rotate(imp, 180)
back = pygame.transform.scale(imp, (screenSizeX / 10, screenSizeX / 10))
backBoxS = back.get_rect()
backBoxS.center = (90, 80)

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
page = 'home'
while True:
    if page == 'home':
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
                if playBoxL.collidepoint(event.pos):
                    print("Play")
                    page = 'play'
                    break
                if skinsBoxL.collidepoint(event.pos):
                    print("Skins")
                if settingsBoxL.collidepoint(event.pos):
                    print("Settings")
            if event.type == pygame.MOUSEMOTION:
                checkHomeButtons(event.pos)
                screen.blit(text, textRect)
    if page == 'play':
        play_button_pressed()

    pygame.display.update()
