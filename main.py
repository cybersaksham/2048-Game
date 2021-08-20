from Scripts.imports import *
from Scripts.preview_window import prevWindow
from Scripts.game_window import gameWindow, eventHandler

# GAME VARIABLES
START_GAME = False


# GAME LOOP
def mainLoop():
    global START_GAME
    if not START_GAME:
        prevWindow()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                START_GAME = True
    else:
        gameWindow()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                eventHandler(event)
    pygame.display.update()


if __name__ == '__main__':
    while True:
        mainLoop()
