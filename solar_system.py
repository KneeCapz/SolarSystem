import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (100, 50)

import pygame, sys, math, random

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

class soundCollection:
    def __init__(self):
        self.yaay = pygame.mixer.Sound('yaay.wav')
        self.yaay.set_volume(0.2)
        self.not_that_one = pygame.mixer.Sound('not_that_one.wav')
        self.not_that_one.set_volume(0.2)
        self.where_is = pygame.mixer.Sound('where_is.wav')
        self.where_is.set_volume(0.3)
        self.earth = pygame.mixer.Sound('earth.wav')
        self.earth.set_volume(0.3)
        self.jupiter = pygame.mixer.Sound('jupiter.wav')
        self.jupiter.set_volume(0.3)
        self.mars = pygame.mixer.Sound('mars.wav')
        self.mars.set_volume(0.3)
        self.merkur = pygame.mixer.Sound('merkur.wav')
        self.merkur.set_volume(0.3)
        self.moon = pygame.mixer.Sound('moon.wav')
        self.moon.set_volume(0.3)
        self.neptun = pygame.mixer.Sound('neptun.wav')
        self.neptun.set_volume(0.3)
        self.saturn = pygame.mixer.Sound('saturn.wav')
        self.saturn.set_volume(0.3)
        self.sola = pygame.mixer.Sound('sola.wav')
        self.sola.set_volume(0.5)
        self.uranus = pygame.mixer.Sound('uranus.wav')
        self.uranus.set_volume(0.3)
        self.venus = pygame.mixer.Sound('venus.wav')
        self.venus.set_volume(0.3)

class MapObjects:
    def __init__(self, name, position, sound):  ## name, posistion [x, y, radius], sound
        self.name = name
        self.position = position
        self.sound = sound

    def play_sound(self):
        if pygame.mixer.get_busy() == False:
            self.sound.play()

    def position(self):
        return self.position

    def is_over(self, x , y):
        self.sqx = (x - self.position[0])**2
        self.sqy = (y - self.position[1])**2
        if math.sqrt(self.sqx + self.sqy) < self.position[2]:
            return True

    def ask(self):
        self.answer = False
        self.a = True
        sounds.where_is.play()
        while self.a == True:
            if pygame.mixer.get_busy() == False:
                self.sound.play()
                self.a = False

        while self.answer == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]

                    if self.is_over(x, y) == True:
                        sounds.yaay.play()
                        self.answer = True
                        pygame.time.wait(4000)
                    elif 675 < x < 725 and 975 < y < 1000:
                        pygame.mixer.stop()
                        in_game = False
                        menu()

## General
pygame.init()
pygame.display.set_caption('Solsystemet')
clock = pygame.time.Clock()
running = True
white = (255 , 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

## Display
display_width = 1920
display_height = 1260
gameDisplay = pygame.display.set_mode((display_width, display_height))
gameBackground = Background('solarsystemNEW1920x1260.jpg', [0,0])

## Sound
sounds = soundCollection()

## Map objects. name, pos[x , y , radius], sound
jupiter = MapObjects('jupiter', [1683, 742, 184], sounds.jupiter)
saturn = MapObjects('saturn', [1587, 419, 129], sounds.saturn)
uranus = MapObjects('uranus', [1250, 217, 90], sounds.uranus)
neptun = MapObjects('neptun', [1015, 127, 78], sounds.neptun)
earth = MapObjects('earth', [620, 940, 314], sounds.earth)
mars = MapObjects('mars', [1328,946,90], sounds.mars)
venus = MapObjects('venus', [134,898,97], sounds.venus)
moon = MapObjects('moon', [960, 3015, 2028], sounds.moon)
sun = MapObjects('sun', [230, 285, 465], sounds.sola)
merkur = MapObjects('merkur', [128, 643, 33], sounds.merkur)

def menu_text(text):
    largeText = pygame.font.SysFont('comicsansms',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/3))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()

def button_text(text, position, size):
    buttonText = pygame.font.SysFont('comicsansms', size)
    TextSurf, TextRect = text_objects(text, buttonText)
    TextRect.center = (position)
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()

def text_objects(text, font):
    textSurface = font.render(text, True, red)
    return textSurface, textSurface.get_rect()

def menu():
    gameDisplay.fill(black)
    pygame.draw.rect(gameDisplay, white, (400, 600, 250, 100))
    pygame.draw.rect(gameDisplay, white, (800, 600, 250, 100))
    pygame.draw.rect(gameDisplay, white, (1200, 600, 250, 100))
    button_text('Solsystemet', ((display_width/2),(display_height/3)), 115)
    button_text('Start', (525, 650), 70)
    button_text('Spørr!', (925, 650), 70)
    button_text('Avslutt', (1325, 650), 70)
    pygame.display.update()
    in_menu = True

    while in_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                if 400 < x < 650 and 600 < y < 700:
                    in_menu = False
                    game_loop()
                elif 800 < x < 1050 and 600 < y < 700:
                    in_menu = False
                    where_is_game()
                elif 1200 < x < 1450 and 600 < y < 700:
                    pygame.quit()
                    quit()

def where_is_game():

    questions = [jupiter, sun, saturn, uranus, neptun, earth, mars, venus, merkur, moon]
    in_game = True

    while in_game:
        gameDisplay.blit(gameBackground.image, gameBackground.rect)
        pygame.draw.rect(gameDisplay, black, (925, 1235, 70, 25))
        button_text('Meny', (958,1245), 20)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                if 925 < x < 995 and 1235 < y < 1260:
                        pygame.mixer.stop()
                        in_game = False
                        menu()

        random.shuffle(questions)
        while len(questions) > 0:
            current = questions.pop()
            current.ask()

        pygame.display.update()
        clock.tick(60)

def game_loop():
    in_game = True
    while in_game:
        gameDisplay.blit(gameBackground.image, gameBackground.rect)
        pygame.draw.rect(gameDisplay, black, (925, 1235, 70, 25))
        button_text('Meny', (958,1245), 20)
        myObjects = [jupiter, sun, saturn, uranus, neptun, earth, mars, venus, merkur, moon]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]

                for i in myObjects:
                    if i.is_over(x, y) == True:
                        if i.name == 'earth':
                            if moon.is_over(x, y) ==True:
                                moon.play_sound()
                            else:
                                earth.play_sound()
                        elif i.name == 'sun':
                            if merkur.is_over(x, y) ==True:
                                merkur.play_sound()
                            else:
                                sun.play_sound()
                        else:
                            i.play_sound()
                        break
                    elif 925 < x < 995 and 1235 < y < 1260:
                        pygame.mixer.stop()
                        in_game = False
                        menu()


        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':

    while running:
        menu()


pygame.quit()
quit()
