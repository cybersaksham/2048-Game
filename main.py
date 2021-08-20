from Scripts.imports import *
from Scripts.preview_window import prevWindow
from Scripts.events import check_event


# GAME LOOP
def mainLoop():
    prevWindow()
    check_event()
    pygame.display.update()


if __name__ == '__main__':
    while True:
        mainLoop()
