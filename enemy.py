from pygame.locals import *
import pygame
import math
from tank import Tank
from random import randrange

#constants
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900
ENEMY_SPEED = 5
ENEMY_SIZE = 8
TANK_WIDTH = 200
TANK_HEIGHT = 128

#var
i = 0
e = []
dist = 0

# Now we are randomly placing the enemies
class Enemy:
    def __init__(self):
        """Initializes the enemys."""
        x = randrange(SCREEN_WIDTH)
        y = randrange(SCREEN_HEIGHT)
        self.position = pygame.Vector2(x, y)
        self.angle = math.radians(randrange(0, 360))
        self.speed = ENEMY_SPEED

    def update(self,tankx,tanky,tankd):
        """Moves the enemy."""

        ox = tankx - self.position.x + 0.000001
        oy = tanky - self.position.y + 0.000001
        on = 0
        if tankx < self.position.x:
            on = 180
        self.angle = (math.atan(oy/ox)) + on

        tankw = (TANK_WIDTH * math.cos(math.radians(tankd))) / 2
        tankh = (TANK_HEIGHT * math.sin(math.radians(tankd))) / 2

        self.position.x += self.speed * math.cos(self.angle)
        self.position.y += self.speed * math.sin(self.angle)

        point = pygame.Rect(ENEMY_SIZE,ENEMY_SIZE,self.position.x,self.position.y)
        point = point.collidepoint(tankx + tankw,tanky + tankh)
        if not point:
            point = pygame.Rect(ENEMY_SIZE,ENEMY_SIZE,self.position.x,self.position.y)
            point = point.collidepoint(tankx - tankw,tanky - tankh)
            if not point:
                point = pygame.Rect(ENEMY_SIZE,ENEMY_SIZE,self.position.x,self.position.y)
                point = point.collidepoint(tankx - tankw,tanky + tankh)
                if not point:
                    point = pygame.Rect(ENEMY_SIZE,ENEMY_SIZE,self.position.x,self.position.y)
                    point = point.collidepoint(tankx + tankw,tanky - tankh)
                else:
                    self.position.x -= self.speed * math.cos(self.angle)
                    self.position.y -= self.speed * math.sin(self.angle)
            else:
                self.position.x -= self.speed * math.cos(self.angle)
                self.position.y -= self.speed * math.sin(self.angle)
        else:
            self.position.x -= self.speed * math.cos(self.angle)
            self.position.y -= self.speed * math.sin(self.angle)

    def get_tank(self,tankx,tanky,tankd):
        """checks if touching tank."""

        tankw = (TANK_WIDTH * math.sin(math.radians(tankd))) // 2
        tankh = (TANK_HEIGHT * math.cos(math.radians(tankd))) // 2

        point = pygame.Rect(ENEMY_SIZE,ENEMY_SIZE,self.position.x,self.position.y)
        point = point.collidepoint(tankx + tankw,tanky + tankh)
        if not point:
            point = pygame.Rect(ENEMY_SIZE,ENEMY_SIZE,self.position.x,self.position.y)
            point = point.collidepoint(tankx - tankw,tanky - tankh)
            if not point:
                point = pygame.Rect(ENEMY_SIZE,ENEMY_SIZE,self.position.x,self.position.y)
                point = point.collidepoint(tankx - tankw,tanky + tankh)
                if not point:
                    point = pygame.Rect(ENEMY_SIZE,ENEMY_SIZE,self.position.x,self.position.y)
                    point = point.collidepoint(tankx + tankw,tanky - tankh)

        return(point)
            
        
    def draw(self, surface):
        """Draws the enemy as a small circle."""
        pygame.draw.circle(surface, (0, 0, 0), (int(self.position.x), int(self.position.y)), ENEMY_SIZE)

    def is_off_screen(self):
        """Check if the enemy is off the screen."""
        return not (0 <= self.position.x <= SCREEN_WIDTH and 0 <= self.position.y <= SCREEN_HEIGHT)
    
    def is_shot(self,x,y):
        """checks if enemy has been hit"""
        point = pygame.Rect(self.position).collidepoint(x,y)
        return (point) 
    
    