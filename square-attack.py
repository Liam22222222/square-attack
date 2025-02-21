from pygame.locals import *
import pygame, sys
import sys
import random
import math

pygame.init()
pygame.font.init()
width = 1600
hight = 900
screen = pygame.display.set_mode((width,hight))
pygame.display.set_caption("Liams game")

point = False
score = 0
text = ""
time = 5
level = 1
lives = 15
font = pygame.font.SysFont('Comic Sans MS', 60)
ply = pygame.Rect(60,60,60,60)
boxs = []
boxpos = []
# make these numbers a fraction of width and height, make width and height constants
# https://stackoverflow.com/questions/2682745/how-do-i-create-a-constant-in-python
endx = random.randint(700,1200)
endy = random.randint(50, 800)
numbox = level
joydist = 0.0
i = 0
a = 0

# make a class for a position that holds x, y, size
# https://www.w3schools.com/python/python_classes.asp
size = 100
objs = 0.0
objpos = 0.0
plyx = 0.0
plyy = 0.0
plyxs = 0.0
plyys = 0.0
dir = 0.0
while i < numbox:
    size = random.randint(100,150)
    boxs.append(size)
    boxs.append(size)
    boxs.append(size)
    boxs.append(size)
    boxpos.append(random.randint(-10,1000))
    boxpos.append(random.randint(-10,500))
    i += 1
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        plyxs = -5
    if key[pygame.K_RIGHT]:
        plyxs = 5
    if key[pygame.K_DOWN]:
        plyys = 5
    if key[pygame.K_UP]:
        plyys = -5
        
    joydist = math.sqrt((plyxs * plyxs) + (plyys * plyys))
    if joydist > 5:
        plyxs = plyxs * 0.99
        plyys = plyys * 0.99
    plyxs += plyxs * -0.1
    plyys += plyys * -0.1
    plyx += plyxs
    plyy += plyys
    
    # refer to width
    if plyx > 1700:
        plyx = 1700
        plyxs = 0.0
    if plyx < -100:
        plyx = -100
        plyxs = 0.0
    if plyy > 850:
        plyy = 850
        plyys = 0.0
    if plyy < -100:
        plyy = -100
        plyys = 0.0
    
    point = ply.collidepoint(endx,endy)
    if point:
        ply = pygame.Rect(60,60,60,60)
        boxs = []
        boxpos = []
        endx = random.randint(700,1200)
        endy = random.randint(50, 800)
        level += 1
        numbox = level
        joydist = 0.0
        i = 0
        a = 0
        size = 100
        objs = 0.0
        objpos = 0.0
        plyx = 0.0
        plyy = 0.0
        plyxs = 0.0
        plyys = 0.0
        score += math.ceil(time)
        time = 5
        while i < numbox:
            size = random.randint(100,150)
            boxs.append(size)
            boxs.append(size)
            boxs.append(size)
            boxs.append(size)
            boxpos.append(random.randint(-10,1000))
            boxpos.append(random.randint(-10,500))
            i += 1

    
        
    i = 0
    a = 0
    
    while i < len(boxpos):

        if plyx - 180 > boxpos[i]:
            boxpos[i] += random.randint(0,5)
        if plyy - 180 > boxpos[i + 1]:
            boxpos[i + 1] += random.randint(0,5)
        if plyx - 180 < boxpos[i]:
            boxpos[i] += random.randint(-5,0)
        if plyy - 180 < boxpos[i + 1]:
            boxpos[i + 1] += random.randint(-5,0)

        if boxpos[i] > 1700:
            boxpos[i] = 1700
        if boxpos[i] < -10:
            boxpos[i] = -10
        if boxpos[i + 1] > 850:
            boxpos[i + 1] = 850
        if boxpos[i + 1] < -100:
            boxpos[i + 1] = -100
        i += 2

    screen.fill((127,127,127))
    pygame.draw.circle(screen,(0,255,0),(endx,endy),60)
    ply.move_ip(plyxs,plyys)
    pygame.draw.rect(screen, (255,0,0), ply)
    i = 0
    a = 0
    while i < len(boxs):
        objs = pygame.Rect(boxs[i], boxs[i + 1], boxs[i + 2], boxs[i + 3])
        objs.move_ip(boxpos[a], boxpos[a + 1])
        pygame.draw.rect(screen, (0,0,0), objs)
        point = objs.collidepoint(plyx,plyy)
        if point:
            ply = pygame.Rect(60,60,60,60)
            plyx = 0.0
            plyy = 0.0
            plyxs = 0.0
            plyys = 0.0
            score += -1
        i += 4
        a += 2
    time += -0.005
    text = font.render(str(level), False, (0,0,0))
    screen.blit(text,(190,0))
    text = font.render(str(math.ceil(time)), False, (0,0,0))
    screen.blit(text,(100,0))
    text = font.render(str(score), False, (0,0,0))
    screen.blit(text,(10,0))
    pygame.display.update()
        