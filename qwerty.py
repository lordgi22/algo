import pygame
from random import *
pygame.init()
length = 1
game = True
FPS = 50
x = 350
y = 250

x2 = randint(0,700)
y2 = randint(0,500)
apple = x2,y2

snake = [(x,y)]
direction = ''

okno = pygame.display.set_mode((700,500))
pygame.display.set_caption('Змейка')


time = pygame.time.Clock()

while game:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
    okno.fill((255,255,255)) 
    [(pygame.draw.rect(okno,(102,255,0),(x,y,30,30))) for x,y in snake]
    pygame.draw.rect(okno,(255,0,0),(x2,y2,20,20))

    snake.append((x,y))
    snake = snake[-length:]
    #движение
    keys = pygame.key.get_pressed()
    if keys[pygame.K_s]:
        direction = 'down'
    if keys[pygame.K_d]:
        direction = 'right'
    if keys[pygame.K_a]:
        direction = 'left'
    if keys[pygame.K_w]:
        direction = 'up'


    if direction == 'up':
        y -= 5
    if direction == 'down':
        y += 5 
    if direction == 'right':
        x += 5
    if direction == 'left':
        x -= 5

    if keys[pygame.K_q]:
        game = False
    
    if snake == x2 and  snake == y2:
        pygame.draw.rect(okno,(255,0,0),(x2,y2,20,20))
        length += 1

    pygame.display.update()
    time.tick(FPS)
