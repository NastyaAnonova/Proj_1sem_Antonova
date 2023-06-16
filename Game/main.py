import pygame as pg
from config import *
from activity.start_menu import *
from activity.car import *

pg.init()

pg.display.set_caption(NAME)

current_scene = None


# переключение сцен
def switch_scene(scene):
    global current_scene
    current_scene = scene


# сцены
scene_start()
scene_car()

switch_scene(scene_start())
while current_scene is not None:
    current_scene()
