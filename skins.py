import pygame
import home
import props
import sys

from play import checkPlayButtons

skins_date = ['skin_1.png', 'skin_2.png', 'skin_3.png', 'skin_4.png']
current_skin_number = 0
curren_skin = skins_date[current_skin_number]
changed_skin_number = 0
changed_skin = skins_date[changed_skin_number]
text_splitted = skins_date[current_skin_number].split('.png')
text_name1 = text_splitted[0]

def skins_button_pressed(screen, create_back_button):
    global full_back_button
    global current_skin_number
    global changed_skin_number
    global curren_skin
    global changed_skin
    global text_name1
    global text_splitted
    screenSizeX, screenSizeY = screen.get_size()
    full_back_button = create_back_button(screen)
    w = screenSizeX / 3.7
    h = screenSizeY / 2.8
    margin_top = screenSizeY / 2.6
    screen.fill('purple')

    imp = pygame.image.load(f".\\imgs\\{curren_skin}")

    skinS = pygame.transform.scale(imp, (screenSizeX / 6, screenSizeY / 3.3))
    skinBoxS = skinS.get_rect()
    skinBoxS.center = (screenSizeX / 4.35, screenSizeY / 2)

    screen.blit(skinS, skinBoxS)


    imp2 = pygame.image.load(f".\\imgs\\{changed_skin}")

    skin2S = pygame.transform.scale(imp2, (screenSizeX / 12, screenSizeY / 7))
    skin2BoxS = skin2S.get_rect()
    skin2BoxS.center = (screenSizeX / 1.5, screenSizeY / 2)

    screen.blit(skin2S, skin2BoxS)

    create_text_skins(screen)
    create_left_arrow_button(screen)
    create_right_arrow_button(screen)
    create_select_button(screen)
    create_skin_name(screen)
    create_back_button_new(screen)


    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if selectBoxS.collidepoint(event.pos):
                changed_skin_number = current_skin_number
                changed_skin = skins_date[changed_skin_number]
                print('Select')
            if leftarrowBoxS.collidepoint(event.pos):
                try:
                    current_skin_number = current_skin_number - 1
                    curren_skin = skins_date[current_skin_number]
                    text_splitted = skins_date[current_skin_number].split('.png')
                    text_name1 = text_splitted[0]
                    print('Left Arrow')
                except IndexError:
                    current_skin_number = 0
                    curren_skin = skins_date[current_skin_number]
            if rightarrowBoxS.collidepoint(event.pos):
                try:
                    current_skin_number = current_skin_number + 1
                    curren_skin = skins_date[current_skin_number]
                    text_splitted = skins_date[current_skin_number].split('.png')
                    text_name1 = text_splitted[0]
                    print('Right Arrow')
                except IndexError:
                    current_skin_number = 0
                    curren_skin = skins_date[current_skin_number]
                    text_splitted = skins_date[current_skin_number].split('.png')
                    text_name1 = text_splitted[0]
            if backbuttonBoxS.collidepoint(event.pos):
                props.page = 'home'
                home.checkHomeButtons((0, 0), screen)
                print("back")


def create_text_skins(screen):

    text_name_skins = "Skins"
    screenSizeX, screenSizeY = screen.get_size()
    fontObj = pygame.font.Font(None, 92)
    TEXTCOLOUR = (200, 100, 0)
    textSufaceObj = fontObj.render(text_name_skins, True, TEXTCOLOUR, None)
    screen.blit(textSufaceObj, (screenSizeX / 2, screenSizeY / 5))
def create_skin_name(screen):

    screenSizeX, screenSizeY = screen.get_size()
    fontObj = pygame.font.Font(None, 72)
    TEXTCOLOUR = (200, 100, 0)
    textSufaceObj2 = fontObj.render(text_name1, True, TEXTCOLOUR, None)
    screen.blit(textSufaceObj2, (screenSizeX / 5.7, screenSizeY / 4))
def create_left_arrow_button(screen):
    screenSizeX, screenSizeY = screen.get_size()

    global leftarrowS
    global leftarrowBoxS
    global leftarrowL
    global leftarrowL
    imp = pygame.image.load(".\\imgs\\left_arrow.png")
    leftarrowS = pygame.transform.scale(imp, (screenSizeX / 6.5, screenSizeY / 6.5))
    leftarrowBoxS = leftarrowS.get_rect()
    leftarrowBoxS.center = (screenSizeX / 7, screenSizeY / 1.35)


    # settingsL = pygame.transform.scale(imp, (screenSizeX / 5.5, screenSizeY / 8.5))
    # settingsBoxL = settingsL.get_rect()
    # settingsBoxL.center = (screenSizeX / 1.25, screenSizeY / 1.85)
    screen.blit(leftarrowS, leftarrowBoxS)
def create_right_arrow_button(screen):
    screenSizeX, screenSizeY = screen.get_size()

    global rightarrowS
    global rightarrowBoxS
    global rightarrowL
    global rightarrowBoxL
    imp = pygame.image.load(".\\imgs\\right_arrow.png")
    rightarrowS = pygame.transform.scale(imp, (screenSizeX / 6.5, screenSizeY / 6.5))
    rightarrowBoxS = rightarrowS.get_rect()
    rightarrowBoxS.center = (screenSizeX / 3.3, screenSizeY / 1.35)

    # settingsL = pygame.transform.scale(imp, (screenSizeX / 5.5, screenSizeX / 5.5))
    # settingsBoxL = settingsL.get_rect()
    # settingsBoxL.center = (screenSizeX / 1.25, screenSizeY / 1.85)
    screen.blit(rightarrowS, rightarrowBoxS)
def create_select_button(screen):
    screenSizeX, screenSizeY = screen.get_size()

    global selectS
    global selectBoxS
    global selectL
    global selectBoxL

    imp = pygame.image.load(".\\imgs\\select.png")
    selectS = pygame.transform.scale(imp, (screenSizeX / 6.5, screenSizeY / 6.5))
    selectBoxS = selectS.get_rect()
    selectBoxS.center = (screenSizeX / 4.5, screenSizeY / 1.13) # placement

    # selectL = pygame.transform.scale(imp, (screenSizeX / 6.5, screenSizeY / 6.5))
    # selectBoxL = selectL.get_rect()
    # selectBoxL.center = (screenSizeX / center_posX, screenSizeX / center_posY)
    screen.blit(selectS, selectBoxS)
def create_back_button_new(screen):
    screenSizeX, screenSizeY = screen.get_size()

    global backbuttonS
    global backbuttonBoxS
    global backbuttonL
    global backbuttonBoxL

    imp = pygame.image.load(".\\imgs\\button_back.png")
    backbuttonS = pygame.transform.scale(imp, (screenSizeX / 10, screenSizeY / 6))
    backbuttonBoxS = backbuttonS.get_rect()
    backbuttonBoxS.center = (screenSizeX / 17, screenSizeY / 10) # placement

    # selectL = pygame.transform.scale(imp, (screenSizeX / 6.5, screenSizeY / 6.5))
    # selectBoxL = selectL.get_rect()
    # selectBoxL.center = (screenSizeX / center_posX, screenSizeX / center_posY)
    screen.blit(backbuttonS, backbuttonBoxS)
