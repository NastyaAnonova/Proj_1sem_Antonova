import pygame as pg
from Game.config import *
from Game.color import *

pg.init()


def print_text(message, x, y, font_color=(255, 255, 255), font_name='fonts/Jura-SemiBold.ttf', font_size=22):
    font_name = pg.font.Font(font_name, font_size)
    text = font_name.render(message, True, font_color)
    screen.blit(text, (x, y))


class MenuShadow():
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

    def draw(self, x, y):
        pg.draw.rect(screen, self.color, (x, y, self.width, self.height), border_radius=10)


class Menu():
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

    def draw(self, x, y, message):
        pg.draw.rect(screen, self.color, (x, y, self.width, self.height), border_radius=10)
        print_text(message, x + 110, y + 10)
