
import pygame
import random
import time

pygame.init()
pygame.mixer.init()

sound = pygame.mixer.Sound("Sounds/ooops.mp3")

# Добавление звуковых файлов
sound_game_won = pygame.mixer.Sound("Sounds/GameWon.mp3")
sound_game_lost = pygame.mixer.Sound("Sounds/GameLost.mp3")
sound_game_finished = pygame.mixer.Sound("Sounds/GameFinished.mp3")

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('Игра "Убегающий колобок"')

icon = pygame.image.load("Images/Target_icon.png")
pygame.display.set_icon(icon)

target_image = pygame.image.load("Images/smaylik.png")
target_clicked_image = pygame.image.load("Images/smaylikIn.png")

target_width = 80
target_height = 80

MOVE_TARGET = pygame.USEREVENT + 1
pygame.time.set_timer(MOVE_TARGET, 900)

font = pygame.font.Font(None, 36)

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

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
                pygame.quit()
                quit()
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
                        time.sleep(0.8)
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

            button = pygame.image.load("Images/ContinueButton.png")
            stop_button = pygame.image.load("Images/StopButton.png")

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
                        pygame.quit()
                        quit()

game_loop()
pygame.quit()