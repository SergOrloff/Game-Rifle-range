# Программа "Тир" на Python использует библиотеку Pygame для создания интерактивной игры,
# в которой игрок должен попадать по мишеням, которые случайным образом перемещаются по
# экрану. Игра также позволяет выбрать уровень сложности, который влияет на размер мишени.

import pygame
import random
import time
import tkinter as tk
from tkinter import simpledialog

# Инициализировать Pygame
pygame.init()

# Задаем начальные параметры
final_screen = True
running = True
difficulty = 'Normal'  # Значение по умолчанию

# Функция для выбора уровня сложности
def choose_difficulty():
    global difficulty
    root = tk.Tk()
    root.withdraw()  # Скрыть основное окно

    difficulty = simpledialog.askstring("Выбор уровня сложности",
                                        "Введите уровень сложности (Легкий, Нормальный, Сложный):",
                                        initialvalue="Нормальный")

    root.destroy()

# Вызов функции выбора уровня сложности
choose_difficulty()

# Настройки экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('Rifle-range game')
icon = pygame.image.load('img/image.jpg')
pygame.display.set_icon(icon)

# Загрузите целевое изображение и задайте размеры
target_img = pygame.image.load('img/target.png')
target_width = 50
target_height = 50

# Загрузите звуковые эффекты
hit_sound = pygame.mixer.Sound('sound/hit.wav')
end_sound = pygame.mixer.Sound('sound/end.wav')

# Функция для получения случайной позиции для объекта
def get_random_position():
    return random.randint(0, SCREEN_WIDTH - target_width), random.randint(0, SCREEN_HEIGHT - target_height)

# Функция для получения случайного цвета
def get_random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Функция для отображения текста на экране
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# Начальная позиция цели и цвет
target_x, target_y = get_random_position()
color = get_random_color()

# Счетчик очков
score = 0

# Ограничение по времени
time_limit = 30  # Секунды
start_time = time.time()

# Уровень сложности
# difficulty = get_difficulty_level()

# Запуск основного игрового цикла
while running:
    current_time = time.time()
    elapsed_time = current_time - start_time
    remaining_time = max(0, time_limit - elapsed_time)

    if remaining_time == 0:
        running = False  # Игра заканчивается, когда время истекает

    # Изменение размера мишени в зависимости от уровня сложности
    if difficulty == 'Легкий':
        target_width = target_height = 50
    elif difficulty == 'Нормальный':
        target_width = target_height = 35
    elif difficulty == 'Сложный':
        target_width = target_height = 25

    screen.fill(color)  # Заполните экран текущим фоном цвета

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # Проверьте, находится ли щелчок мыши в пределах целевой области
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_x, target_y = get_random_position()  # Переместите цель в новую случайную позицию
                color = get_random_color()  # Изменить цвет фона
                score += 1  # Увеличение счета
                hit_sound.play()  # Проиграть звук попадания

    # Нарисуйте цель на экране в новом положении
    screen.blit(pygame.transform.scale(target_img, (target_width, target_height)), (target_x, target_y))

    # Отображение оставшегося времени и счета
    font = pygame.font.Font(None, 36)
    draw_text(f'Time: {int(remaining_time)}', font, (255, 255, 255), screen, 10, 10)
    draw_text(f'Score: {score}', font, (255, 255, 255), screen, 10, 50)

    pygame.display.flip()

# Финальный экран
end_sound.play()  # Проиграть звук окончания игры
screen.fill((0, 0, 0))  # Заполните экран черным цветом
draw_text(f'Игра окончена! Число попаданий: {score}', font, (255, 255, 255), screen, SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 20)
pygame.display.flip()

# Подождите несколько секунд, показывая финальный экран
time.sleep(5)

pygame.quit()
