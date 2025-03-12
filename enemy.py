from pygame.locals import *
import pygame
import math

#constants
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900
ENEMY_SPEED = 5
ENEMY_SIZE = 8

#var
i = 0
e = []
dist = 0


class Enemy:
    def __init__(self, x, y, angle):
        """Initializes the enemys."""
        self.position = pygame.Vector2(x, y)
        self.angle = math.radians(angle)
        self.speed = ENEMY_SPEED

    def update(self):
        """Moves the enemy."""
        self.position.x += self.speed * math.cos(self.angle)
        self.position.y += self.speed * math.sin(self.angle)

    def draw(self, surface):
        """Draws the enemy as a small circle."""
        pygame.draw.circle(surface, (0, 0, 0), (int(self.position.x), int(self.position.y)), ENEMY_SIZE)

    def is_off_screen(self):
        """Check if the enemy is off the screen."""
        return not (0 <= self.position.x <= SCREEN_WIDTH and 0 <= self.position.y <= SCREEN_HEIGHT)
    
    def is_shot(self,x,y):
        """checks if enemy has been hit"""
        return (math.dist((self.position.x,self.position.y),(x,y))) 
    
    def spawn(x,y,a):
        """spawns an amount of enemys"""
        i = 0
        e = []
        while i < a:
            e.append(x)
            e.append(y)
            i += 1
        return (e)