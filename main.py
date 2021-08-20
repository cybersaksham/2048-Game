import pygame
import sys
from pygame import mixer
from pygame.locals import *

# INITIALIZATION
pygame.init()
mixer.init()

# GAME SCREEN
SCREENWIDTH = 600
SCREENHEIGHT = 600
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption("2048 Game")


# GAME LOOP
def mainLoop():
    SCREEN.blit(pygame.transform.scale(pygame.image.load("Gallery/Images/images.jpeg"), (600, 600)), (0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()


if __name__ == '__main__':
    while True:
        mainLoop()
