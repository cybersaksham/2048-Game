from Scripts.screen import *
from Scripts.font import FONT

GAME_WINDOW = pygame.transform.scale(pygame.image.load("Gallery/Images/grid.png"), (SCREENWIDTH, SCREENHEIGHT))

BOXES = [[(16, 20), (163, 20), (313, 20), (458, 20)],
         [(16, 168), (163, 168), (313, 168), (458, 168)],
         [(16, 317), (163, 317), (313, 317), (458, 317)],
         [(16, 463), (163, 463), (313, 463), (458, 463)]]
BOX_WIDTH = 125


# Showing Box
def drawBox(pos):
    text = FONT.render(str(pos[0]), 1, pygame.Color("black"))
    text_rect = text.get_rect(center=((pos[0] * 2 + BOX_WIDTH) / 2, (pos[1] * 2 + BOX_WIDTH) / 2))
    SCREEN.blit(text, text_rect)


# PREVIEW WINDOW
def gameWindow():
    SCREEN.blit(GAME_WINDOW, (0, 0))
    for item in BOXES:
        for pt in item:
            pygame.draw.rect(SCREEN, WHITE, pygame.Rect(pt[0], pt[1], BOX_WIDTH, BOX_WIDTH), 0)
            drawBox(pt)
