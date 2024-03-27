import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Задаем размеры экрана игры

pygame.display.set_caption("Игра Тир") # Задаем название заголовка окна игры
icon = pygame.image.load("Images/Target_icon.png") # Прописываем путь к иконке




running = True
while running:
    pass

pygame.quit()