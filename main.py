from Scripts.imports import *
from Scripts.preview_window import prevWindow
from Scripts.game_window import gameWindow
from Scripts.events import check_event

# GAME VARIABLES
START_GAME = False


# GAME LOOP
def mainLoop():
    global START_GAME
    if not START_GAME:
        prevWindow()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                START_GAME = True
    else:
        gameWindow()
    check_event()
    pygame.display.update()


if __name__ == '__main__':
    while True:
        mainLoop()
