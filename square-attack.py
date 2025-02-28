from pygame.locals import *
import pygame, sys
import random
import math
import time

pygame.init()
pygame.font.init()
width = 1600
hight = 900
screen = pygame.display.set_mode((width,hight))
pygame.display.set_caption("Liams game")

point = False
score = 0
text = ""
time1 = 5
level = 1
lives = 15
font = pygame.font.SysFont('Comic Sans MS', 60)
boxpos = []
endx = random.randint(200,width - 400)
endy = random.randint(60, hight - 100)
numbox = level
joydist = 0.0
i = 0
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

def add_cubes():
    i = 0
    while i < numbox:
        size = random.randint(100,150)
        boxpos.append(random.randint(500,1000))
        boxpos.append(random.randint(0,500))
        boxpos.append(size)
        boxpos.append(size)
        i += 1

add_cubes()

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
    ply.s = pygame.Rect(ply.x,ply.y,60,60)
    
    if ply.x > width - 300:
        ply.x = width - 300
        ply.xs = 0.0
    if ply.x < 0:
        ply.x = 0
        ply.xs = 0.0
    if ply.y > hight - 200:
        ply.y = hight - 200
        ply.ys = 0.0
    if ply.y < 0:
        ply.y = 0
        ply.ys = 0.0
    
    point = ply.s.collidepoint(endx,endy)
    if point:
        boxpos = []
        endx = random.randint(200,width - 400)
        endy = random.randint(60, hight - 100)
        level += 1
        numbox = level
        joydist = 0.0
        i = 0
        size = 100
        objs = 0.0
        objpos = 0.0
        ply = plyer(pygame.Rect(60,60,60,60),0.0,0.0,0.0,0.0)
        score += math.ceil(time1)
        time1 = 5
        add_cubes()

    i = 0
    
    while i < len(boxpos):

        if ply.x > boxpos[i]:
            boxpos[i] += random.randint(0,5)
        if ply.y > boxpos[i + 1]:
            boxpos[i + 1] += random.randint(0,5)
        if ply.x < boxpos[i]:
            boxpos[i] += random.randint(-5,0)
        if ply.y < boxpos[i + 1]:
            boxpos[i + 1] += random.randint(-5,0)

        if boxpos[i] > width - 300:
            boxpos[i] = width - 300
        if boxpos[i] < 150:
            boxpos[i] = 150
        if boxpos[i + 1] > hight - 200:
            boxpos[i + 1] = hight - 200
        if boxpos[i + 1] < 0:
            boxpos[i + 1] = 0
        i += 4

    screen.fill((127,127,127))
    pygame.draw.circle(screen,(0,255,0),(endx,endy),60)
    pygame.draw.rect(screen, (255,0,0), ply.s)
    i = 0
    while i < len(boxpos):
        objs = pygame.Rect(boxpos[i], boxpos[i + 1], boxpos[i + 2], boxpos[i + 3])
        pygame.draw.rect(screen, (0,0,0), objs)
        point = objs.collidepoint(ply.x,ply.y)
        if point:
            ply = plyer(pygame.Rect(60,60,60,60),0.0,0.0,0.0,0.0)
            score += -1
        i += 4

    time1 += -0.005

    if math.ceil(time1) <= -1:
        text = font.render("GAME OVER", False, (250,250,250))
        screen.blit(text,((width / 2) - 300,(hight / 2) - 200))

        text = font.render("SCORE:"+str(score), False, (250,250,250))
        screen.blit(text,((width / 2) - 300,(hight / 2) - 300))
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    text = font.render("level:"+str(level), False, (250,250,250))
    screen.blit(text,(600,0))

    text = font.render("time:"+str(math.ceil(time1)), False, (250,250,250))
    screen.blit(text,(300,0))

    text = font.render("score:"+str(score), False, (250,250,250))
    screen.blit(text,(10,0))

    pygame.display.update()