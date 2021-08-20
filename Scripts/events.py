from Scripts.imports import *


def check_event():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
