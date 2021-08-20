from Scripts.screen import *
from Scripts.font import FONT

PREVIEW_WINDOW = pygame.transform.scale(pygame.image.load("Gallery/Images/images.jpeg"), (SCREENWIDTH, SCREENHEIGHT))


# PREVIEW WINDOW
def prevWindow():
    SCREEN.blit(PREVIEW_WINDOW, (0, 0))
    SCREEN.blit(FONT.render("Click anywhere to start", True, WHITE), [SCREENWIDTH / 4, SCREENHEIGHT / 2 - 45])
