from Scripts.screen import *
from Scripts.font import FONT

GAME_WINDOW = pygame.transform.scale(pygame.image.load("Gallery/Images/grid.png"), (SCREENWIDTH, SCREENHEIGHT))

BOXES = [[(16, 20), (163, 20), (313, 20), (458, 20)],
         [(16, 168), (163, 168), (313, 168), (458, 168)],
         [(16, 317), (163, 317), (313, 317), (458, 317)],
         [(16, 463), (163, 463), (313, 463), (458, 463)]]
BOX_WIDTH = 125
EMPTY_BOXES = [pt for item in BOXES for pt in item]
FULL_BOXES = []
CHOSEN = False


# Showing Box
def drawBox(pos, no):
    text = FONT.render(str(no), 1, pygame.Color("black"))
    text_rect = text.get_rect(center=((pos[0] * 2 + BOX_WIDTH) / 2, (pos[1] * 2 + BOX_WIDTH) / 2))
    SCREEN.blit(text, text_rect)


# Choose Random Box
def chooseRandomBox():
    global CHOSEN
    if not CHOSEN:
        import random
        CHOSEN = True
        box__ = random.choice(EMPTY_BOXES)
        FULL_BOXES.append([box__, 2])


# PREVIEW WINDOW
def gameWindow():
    SCREEN.blit(GAME_WINDOW, (0, 0))
    chooseRandomBox()
    for box in FULL_BOXES:
        drawBox(box[0], box[1])
