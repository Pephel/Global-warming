# -*- coding: utf8 -*-

import pygame
import random

# Инициализация библиотеки
pygame.init()

# Указываем размер окна
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Задаем название окна
pygame.display.set_caption("Global Warming")

# Загружаем изображение
background_image = pygame.image.load("background\sky1.jpg")

# Подгоняем масштаб под размер окна
background_image = pygame.transform.scale(background_image, (800, 800))

# Накладываем изображение на поверхность
screen.blit(background_image, (0, 0))

# Smoke object
smoke = pygame.image.load('smoke\smoke1.png')
object_width = 100
object_height = 100
smoke = pygame.transform.scale(smoke, (object_width, object_height))
smokeX = 0
smokeY = 800    
speed = 3

pygame.mixer.music.load('wind.mp3')
pygame.mixer.music.play(-1) 

s = pygame.mixer.Sound("smoke.mp3")
f = pygame.mixer.Sound("inf.mp3")
e = pygame.mixer.Sound("end.mp3")

objects = []
object_spawn_timer = 0

score = 0
screentime = 0
font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()
fail = 0
attemp = 1

while True:
    pygame.time.delay(5)
    screen.blit(background_image, (0, 0))
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Проверяем, нажали ли на дым
            for obj in objects:
                if obj[0] <= event.pos[0] <= obj[0] + object_width and obj[1] <= event.pos[1] <= obj[1] + object_height:
                    objects.remove(obj)
                    score+=1
                    speed+=0.5
                    object_spawn_timer = max(object_spawn_timer -30, 10)
                    s.play()

    if fail <= 15:
        if object_spawn_timer <= 0:
            objects.append([random.randint(0, screen_width - object_width), screen_height])
            object_spawn_timer = 100 

    for obj in objects:
        screen.blit(smoke, (obj[0], obj[1]))
        obj[1] -= speed

        if obj[1] <= 0:       
            fail += 1
            objects.remove(obj)             

    if fail > 3:
        if attemp == 1:
            background_image = pygame.image.load("background\sky2.jpg")
            f.play()             
            attemp += 1

    if fail > 6:
        if attemp == 2:
            background_image = pygame.image.load("background\sky3.jpg")
            f.play()
            attemp += 1

    if fail > 15:
        if attemp == 3:
            background_image = pygame.image.load("background\end.jpg")
            e.play()
            objects.clear() 
            pygame.mixer.music.stop() 
            attemp += 1 
 
         
    object_spawn_timer -= 1    
    
    pygame.display.update()   
    clock.tick(60)