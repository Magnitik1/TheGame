import pygame
import sys
import props
import home

pygame.init()
screen = 0
screenSizeX, screenSizeY = 0, 0
# Set up colors
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
font = pygame.font.Font('freesansbold.ttf', 20)
frame_color = (25, 0, 0)
frame_thickness = 5
num_steps = 20
# Set up fonts
font = pygame.font.Font(None, 36)
playMark = 1

class GameControl:
    def __init__(self):

        self.volume_control = VolumeControl()
        self.theme_control = ThemeControl()
        self.options_button = Options()
        self.buttons = [
                           ToggleButton(f"Awesome Feature", (250 , 500))
                       ] +  [
                           ToggleButton(f"Button1", (500 ,500 ))
                       ] +  [
                           ToggleButton(f"Button2", (750 ,500 ))
                       ] +  [
                           ToggleButton(f"Button3", (1000 ,500 ))
                       ]

    def update(self, full_back_button):
        global playMark
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                if full_back_button['backBoxS'].collidepoint(event.pos) and playMark == 1:
                    playMark = 0
                elif not full_back_button['backBoxL'].collidepoint(event.pos) and playMark == 0:
                    playMark = 1
            if event.type == pygame.MOUSEBUTTONDOWN:
                if full_back_button['backBoxL'].collidepoint(event.pos):
                    global running
                    running = False
                    props.page = 'home'
                    print('back3')
                    return
            self.volume_control.handle_event(event)
            self.theme_control.handle_event(event)
            self.options_button.handle_event(event)
            for button in self.buttons:
                button.handle_event(event)

        # Cap the frame rate
        pygame.time.Clock().tick(30)

    def draw(self, screen):
        # Clear the screen

        # Update and draw the game controls
        self.volume_control.draw(screen)
        self.theme_control.draw(screen)
        self.options_button.draw(screen)
        for button in self.buttons:
            button.draw(screen)

        # Update the display
        pygame.display.flip()


class VolumeControl:
    def __init__(self):
        self.volume_level = 0.5  # Starting volume level (0.0 to 1.0)
        self.music_playing = False
        self.load_music()

    def load_music(self):
        pygame.mixer.music.load("CIPI.mp3")  # Replace with your music file path

    def play_music(self):
        if not self.music_playing:
            pygame.mixer.music.play(-1)  # -1 plays the music in an infinite loop
            self.music_playing = True

    def stop_music(self):
        if self.music_playing:
            pygame.mixer.music.stop()
            self.music_playing = False

    def adjust_volume(self, delta):
        self.volume_level += delta / 100.0  # Delta is in the range [-100, 100], convert to [-1.0, 1.0]
        self.volume_level = max(0.0, min(1.0, self.volume_level))  # Ensure volume is within the valid range
        pygame.mixer.music.set_volume(self.volume_level)

    def draw(self, screen):
        screenSizeX, screenSizeY = screen.get_size()
        # Draw volume label
        pygame.draw.rect(screen, frame_color, (
            screenSizeX / 4 - frame_thickness, screenSizeY / 3.5 - frame_thickness, 155 + 2 * frame_thickness, 40 + 2 * frame_thickness),
                         frame_thickness)
        pygame.draw.rect(screen, white, (screenSizeX / 4, screenSizeY / 3.5, 155, 40))
        volume_text = font.render("Volume: {}".format(int(self.volume_level * 100)), True, black)
        screen.blit(volume_text, (screenSizeX / 3.9, screenSizeY / 3.4))

        # Draw volume control buttons
        pygame.draw.rect(screen, frame_color, (
            575 - frame_thickness, 200 - frame_thickness, 40 + 2 * frame_thickness, 40 + 2 * frame_thickness),
                         frame_thickness)
        pygame.draw.rect(screen, white, (575, 200, 40, 40))  # Plus button
        plus_text = font.render("+", True, black)
        screen.blit(plus_text, (588, 205))
        pygame.draw.rect(screen, frame_color, (
            515 - frame_thickness, 200 - frame_thickness, 40 + 2 * frame_thickness, 40 + 2 * frame_thickness),
                         frame_thickness)
        pygame.draw.rect(screen, white, (515, 200, 40, 40))  # Minus button
        minus_text = font.render("-", True, black)
        screen.blit(minus_text, (530, 205))

        pygame.draw.rect(screen, frame_color, (
            screenSizeX / 2 - frame_thickness, screenSizeY / 3.5 - frame_thickness, 120 + 2 * frame_thickness, 40 + 2 * frame_thickness),
                         frame_thickness)
        pygame.draw.rect(screen, white, (screenSizeX / 2, screenSizeY / 3.5, 120, 40))  # Play/Stop button
        play_stop_text = font.render("Play/Stop", True, black)
        screen.blit(play_stop_text, (655, 210))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if 590 <= mouse_x <= 630 and 190 <= mouse_y <= 230:
                self.adjust_volume(10)  # Increase volume
            elif 250 <= mouse_x <= 290 and 10 <= mouse_y <= 50:
                self.adjust_volume(-10)  # Decrease volume
            elif 650 <= mouse_x <= 750 and 200 <= mouse_y <= 250:
                if self.music_playing:
                    self.stop_music()
                else:
                    self.play_music()


all_themes = [{'fontColor': props.fontColor, 'backgroundColor': props.backgroundColor},
              {'fontColor': 'black', 'backgroundColor': 'lightgrey'}]


class ThemeControl:
    def __init__(self):
        self.current_theme = 1  # 1: Green and Blue, 2: Black and White
        self.set_theme()

    def set_theme(self):
        self.background_color = all_themes[self.current_theme-1]['backgroundColor']
        self.button_color = white
        self.text_color = black

    def switch_theme(self):
        self.current_theme = 3 - self.current_theme  # Toggle between 1 and 2
        self.set_theme()

    def draw(self, screen):
        screenSizeX, screenSizeY = screen.get_size()
        # Draw theme label
        frame_thickness = 5
        pygame.draw.rect(screen, frame_color, (
        screenSizeX/3.5 - frame_thickness, screenSizeY/2.1- frame_thickness, 125 + 2 * frame_thickness, 50 + 2 * frame_thickness),
                         frame_thickness)
        pygame.draw.rect(screen, self.button_color, (screenSizeX/3.5, screenSizeY/2.1, 125, 50))

        theme_text = font.render("Theme: {}".format(self.current_theme), True, self.text_color)
        screen.blit(theme_text, (380, 345))



        # Draw theme switch button
        pygame.draw.rect(screen, frame_color, (
            600 - frame_thickness, 340 - frame_thickness, 190 + 2 * frame_thickness, 40 + 2 * frame_thickness),
                         frame_thickness)
        pygame.draw.rect(screen, self.button_color, (600, 340, 190, 40))
        switch_text = font.render("Switch Theme", True, self.text_color)
        screen.blit(switch_text, (610, 345))

    def handle_event(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if 600 <= mouse_x <= 800 and 350 <= mouse_y <= 400:
                self.switch_theme()



class Options:
    def __init__(self):
        self.clicked = False
        self.checkbox_checked = False  # Added attribute for checkbox state

    def draw(self, screen):
        screenSizeX, screenSizeY = screen.get_size()
        # Draw frame around the button
        frame_thickness = 5
        pygame.draw.rect(screen, frame_color, (
        100 - frame_thickness, 500 - frame_thickness, 120 + 2 * frame_thickness, 40 + 2 * frame_thickness),
                         frame_thickness)
        # Draw button
        pygame.draw.rect(screen, white, (100, 500, 120, 40))
        button_text = font.render("Options", True, black)
        screen.blit(button_text, (110, 510))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if 10 <= mouse_x <= 130 and 110 <= mouse_y <= 150:
                self.clicked = not self.clicked  # Toggle the clicked state

                # Toggle checkbox state when button is clicked
                if self.clicked:
                    self.checkbox_checked = not self.checkbox_checked


class ToggleButton:
    def __init__(self, text, position):
        self.text = text
        self.position = position
        self.clicked = False
        self.checkbox_checked = False

    def draw(self, screen):
        # Draw button
        pygame.draw.rect(screen, white, (*self.position, 120, 40))

        # Draw frame around the button
        frame_thickness = 5
        pygame.draw.rect(screen, frame_color, (*self.position, 120, 40), frame_thickness)

        button_text = font.render(self.text, True, black)
        screen.blit(button_text, (self.position[0] + 10, self.position[1] + 10))
        frame_thickness = 5
        pygame.draw.rect(screen, frame_color, (
            self.position[0] + 150 - frame_thickness, self.position[1] + 5 - frame_thickness, 30 + 2 * frame_thickness,
            30 + 2 * frame_thickness), frame_thickness)

        # Draw rectangle
        pygame.draw.rect(screen, red, (self.position[0] + 150, self.position[1] + 5, 30, 30))
        # Draw checkbox if clicked
        if self.clicked:
            # Draw frame around the rectangle
            frame_thickness = 5
            pygame.draw.rect(screen, frame_color, (
            self.position[0] + 150 - frame_thickness, self.position[1] + 5 - frame_thickness, 30 + 2 * frame_thickness,
            30 + 2 * frame_thickness), frame_thickness)

            # Draw rectangle
            pygame.draw.rect(screen, green, (self.position[0] + 150, self.position[1] + 5, 30, 30))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # Check button click
            if self.position[0] <= mouse_x <= self.position[0] + 120 and self.position[1] <= mouse_y <= self.position[
                1] + 40:
                self.clicked = not self.clicked

                # Toggle checkbox state when button is clicked
                if self.clicked:
                    self.checkbox_checked = not self.checkbox_checked



def back_button(screen, create_back_button):
    full_back_button = create_back_button(screen)
    if playMark == 1:
        screen.blit(full_back_button['backS'], full_back_button['backBoxS'])
    else:
        screen.blit(full_back_button['backL'], full_back_button['backBoxL'])
    return full_back_button


# Create an instance of GameControl
game_control = GameControl()

running = True

def settings_button_pressed(screen1, create_back_button):
    global screen
    global running
    running = True
    screen = screen1
    while running:
        game_control.draw(screen1)
        screen.fill(props.backgroundColor)
        game_control.update(back_button(screen, create_back_button))
    home.checkHomeButtons((0, 0), screen)


