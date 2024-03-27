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

# Задаём переменную для рандомного цвета фона
color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

running = True
while running:
    pass

pygame.quit()