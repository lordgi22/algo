import pygame
from random import randrange
pygame.init()
length = 1
game = True
FPS = 50
x = 350
y = 250
eda = 0

apple = randrange(20,300,50),randrange(20,300,50)


snake = [(x,y)]
direction = ''

okno = pygame.display.set_mode((1200,1000))
pygame.display.set_caption('Змейка')


time = pygame.time.Clock()

while game:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
    okno.fill((255,255,255)) 
    [(pygame.draw.rect(okno,(102,255,0),(x,y,40,40))) for x,y in snake]
    pygame.draw.rect(okno,(255,0,0),(*apple,40,40))
    f1 = pygame.font.Font(None, 36)
    text1 = f1.render(('Счёт: ' + str(eda)), True,(180, 0, 0))

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
    
    if x < 0:
        x = 1200
        #direction = 'left'
    if x > 1200:
        x = 0
        #rection = 'right'
    if y < 0:
        y = 1000
        #direction = 'ip'
    if y > 1000:
        y = 0
        #direction = 'down'

    if snake[-1] == apple:
        apple = randrange(20,300,50),randrange(20,300,50)
        length += 5
        eda += 1
    if snake[-1] == snake:
        game = False
    okno.blit(text1, (10, 20))
    pygame.display.update()
    time.tick(FPS)
