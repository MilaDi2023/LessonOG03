import pygame
import random
import time

import sys
import os
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)



pygame.init()
pygame.mixer.init()

# Загрузка звука для начала игры
start_sound = pygame.mixer.Sound(resource_path("Sounds/StartGame.mp3"))
sound = pygame.mixer.Sound(resource_path("Sounds/ooops.mp3"))

# Добавление звуковых файлов
sound_game_won = pygame.mixer.Sound(resource_path("Sounds/GameWon.mp3"))
sound_game_lost = pygame.mixer.Sound(resource_path("Sounds/GameLost.mp3"))
sound_game_lost.set_volume(0.5) # 50% громкости
sound_game_finished = pygame.mixer.Sound(resource_path("Sounds/GameFinished.mp3"))

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('Игра "Убегающий колобок"')

icon = pygame.image.load(resource_path("Images/Target_icon.png"))
pygame.display.set_icon(icon)

target_image = pygame.image.load(resource_path("Images/smaylik.png"))
target_clicked_image = pygame.image.load(resource_path("Images/smaylikIn.png"))

start_button = pygame.image.load(resource_path("Images/StartButton.png"))
background_image = pygame.image.load(resource_path("Images/BackgroundImage.png"))

target_width = 80
target_height = 80

MOVE_TARGET = pygame.USEREVENT + 1
pygame.time.set_timer(MOVE_TARGET, 700) # Тут меняем временнОй интервал, через который колобок убегает в другую точку экрана

font = pygame.font.Font(None, 36)

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Инициализация изображений кнопки
start_button = pygame.image.load(resource_path("Images/StartButton.png"))
start_button_large = pygame.transform.scale(start_button, (int(start_button.get_width() * 1.1),
                                                           int(start_button.get_height() * 1.1)))



# функция отображения начального экрана игры
def display_start_screen():
    start_sound.play()  # проигрывание звука начала игры
    screen.blit(background_image, (0, 0))  # загрузка фонового изображения

    # отображение приветственного текста
    welcome_lines = [" ",
                     " ",
                     " ",
                     " ",
                     " ",
                     " "]
    welcome_texts = [font.render(line, True, (249, 194, 33)) for line in welcome_lines]

    # Установка начальной точки для вертикального позиционирования первой строки приветственного текста
    vert_start = SCREEN_HEIGHT // 2 - 175

    # Вывод каждого ряда текста по центру, добавляя перерывы между строками
    for i, welcome_text in enumerate(welcome_texts):
        screen.blit(welcome_text,
                    (SCREEN_WIDTH // 2 - welcome_text.get_width() // 2, vert_start + i * (font.get_linesize() + 5))
                    )
    # Установка положения кнопки "Начать игру"
    start_button_x = (SCREEN_WIDTH // 2) - start_button.get_width() // 2
    start_button_y = vert_start + len(welcome_texts) * (font.get_linesize() + 5) + 130

    pygame.display.flip()

    # цикл ожидания нажатия на кнопку "Начать игру"
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if (start_button_x < mouse_x < start_button_x + start_button_large.get_width()) and \
                        (start_button_y < mouse_y < start_button_y + start_button_large.get_height()):
                    start_sound.stop()  # остановка звука начала игры
                    game_loop()  # запуск игрового цикла
                    return
            if event.type == pygame.QUIT:
                sys.exit()
                sys.exit()

        # очистить экран перед отрисовкой кнопки
        screen.fill((0, 0, 0))
        screen.blit(background_image, (0, 0))  # загрузка фонового изображения

        # отображение приветственного текста
        for i, welcome_text in enumerate(welcome_texts):
            screen.blit(welcome_text,
                        (SCREEN_WIDTH // 2 - welcome_text.get_width() // 2, vert_start + i * (font.get_linesize() + 5))
                        )

        # Рисовать кнопку, увеличивая её при наведении
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if (start_button_x < mouse_x < start_button_x + start_button_large.get_width()) and \
                (start_button_y < mouse_y < start_button_y + start_button_large.get_height()):
            current_button = start_button_large
            button_x = start_button_x - (start_button_large.get_width() - start_button.get_width()) // 2
        else:
            current_button = start_button
            button_x = start_button_x

        screen.blit(current_button, (button_x, start_button_y))
        pygame.display.flip()

def game_loop():
    global target_x, target_y
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    start_ticks = pygame.time.get_ticks()
    user_score = 0
    smiley_score = 0
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                sys.exit()
            if event.type == MOVE_TARGET:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
            if event.type == pygame.MOUSEBUTTONDOWN:
                seconds = (pygame.time.get_ticks() - start_ticks) / 1000
                if seconds < 30:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                        screen.blit(target_clicked_image, (target_x, target_y))
                        pygame.display.update()
                        sound.play()
                        user_score += 1
                        time.sleep(0.7)
                    else:
                        smiley_score += 1
        screen.fill(color)
        seconds = (pygame.time.get_ticks() - start_ticks) / 1000
        if seconds < 30:
            screen.blit(target_image, (target_x, target_y))
        elif seconds >= 30:
            running = False
            if user_score > smiley_score:
                winner_text = font.render('Победил Охотник!', True, (0, 0, 0))
                screen.blit(winner_text, (SCREEN_WIDTH // 2 - winner_text.get_width() // 2, SCREEN_HEIGHT // 2 - winner_text.get_height() // 2 - 150))
                sound_game_won.play() # проигрывание звука при победе пользователя
            elif user_score < smiley_score:
                winner_text = font.render('Победил Колобок!', True, (0, 0, 0))
                screen.blit(winner_text, (SCREEN_WIDTH // 2 - winner_text.get_width() // 2, SCREEN_HEIGHT // 2 - winner_text.get_height() // 2 - 150))
                sound_game_lost.play() # проигрывание звука при проигрыше пользователя
            else:
                winner_text = font.render('Ничья!', True, (0, 0, 0))
                screen.blit(winner_text, (SCREEN_WIDTH // 2 - winner_text.get_width() // 2, SCREEN_HEIGHT // 2 - winner_text.get_height() // 2 - 150))
                sound_game_finished.play() # проигрывание звука при ничьей

            button = pygame.image.load(resource_path("Images/ContinueButton.png"))
            stop_button = pygame.image.load(resource_path("Images/StopButton.png"))

            buttons_gap = 80
            button_x = (SCREEN_WIDTH // 2) - button.get_width() - buttons_gap // 2
            button_y = (SCREEN_HEIGHT // 2) - button.get_height() // 2

            stop_button_x = (SCREEN_WIDTH // 2) + buttons_gap // 2
            stop_button_y = button_y

            screen.blit(button, (button_x, button_y))
            screen.blit(stop_button, (stop_button_x, stop_button_y))
        user_versus_smiley = font.render("Колобок против Охотника", True, (0, 0, 0))
        screen.blit(user_versus_smiley, ((SCREEN_WIDTH - user_versus_smiley.get_rect().width) // 2, 10))
        score_text = font.render("{0}:{1}".format(smiley_score, user_score), True, (0, 0, 0))
        screen.blit(score_text, ((SCREEN_WIDTH - score_text.get_rect().width) // 2, 60))
        pygame.display.flip()

        while not running:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if (button_x < mouse_x < button_x + button.get_width()) and (
                            button_y < mouse_y < button_y + button.get_height()):
                        game_loop()
                    elif (stop_button_x < mouse_x < stop_button_x + stop_button.get_width()) and (
                            stop_button_y < mouse_y < stop_button_y + stop_button.get_height()):
                        sys.exit()
                        sys.exit()


display_start_screen()
pygame.sys.exit()