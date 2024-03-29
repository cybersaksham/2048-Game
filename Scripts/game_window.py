from Scripts.screen import *
from Scripts.font import FONT
from Scripts.status_window import showWon, showLose

GAME_WINDOW = pygame.transform.scale(pygame.image.load("Gallery/Images/grid.png"), (SCREENWIDTH, SCREENHEIGHT))

BOXES = [[(16, 20), (163, 20), (313, 20), (458, 20)],
         [(16, 168), (163, 168), (313, 168), (458, 168)],
         [(16, 317), (163, 317), (313, 317), (458, 317)],
         [(16, 463), (163, 463), (313, 463), (458, 463)]]
BOX_WIDTH = 125
EMPTY_BOXES = [pt for item in BOXES for pt in item]
FULL_BOXES = {}
CHOSEN = False
GAME_WON = False
GAME_LOST = False


# Showing Box
def drawBox(pos, no):
    pygame.draw.rect(SCREEN, NUMBERS[no], pygame.Rect(pos[0] + 20, pos[1] + 20, BOX_WIDTH - 40, BOX_WIDTH - 40), 0)
    text = FONT.render(str(no), 1, pygame.Color(BLACK))
    text_rect = text.get_rect(center=((pos[0] * 2 + BOX_WIDTH) / 2, (pos[1] * 2 + BOX_WIDTH) / 2))
    SCREEN.blit(text, text_rect)


# Reset Game
def resetGame():
    global CHOSEN, FULL_BOXES, EMPTY_BOXES, GAME_WON, GAME_LOST
    GAME_WON = False
    GAME_LOST = False
    CHOSEN = False
    FULL_BOXES = {}
    EMPTY_BOXES = [pt for item in BOXES for pt in item]


# Play Sound
def playSound(sound):
    pygame.mixer.stop()
    pygame.mixer.music.load(f"Gallery/Sounds/{sound}.wav")
    pygame.mixer.music.play()


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


# UP Logic
def UPLogic(item):
    fill_pt = list(filter(lambda box__: box__ not in EMPTY_BOXES, item))
    for i, j in enumerate(fill_pt):
        FULL_BOXES[item[i]] = FULL_BOXES[j]
        if item[i] != j:
            FULL_BOXES.pop(j)
            EMPTY_BOXES.append(j)
            EMPTY_BOXES.remove(item[i])


# DOWN Logic
def DOWNLogic(item):
    fill_pt = list(filter(lambda box__: box__ not in EMPTY_BOXES, item))[::-1]
    for i, j in enumerate(fill_pt):
        FULL_BOXES[item[len(item) - 1 - i]] = FULL_BOXES[j]
        if item[len(item) - 1 - i] != j:
            FULL_BOXES.pop(j)
            EMPTY_BOXES.append(j)
            EMPTY_BOXES.remove(item[len(item) - 1 - i])


# RIGHT Logic
def RIGHTLogic(item):
    fill_pt = list(filter(lambda box__: box__ not in EMPTY_BOXES, item))[::-1]
    for i, j in enumerate(fill_pt):
        FULL_BOXES[item[len(item) - 1 - i]] = FULL_BOXES[j]
        if item[len(item) - 1 - i] != j:
            FULL_BOXES.pop(j)
            EMPTY_BOXES.append(j)
            EMPTY_BOXES.remove(item[len(item) - 1 - i])


# LEFT Logic
def LEFTLogic(item):
    fill_pt = list(filter(lambda box__: box__ not in EMPTY_BOXES, item))
    for i, j in enumerate(fill_pt):
        FULL_BOXES[item[i]] = FULL_BOXES[j]
        if item[i] != j:
            FULL_BOXES.pop(j)
            EMPTY_BOXES.append(j)
            EMPTY_BOXES.remove(item[i])


# SUM Logic
def SUMLogic(item, i, j):
    if item[i] not in EMPTY_BOXES and item[j] not in EMPTY_BOXES:
        if FULL_BOXES[item[i]] == FULL_BOXES[item[j]]:
            FULL_BOXES[item[i]] *= 2
            FULL_BOXES.pop(item[j])
            EMPTY_BOXES.append(item[j])


# Event Handler
def eventHandler(event):
    global CHOSEN, GAME_WON, GAME_LOST
    if not GAME_WON and not GAME_LOST:
        if event.key == K_UP:
            playSound("slide")
            rev_list = revList()
            for item in rev_list:
                UPLogic(item)
                for i in range(3):
                    SUMLogic(item, i, i + 1)
                UPLogic(item)
            CHOSEN = False
        elif event.key == K_DOWN:
            playSound("slide")
            rev_list = revList()
            for item in rev_list:
                DOWNLogic(item)
                for i in range(3, 0, -1):
                    SUMLogic(item, i, i - 1)
                DOWNLogic(item)
            CHOSEN = False
        elif event.key == K_RIGHT:
            playSound("slide")
            for item in BOXES:
                RIGHTLogic(item)
                for i in range(3, 0, -1):
                    SUMLogic(item, i, i - 1)
                RIGHTLogic(item)
            CHOSEN = False
        elif event.key == K_LEFT:
            playSound("slide")
            for item in BOXES:
                LEFTLogic(item)
                for i in range(3):
                    SUMLogic(item, i, i + 1)
                LEFTLogic(item)
            CHOSEN = False
        for item in FULL_BOXES:
            if FULL_BOXES[item] == 2048:
                playSound("gamewon")
                GAME_WON = True
                CHOSEN = True
        if len(EMPTY_BOXES) == 0:
            playSound("gameover")
            GAME_LOST = True
            CHOSEN = True
    else:
        if event.key == K_SPACE:
            resetGame()


# PREVIEW WINDOW
def gameWindow():
    SCREEN.blit(GAME_WINDOW, (0, 0))
    for box in FULL_BOXES:
        drawBox(box, FULL_BOXES[box])
    if GAME_WON:
        showWon()
    elif GAME_LOST:
        showLose()
    else:
        chooseRandomBox()
