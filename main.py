import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Задаем размеры экрана игры

pygame.display.set_caption("Игра Тир") # Задаем название заголовка окна игры

icon = pygame.image.load("Images/Target_icon.png") # Прописываем путь к картинке
pygame.display.set_icon(icon) # Назначаем картинку в качестве иконки игры

target_image = pygame.image.load("Images/smaylik.png") # Прописываем путь к картинке мишени
target_width = 80 # Задаём ширину мишени
target_height = 80 # Задаём высоту мишени

# Задаём переменные для рандомных координат (х, у) мишени
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

# Задаем переменную рандомного цвета игрового фона
color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

running = True
while running:
    screen.fill(color) # Заливаем фон игры рандомным цветом
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos() # Проверка координат клика мышки на попадание в диапазон смайла-мишени
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                # Рандомное обновление координат смайлика-мишени
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
    screen.blit(target_image, (target_x, target_y)) # Отрисовка на экране смайлика-мишени
    pygame.display.update()


pygame.quit()