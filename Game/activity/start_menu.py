import pygame as pg
from Game.config import *
from Game.color import *
from Game.Objects.Button import *
from Game.activity.car import scene_car

pg.init()

pg.display.set_caption(NAME)
bg = pg.image.load('image/menu/start_fon.png')


def switch_scene(scene):
    global current_scene
    current_scene = scene


# начальный экран
def scene_start():
    run = True
    while run:
        # выход
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                switch_scene(None)
            elif event.type == pg.MOUSEBUTTONDOWN:
                # получение позиции мышки
                x_pos, y_pos = pg.mouse.get_pos()
                if 125 < x_pos < 425 and 352 < y_pos < 397:
                    switch_scene(scene_car())
                    run = False
        screen.fill(BG_COLOR)  # фон
        bg_img = pg.transform.scale(bg, (499, 585))

        # отрисовка заднего фона
        screen.blit(bg_img, (26, 96))
        button_shadow = MenuShadow(300, 55, BUTTON_RED_SHADOW).draw(125, 352)  # создание тени кнопки
        button = Menu(300, 50, BUTTON_RED).draw(125, 352, 'Играть')  # создание кнопки
        text_font = pg.font.Font('fonts/Jura-Bold.ttf', 16)
        text_red = text_font.render('Владимир Егоров', False, TEXT_RED)  # создание текстовых надписей
        text_white = text_font.render('&', False, TEXT_WHITE)  # создание текстовых надписей
        text_blue = text_font.render('Анастасия Антонова', False, TEXT_BLUE)  # создание текстовых надписей
        screen.blit(text_red, (110, 701))
        screen.blit(text_white, (270, 701))
        screen.blit(text_blue, (299, 701))
        pg.display.update()
