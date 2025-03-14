from pygame.locals import *
import pygame
import math

# Constants
IMAGE_WIDTH = 200
IMAGE_HEIGHT = 128
PROJECTILE_RADIUS = 5
PROJECTILE_SPEED = 3
TURNING_SPEED = 1
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900
ENEMY_SPEED = 5
ENEMY_SIZE = 8

#var
i = 0
e = []
dist = 0

class Tank:
    def __init__(self, x, y, speed, image_path):
        self.position = pygame.Vector2(x, y)
        self.speed = speed
        self.angle = 0  # Angle in degrees
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (IMAGE_WIDTH, IMAGE_HEIGHT))
        self.barrel_offset = 100  # Distance from center to projectile launcher
        self.barrel_side_offset = 40  # Horizontal offset for left/right of the tank

    def rotate(self, direction):
        """Rotates the tank left (-1) or right (+1)."""
        self.angle += direction * TURNING_SPEED  # Increase rotation speed

    def move(self, forward=True):
        """Moves the tank in the direction it's facing."""
        angle_radians = math.radians(self.angle)
        direction = 1 if forward else -1
        self.position.x += direction * self.speed * math.cos(angle_radians)
        self.position.y += direction * self.speed * math.sin(angle_radians)
        

    def draw(self, surface):
        """Rotates and draws the tank on the screen."""
        rotated_image = pygame.transform.rotate(self.image, -self.angle)  # Fix rotation direction
        rect = rotated_image.get_rect(center=self.position)
        surface.blit(rotated_image, rect.topleft)

    def fire_projectile(self):
        """Creates a new projectile fired from the barrel position."""
        angle_radians = math.radians(self.angle)

        # Calculate barrel's forward position (barrel offset).
        barrel_x = self.position.x + self.barrel_offset * math.cos(angle_radians)
        barrel_y = self.position.y + self.barrel_offset * math.sin(angle_radians)

        # Calculate barrel's lateral position (left/right offset).
        barrel_x += self.barrel_side_offset * math.sin(angle_radians)  # Left or right offset
        barrel_y -= self.barrel_side_offset * math.cos(angle_radians)  # Left or right offset

        return Projectile(barrel_x, barrel_y, self.angle)


class Projectile:
    def __init__(self, x, y, angle):
        """Initializes the projectile."""
        self.position = pygame.Vector2(x, y)
        self.angle = math.radians(angle)
        self.speed = PROJECTILE_SPEED

    def update(self):
        """Moves the projectile in the direction it was fired."""
        self.position.x += self.speed * math.cos(self.angle)
        self.position.y += self.speed * math.sin(self.angle)

    def draw(self, surface):
        """Draws the projectile as a small circle."""
        pygame.draw.circle(surface, (255, 0, 0), (int(self.position.x), int(self.position.y)), PROJECTILE_RADIUS)

    def is_off_screen(self):
        """Check if the projectile is off the screen."""
        return not (0 <= self.position.x <= SCREEN_WIDTH and 0 <= self.position.y <= SCREEN_HEIGHT)
    

