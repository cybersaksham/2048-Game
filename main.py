import pygame
import sys
from pygame import mixer
from pygame.locals import *
from Scripts.variables import *

# INITIALIZATION
pygame.init()
mixer.init()

# GAME SCREEN
SCREENWIDTH = 600
SCREENHEIGHT = 600
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption("2048 Game")

# FONT
FONT = pygame.font.SysFont(None, 40)

# IMAGES
PREVIEW_WINDOW = pygame.transform.scale(pygame.image.load("Gallery/Images/images.jpeg"), (SCREENWIDTH, SCREENHEIGHT))


# PREVIEW WINDOW
def prevWindow():
    SCREEN.blit(PREVIEW_WINDOW, (0, 0))
    SCREEN.blit(FONT.render("Click anywhere to start", True, WHITE), [SCREENWIDTH / 4, SCREENHEIGHT / 2 - 45])


# GAME LOOP
def mainLoop():
    prevWindow()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()


if __name__ == '__main__':
    while True:
        mainLoop()
