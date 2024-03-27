import pygame
import random
import time

pygame.init()

# Инициализируем mixer для воспроизведения звуков
pygame.mixer.init()

# Загружаем звуковой файл
sound = pygame.mixer.Sound("Sounds/ooops.mp3")

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра Тир")

icon = pygame.image.load("Images/Target_icon.png")
pygame.display.set_icon(icon)

target_image = pygame.image.load("Images/smaylik.png")
target_clicked_image = pygame.image.load("Images/smaylikIn.png")

target_width = 80
target_height = 80

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                screen.blit(target_clicked_image, (target_x, target_y))
                pygame.display.update()
                sound.play()  # Воспроизводим звук при попадании по изображению
                time.sleep(0.3)

                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
    screen.blit(target_image, (target_x, target_y))
    pygame.display.update()

pygame.quit()