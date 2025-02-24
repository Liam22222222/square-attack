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
boxs = []
boxpos = []
endx = random.randint(width - 900,width - 400)
endy = random.randint(hight - 850, hight - 100)
numbox = level
joydist = 0.0
i = 0
a = 0
size = 100
objs = 0.0
objpos = 0.0

class plyer:
    def __init__(self,s,x,y,xs,ys):
        self.s = s
        self.x = x
        self.y = y
        self.xs = xs
        self.ys = ys

ply = plyer(pygame.Rect(60,60,60,60),0.0,0.0,0.0,0.0)

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
        ply.xs = -5
    if key[pygame.K_RIGHT]:
        ply.xs = 5
    if key[pygame.K_DOWN]:
        ply.ys = 5
    if key[pygame.K_UP]:
        ply.ys = -5
        
    joydist = math.sqrt((ply.xs * ply.xs) + (ply.ys * ply.ys))
    if joydist > 5:
        ply.xs = ply.xs * 0.99
        ply.ys = ply.ys * 0.99
    ply.xs += ply.xs * -0.1
    ply.ys += ply.ys * -0.1
    ply.x += ply.xs
    ply.y += ply.ys
    
    if ply.x > width + 100:
        ply.x = width + 100
        ply.xs = 0.0
    if ply.x < -100:
        ply.x = -100
        ply.xs = 0.0
    if ply.y > hight - 50:
        ply.y = hight - 50
        ply.ys = 0.0
    if ply.y < -100:
        ply.y = -100
        ply.ys = 0.0
    
    point = ply.s.collidepoint(endx,endy)
    if point:
        boxs = []
        boxpos = []
        endx = random.randint(width - 900,width - 400)
        endy = random.randint(hight - 850, hight - 100)
        level += 1
        numbox = level
        joydist = 0.0
        i = 0
        a = 0
        size = 100
        objs = 0.0
        objpos = 0.0
        ply = plyer(pygame.Rect(60,60,60,60),0.0,0.0,0.0,0.0)
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

        if ply.x - 180 > boxpos[i]:
            boxpos[i] += random.randint(0,5)
        if ply.y - 180 > boxpos[i + 1]:
            boxpos[i + 1] += random.randint(0,5)
        if ply.x - 180 < boxpos[i]:
            boxpos[i] += random.randint(-5,0)
        if ply.y - 180 < boxpos[i + 1]:
            boxpos[i + 1] += random.randint(-5,0)

        if boxpos[i] > width + 100:
            boxpos[i] = width + 100
        if boxpos[i] < -10:
            boxpos[i] = -10
        if boxpos[i + 1] > hight - 50:
            boxpos[i + 1] = hight - 50
        if boxpos[i + 1] < -100:
            boxpos[i + 1] = -100
        i += 2

    screen.fill((127,127,127))
    pygame.draw.circle(screen,(0,255,0),(endx,endy),60)
    ply.s.move_ip(ply.xs,ply.ys)
    pygame.draw.rect(screen, (255,0,0), ply.s)
    i = 0
    a = 0
    while i < len(boxs):
        objs = pygame.Rect(boxs[i], boxs[i + 1], boxs[i + 2], boxs[i + 3])
        objs.move_ip(boxpos[a], boxpos[a + 1])
        pygame.draw.rect(screen, (0,0,0), objs)
        point = objs.collidepoint(ply.x,ply.y)
        if point:
            ply = plyer(pygame.Rect(60,60,60,60),0.0,0.0,0.0,0.0)
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
        