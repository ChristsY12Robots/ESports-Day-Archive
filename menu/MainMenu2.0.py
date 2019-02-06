import pygame
import os
import sys
import importlib.util

#Path to games folder
path = os.getcwd()
path = path[:-4]
path += 'games'


#Set Up Window
width,height = 1280,720
pygame.init()
window = pygame.display.set_mode((width,height))
pygame.display.set_caption('Main Menu')

fps = pygame.time.Clock()

# Loading Images
MainMenu = pygame.image.load('mainmenubackground.jpg')
runim = pygame.image.load('run.png')
sokobanim = pygame.image.load('sokoban.png')
spaceinvadersim = pygame.image.load('spaceinvaders.png')
tetrisim = pygame.image.load('tetris.png')
dinoim = pygame.image.load('dino.png')
snakeim = pygame.image.load('snake.png')

def open_game(game):
    pygame.quit()
    spec = importlib.util.spec_from_file_location(game+".py", "{}/{}/{}.py".format(path,game,game))
    dirpath = "{}\{}".format(path,game)
    os.chdir(dirpath)
    sys.path.insert(0, dirpath)
    foo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(foo)
    foo.MyClass()
    
def menu_animation():
    shift = 400
    while shift > -20:
            window.blit(MainMenu,[0,0])
            window.blit(runim, [301 - shift,184])
            window.blit(spaceinvadersim, [190 - shift,340])
            window.blit(snakeim, [210 - shift,515])
            window.blit(sokobanim, [686 + shift,188])
            window.blit(tetrisim, [750 + shift,339])
            window.blit(dinoim, [804 + shift,524])
            pygame.display.update()
            shift -= 20

def main():
    menu_animation()
    while True:
        window.blit(MainMenu,[0,0])
        hover = False 
        fps.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        #x + width > mouse_x > x and y + height > mouse_y > y

        #run
        if 301 + 231 > mouse[0] > 301 and 184 + 111 > mouse[1] > 184:
            window.blit(runim, [301,184])
            hover = True
            if click[0] == 1:
                open_game('run')
        #spaceinvaders
        if 190 + 332 > mouse[0] > 190 and 340 + 142 > mouse[1] > 340:
            window.blit(spaceinvadersim, [190,340])
            hover = True
            if click[0] == 1:
                open_game('spaceinvaders')
        #snake
        if 210 + 325 > mouse[0] > 210 and 515 + 106 > mouse[1] > 515:
            window.blit(snakeim, [210,515])
            hover = True
            if click[0] == 1:
                open_game('snake')
        #sokoban
        if 686 + 468 > mouse[0] > 686 and 188 + 102 > mouse[1] > 188:
            window.blit(sokobanim, [686,188])
            hover = True
            if click[0] == 1:
                open_game('sokoban')
        #tetris
        if 750 + 319 > mouse[0] > 750 and 339 + 112 > mouse[1] > 339:
            window.blit(tetrisim, [750,339])
            hover = True
            if click[0] == 1:
                open_game('tetris')
        #dino
        if 804 + 277 > mouse[0] > 804 and 524 + 94 > mouse[1] > 524:
            window.blit(dinoim, [804,524])
            hover = True
            if click[0] == 1:
                open_game('dino')                
        
  
                
        if hover != True:
            window.blit(runim, [301,184])
            window.blit(spaceinvadersim, [190,340])
            window.blit(snakeim, [210,515])
            window.blit(sokobanim, [686,188])
            window.blit(tetrisim, [750,339])
            window.blit(dinoim, [804,524])

        pygame.display.update()
            
            
        

        
main()
