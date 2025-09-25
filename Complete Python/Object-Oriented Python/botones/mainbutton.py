from simpleboton import SimpleButton
import pygame
from pygame.locals import *
import sys

# Constantes
GRAY = (200, 200, 200)
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
FRAMES_PER_SECOND = 30 

# 2 - Initialializar
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()  

def hacerClic():
    print("CLICK!")

oButton1 = SimpleButton(window,(50,50),
                       'botones/images/buttonDown.png',
                       'botones/images/buttonUp.png', callback=hacerClic)

oButton2 = SimpleButton(window,(100,107),
                       'botones/images/buttonDown.png',
                       'botones/images/buttonUp.png', callback=hacerClic)

oButton3 = SimpleButton(window,(200,160),
                       'botones/images/buttonDown.png',
                       'botones/images/buttonUp.png', callback=hacerClic)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        oButton1.handleEvent(event)
        oButton2.handleEvent(event)
        oButton3.handleEvent(event)

    

    window.fill(GRAY)

    oButton1.draw()
    oButton2.draw()
    oButton3.draw()

    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)


    