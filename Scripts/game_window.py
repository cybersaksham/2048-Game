from Scripts.screen import *
from Scripts.font import FONT

GAME_WINDOW = pygame.transform.scale(pygame.image.load("Gallery/Images/grid.png"), (SCREENWIDTH, SCREENHEIGHT))

BOXES = [[(16, 20), (163, 20), (313, 20), (458, 20)],
         [(16, 168), (163, 168), (313, 168), (458, 168)],
         [(16, 317), (163, 317), (313, 317), (458, 317)],
         [(16, 463), (163, 463), (313, 463), (458, 463)]]
BOX_WIDTH = 125
EMPTY_BOXES = [pt for item in BOXES for pt in item]
FULL_BOXES = {}
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
        FULL_BOXES[box__] = 2
        EMPTY_BOXES.remove(box__)


# Reverse List
def revList():
    rev_list = []
    for i in range(4):
        item = []
        for j in range(4):
            item.append(BOXES[j][i])
        rev_list.append(item)
    return rev_list


# Event Handler
def eventHandler(event):
    global CHOSEN
    if event.key == K_UP:
        rev_list = revList()
        for item in rev_list:
            fill_pt = list(filter(lambda box__: box__ not in EMPTY_BOXES, item))
            for i, j in enumerate(fill_pt):
                FULL_BOXES[item[i]] = FULL_BOXES[j]
                if item[i] != j:
                    FULL_BOXES.pop(j)
                    EMPTY_BOXES.append(j)
                    EMPTY_BOXES.remove(item[i])
        CHOSEN = False
    elif event.key == K_DOWN:
        rev_list = revList()
        for item in rev_list:
            fill_pt = list(filter(lambda box__: box__ not in EMPTY_BOXES, item))[::-1]
            for i, j in enumerate(fill_pt):
                FULL_BOXES[item[len(item) - 1 - i]] = FULL_BOXES[j]
                if item[len(item) - 1 - i] != j:
                    FULL_BOXES.pop(j)
                    EMPTY_BOXES.append(j)
                    EMPTY_BOXES.remove(item[len(item) - 1 - i])
        CHOSEN = False
    elif event.key == K_RIGHT:
        for item in BOXES:
            fill_pt = list(filter(lambda box__: box__ not in EMPTY_BOXES, item))[::-1]
            for i, j in enumerate(fill_pt):
                FULL_BOXES[item[len(item) - 1 - i]] = FULL_BOXES[j]
                if item[len(item) - 1 - i] != j:
                    FULL_BOXES.pop(j)
                    EMPTY_BOXES.append(j)
                    EMPTY_BOXES.remove(item[len(item) - 1 - i])
        CHOSEN = False
    elif event.key == K_LEFT:
        for item in BOXES:
            fill_pt = list(filter(lambda box__: box__ not in EMPTY_BOXES, item))
            for i, j in enumerate(fill_pt):
                FULL_BOXES[item[i]] = FULL_BOXES[j]
                if item[i] != j:
                    FULL_BOXES.pop(j)
                    EMPTY_BOXES.append(j)
                    EMPTY_BOXES.remove(item[i])
        CHOSEN = False


# PREVIEW WINDOW
def gameWindow():
    SCREEN.blit(GAME_WINDOW, (0, 0))
    chooseRandomBox()
    for box in FULL_BOXES:
        drawBox(box, FULL_BOXES[box])
