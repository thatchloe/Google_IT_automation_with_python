import pygame
from pygame.locals import *
import sys
import os
from win32api import GetSystemMetrics

pygame.init()

##Class for closing game##
def __Terminate():
    pygame.quit()
    sys.exit()

##Objects##
def text_objects(text, font):
    textSurface = font.render(text, True, (255, 255, 255))
    return textSurface, textSurface.get_rect()

##Music##
def music_menu():
    file = r'C:\Users\N Davies\Desktop\sound.wav'
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()


def paused():
    pygame.mixer.music.pause()

def unpause():
    global pause
    pygame.mixer.music.unpause
    pause = False

##Setting up Start Screen##
def __StartupScreen():

        ##Defining Colours
        red = (200,0,0)
        green = (0,200,0)
        bright_red = (255,0,0)
        bright_green = (0,255,0)
        white = (255,255,255)
        black = (0,0,0)
        
        screen_width = GetSystemMetrics(0)
        screen_height = GetSystemMetrics(1)

        os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0"

        screen = pygame.display.set_mode((screen_width, screen_height), pygame.NOFRAME)

        screen.fill(white)
        
        ##surface, colour, rect --> rect: x, y, width, height
       ##optionsButton = pygame.draw.rect(screen, (0, 0, 0), (760, 600, 400, 75))

        ##Detect Mouse Positon##
        mouse = pygame.mouse.get_pos()

        ##If the x coord + the width is greater than the mouse position , while it is greater than the x coord.##
        ##And the y coord + the width is greater than the mouse position, while it is greater than the y coord.##

        if 760+400 > mouse[0] > 760 and 600+75 > mouse[1] > 600:
            pygame.draw.rect(screen, green, (760, 600, 400, 75))
            
            smallText = pygame.font.Font("freesansbold.ttf",40)
            textSurf, textRect = text_objects("Select", smallText)
            textRect.center = ( (760+(400/2)), (600+(75/2)) )
            screen.blit(textSurf, textRect)
        else:
            pygame.draw.rect(screen, black, (760, 600, 400, 75))
            
            smallText = pygame.font.Font("freesansbold.ttf",40)
            textSurf, textRect = text_objects("Options", smallText)
            textRect.center = ( (760+(400/2)), (600+(75/2)) )
            screen.blit(textSurf, textRect)
            
        music_menu()
        
        pygame.display.update()
        clock = pygame.time.Clock()
        clock.tick(15)

##Setting up Main Game Screen
def __GameScreen():
    ##GetSystemMetrics(0) can be used to auto detect resolution
    screen_width = GetSystemMetrics(0)
    screen_height = GetSystemMetrics(1)

    os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0"

    screen = pygame.display.set_mode((screen_width, screen_height), pygame.NOFRAME)

def __StartUp():

    done_menu = False  

    while not done_menu:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done_menu = True
            elif event.type == pygame.QUIT:
                done_menu = True
        if done_menu:
            __Terminate()

        __StartupScreen()
    
def Floor():
    screen = pygame.display.get_surface()
    pygame.display.update()
    
    pygame.draw.line(screen, (100, 100, 100), (0, 900), (1920, 900))

    
#Main Class
def __Main():
    ##Calling Screen Size
    __GameScreen()      
    
    ##Setting up quit condition.
    done_game = False
    
    while not done_game:
        Floor()
        ##An event is tracked: event is key or mouse motion.
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done_game = True
            elif event.type == pygame.QUIT:
                done_game = True
        if done_game:
            __Terminate()

##Running Game
__StartUp()

##INFORMATION
    ##while True:
    ##    events()
        ##Pressed keys, mouse motions.
    ##    loop()
        ##Changes with characters and npcs in the game world.
    ##    render()
        ##Screen graphic.
