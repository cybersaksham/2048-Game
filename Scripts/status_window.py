from Scripts.screen import *
from Scripts.font import FONT


def showStatus(color, t1):
    pygame.draw.rect(SCREEN, color, pygame.Rect(80, 231, 442, 150), 0)
    text = FONT.render(t1, 1, pygame.Color("white"))
    text_rect = text.get_rect(center=(SCREENWIDTH / 2, 275))
    SCREEN.blit(text, text_rect)
    text2 = FONT.render("Click anywhere to restart.", 1, pygame.Color("white"))
    text_rect2 = text2.get_rect(center=(SCREENWIDTH / 2, 315))
    SCREEN.blit(text2, text_rect2)


def showWon():
    showStatus("green", "2048 MADE!!!")


def showLose():
    showStatus("red", "GAME OVER!!!")