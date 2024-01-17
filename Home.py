import pygame
import sys
import props

playMark = 0
skinsMark = 0
settingsMark = 0
backMark = 0

# Play button
def create_play_button(screen):
    screenSizeX, screenSizeY = screen.get_size()

    global playS
    global playBoxS
    global playL
    global playBoxL
    imp = pygame.image.load(".\\imgs\\play.png")
    playS = pygame.transform.scale(imp, (screenSizeX / 5, screenSizeX / 5))
    playBoxS = playS.get_rect()
    playBoxS.center = (screenSizeX / 2, screenSizeY / 1.85)
    playL = pygame.transform.scale(imp, (screenSizeX / 4, screenSizeX / 4))
    playBoxL = playL.get_rect()
    playBoxL.center = (screenSizeX / 2, screenSizeY / 1.85)
    screen.blit(playS, playBoxS)


# Skins button
def create_skins_button(screen):
    screenSizeX, screenSizeY = screen.get_size()

    global skinsS
    global skinsBoxS
    global skinsL
    global skinsBoxL
    imp = pygame.image.load(".\\imgs\\skins.png")
    skinsS = pygame.transform.scale(imp, (screenSizeX / 6.5, screenSizeX / 6.5))
    skinsBoxS = skinsS.get_rect()
    skinsBoxS.center = (screenSizeX / 4, screenSizeY / 1.85)
    skinsL = pygame.transform.scale(imp, (screenSizeX / 5.5, screenSizeX / 5.5))
    skinsBoxL = skinsL.get_rect()
    skinsBoxL.center = (screenSizeX / 4, screenSizeY / 1.85)
    screen.blit(skinsS, skinsBoxS)

# Settings button
def create_settings_button(screen):
    screenSizeX, screenSizeY = screen.get_size()

    global settingsS
    global settingsBoxS
    global settingsL
    global settingsBoxL
    imp = pygame.image.load(".\\imgs\\settings.png")
    settingsS = pygame.transform.scale(imp, (screenSizeX / 6.5, screenSizeX / 6.5))
    settingsBoxS = settingsS.get_rect()
    settingsBoxS.center = (screenSizeX / 1.25, screenSizeY / 1.85)
    settingsL = pygame.transform.scale(imp, (screenSizeX / 5.5, screenSizeX / 5.5))
    settingsBoxL = settingsL.get_rect()
    settingsBoxL.center = (screenSizeX / 1.25, screenSizeY / 1.85)
    screen.blit(settingsS, settingsBoxS)

# Back button
def create_back_button(screen):
    screenSizeX, screenSizeY = screen.get_size()

    global backBoxS
    global backBoxL
    global backS
    global backL
    imp = pygame.image.load(".\\imgs\\back.webp")
    imp = pygame.transform.rotate(imp, 180)
    backS = pygame.transform.scale(imp, (screenSizeX / 10, screenSizeY / 5.5))
    backBoxS = backS.get_rect()
    backBoxS.center = (screenSizeX/13, screenSizeY/6)
    backL = pygame.transform.scale(imp, (screenSizeX / 8, screenSizeY / 4.5))
    backBoxL = backL.get_rect()
    backBoxL.center = (screenSizeX / 13, screenSizeY / 6)
    return {'backS': backS, 'backL': backL, 'backBoxS': backBoxS, 'backBoxL': backBoxL}


def checkHomeButtons(pos, screen):
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

    # Play button
    if playBoxS.collidepoint(pos) and playMark == 1:  # HOVERED
        playMark = 0
        screen.fill(props.backgroundColor)
        screen.blit(playL, playBoxL)
        screen.blit(skinsS, skinsBoxS)
        screen.blit(settingsS, settingsBoxS)
    elif not playBoxL.collidepoint(pos) and playMark == 0:
        playMark = 1
        screen.fill(props.backgroundColor)
        screen.blit(playS, playBoxS)
        screen.blit(skinsS, skinsBoxS)
        screen.blit(settingsS, settingsBoxS)

    # Skins button

    if skinsBoxS.collidepoint(pos) and skinsMark == 1:  # HOVERED
        skinsMark = 0
        screen.fill(props.backgroundColor)
        screen.blit(skinsL, skinsBoxL)
        screen.blit(playS, playBoxS)
        screen.blit(settingsS, settingsBoxS)
    elif not skinsBoxL.collidepoint(pos) and skinsMark == 0:
        skinsMark = 1
        screen.fill(props.backgroundColor)
        screen.blit(skinsS, skinsBoxS)
        screen.blit(playS, playBoxS)
        screen.blit(settingsS, settingsBoxS)

    # Settings button

    if settingsBoxS.collidepoint(pos) and settingsMark == 1:  # HOVERED
        settingsMark = 0
        screen.fill(props.backgroundColor)
        screen.blit(settingsL, settingsBoxL)
        screen.blit(skinsS, skinsBoxS)
        screen.blit(playS, playBoxS)
    elif not settingsBoxL.collidepoint(pos) and settingsMark == 0:
        settingsMark = 1
        screen.fill(props.backgroundColor)
        screen.blit(settingsS, settingsBoxS)
        screen.blit(skinsS, skinsBoxS)
        screen.blit(playS, playBoxS)

