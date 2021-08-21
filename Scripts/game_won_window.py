from Scripts.screen import *
from Scripts.font import FONT


def showWon():
    pygame.draw.rect(SCREEN, "green", pygame.Rect(80, 231, 442, 150), 0)
    text = FONT.render("2048 MADE!!!", 1, pygame.Color("white"))
    text_rect = text.get_rect(center=(SCREENWIDTH / 2, 275))
    SCREEN.blit(text, text_rect)
    text2 = FONT.render("Click anywhere to restart.", 1, pygame.Color("white"))
    text_rect2 = text2.get_rect(center=(SCREENWIDTH / 2, 315))
    SCREEN.blit(text2, text_rect2)
