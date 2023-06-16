import pygame

NAME = 'Машинка'  # название

WIDTH = 550  # ширина
HEIGHT = 750  # высота

screen = pygame.display.set_mode((WIDTH, HEIGHT))  # экран

FPS = 120 # фпс

CLOCK = pygame.time.Clock()  # время

# Игра Машинка

GAMEOVER = False
SPEED = 2
SCORE = 0

# размеры дорог и маркеров

ROAD_WIDTH = 300
MARKER_WIDTH = 10
MARKER_HEIGHT = 50

# координаты переулка
LEFT_LANE = 150
CENTER_LANE = 250
RIGHT_LANE = 350
LANES = [LEFT_LANE, CENTER_LANE, RIGHT_LANE]

# дорожные и краевые маркеры
ROAD = (100, 0, ROAD_WIDTH, HEIGHT)
LEFT_EDGE_MARKER = (95, 0, MARKER_WIDTH, HEIGHT)
RIGHT_EDGE_MARKER = (395, 0, MARKER_WIDTH, HEIGHT)

# для анимации движения маркеров дорожек
LANE_MARKER_MOVE_Y = 0

# стартовые координаты игрока
PLAYER_X = 250
PLAYER_Y = 400
