import pygame
from pygame.locals import *
import random
from Game.color import *
from Game.config import *
from Game.Objects.Player import *
from Game.Objects.Button import *

pygame.init()

# группы спрайтов
player_group = pygame.sprite.Group()
vehicle_group = pygame.sprite.Group()

# создание машины игрока
player = PlayerVehicle(PLAYER_X, PLAYER_Y)
player_group.add(player)

# загрузка изображения автомобилей
image_filenames = ['car1.png', 'car2.png', 'car3.png', 'car4.png']
vehicle_images = []
for image_filename in image_filenames:
    image = pygame.image.load('image/car/' + image_filename)
    vehicle_images.append(image)

# загрузка изображения сбоя
crash = pygame.image.load('image/car/crash.png')
crash_rect = crash.get_rect()


def scene_car():
    global LANE_MARKER_MOVE_Y, SCORE, SPEED, GAMEOVER
    running = True
    while running:

        CLOCK.tick(FPS)

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

            # перемещение машины игрока с помощью клавиш со стрелками влево/вправо
            if event.type == KEYDOWN:

                if event.key == K_LEFT and player.rect.center[0] > LEFT_LANE:
                    player.rect.x -= 100
                elif event.key == K_RIGHT and player.rect.center[0] < RIGHT_LANE:
                    player.rect.x += 100

                # проверка, есть ли боковое столкновение после смены полосы движения
                for vehicle in vehicle_group:
                    if pygame.sprite.collide_rect(player, vehicle):

                        GAMEOVER = True

                        # поставить машину игрока рядом с другим транспортом
                        # и определение, где расположить изображение сбоя
                        if event.key == K_LEFT:
                            player.rect.left = vehicle.rect.right
                            crash_rect.center = [player.rect.left, (player.rect.center[1] + vehicle.rect.center[1]) / 2]
                        elif event.key == K_RIGHT:
                            player.rect.right = vehicle.rect.left
                            crash_rect.center = [player.rect.right,
                                                 (player.rect.center[1] + vehicle.rect.center[1]) / 2]

        # отрисовка фона
        screen.fill(BG_COLOR)

        # отрисовка дороги
        pygame.draw.rect(screen, GRAY, ROAD)

        # отрисовка крайних маркеров
        pygame.draw.rect(screen, YELLOW, LEFT_EDGE_MARKER)
        pygame.draw.rect(screen, YELLOW, RIGHT_EDGE_MARKER)

        # отрисовка маркеров дороги
        LANE_MARKER_MOVE_Y += SPEED * 2
        if LANE_MARKER_MOVE_Y >= MARKER_HEIGHT * 2:
            LANE_MARKER_MOVE_Y = 0
        for y in range(MARKER_HEIGHT * -2, HEIGHT, MARKER_HEIGHT * 2):
            pygame.draw.rect(screen, WHITE, (LEFT_LANE + 45, y + LANE_MARKER_MOVE_Y, MARKER_WIDTH, MARKER_HEIGHT))
            pygame.draw.rect(screen, WHITE, (CENTER_LANE + 45, y + LANE_MARKER_MOVE_Y, MARKER_WIDTH, MARKER_HEIGHT))

        # отрисовка машины игрока
        player_group.draw(screen)

        # добавление автомобиля
        if len(vehicle_group) < 2:
            add_vehicle = True
            for vehicle in vehicle_group:
                if vehicle.rect.top < vehicle.rect.height * 1.5:
                    add_vehicle = False

            if add_vehicle:
                # выбираем случайную дорожку
                lane = random.choice(LANES)

                # выбираем случайное изображение автомобиля
                image = random.choice(vehicle_images)
                vehicle = Vehicle(image, lane, HEIGHT / -2)
                vehicle_group.add(vehicle)

        # движение машин
        for vehicle in vehicle_group:
            vehicle.rect.y += SPEED

            # удаляем машину, как только она пропадает с экрана
            if vehicle.rect.top >= HEIGHT:
                vehicle.kill()

                # добавление счета
                SCORE += 1

                # ускоряем игру после прохождения 5 машин
                if SCORE > 0 and SCORE % 5 == 0:
                    SPEED += 0.5

        # отрисовка машин
        vehicle_group.draw(screen)

        # отображение счета
        font = pygame.font.Font('fonts/Jura-Bold.ttf', 20)
        text = font.render('Счёт: ' + str(SCORE), True, WHITE)
        text_rect = text.get_rect()
        text_rect.center = (50, 50)
        screen.blit(text, text_rect)

        # проверка на лобовое столкновение
        if pygame.sprite.spritecollide(player, vehicle_group, True):
            GAMEOVER = True
            crash_rect.center = [player.rect.center[0], player.rect.top]

        # экран "Конец Игры"
        if GAMEOVER:
            screen.blit(crash, crash_rect)

            pygame.draw.rect(screen, BUTTON_RED, (0, 275, WIDTH, 50))

            font = pygame.font.Font('fonts/Jura-Bold.ttf', 17)
            text = font.render('Конец игры', True, WHITE)
            text_rect = text.get_rect()
            text_rect.center = (WIDTH / 2, 300)
            screen.blit(text, text_rect)
            button_shadow = MenuShadow(300, 55, BUTTON_RED_SHADOW).draw(125, 400)  # создание тени кнопки
            button = Menu(300, 50, BUTTON_RED).draw(125, 400, 'Рестарт')  # создание кнопки

        pygame.display.update()

        # ожидание,когда пользователь нажмет кнопку "Рестарт"
        while GAMEOVER:

            CLOCK.tick(FPS)

            for event in pygame.event.get():

                if event.type == QUIT:
                    GAMEOVER = False
                    running = False

                # получение нажатия кнопки Y
                elif event.type == pg.MOUSEBUTTONDOWN:
                    # получение позиции мышки
                    x_pos, y_pos = pg.mouse.get_pos()
                    if 125 < x_pos < 425 and 400 < y_pos < 450:
                        # перезапуск игры
                        GAMEOVER = False
                        SPEED = 2
                        SCORE = 0
                        vehicle_group.empty()
                        player.rect.center = [PLAYER_X, PLAYER_Y]
