from Scripts.screen import *
from Scripts.font import FONT


def showStatus(color, t1):
    pygame.draw.rect(SCREEN, color, pygame.Rect(80, 231, 442, 150), 0)
    text = FONT.render(t1, 1, pygame.Color(WHITE))
    text_rect = text.get_rect(center=(SCREENWIDTH / 2, 275))
    SCREEN.blit(text, text_rect)
    text2 = FONT.render("Press spacebar to restart.", 1, pygame.Color(WHITE))
    text_rect2 = text2.get_rect(center=(SCREENWIDTH / 2, 315))
    SCREEN.blit(text2, text_rect2)


def showWon():
    showStatus(GREEN, "2048 MADE!!!")


def showLose():
    showStatus(RED, "GAME OVER!!!")
