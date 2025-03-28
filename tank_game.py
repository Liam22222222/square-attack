import pygame
import sys
from tank import Tank, Projectile
from enemy import Enemy


# Constants
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900
BACKGROUND_COLOR = (221, 234, 243)
FPS = 60

# Setup Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tank Game")
i = 0
en3 = 6

# Tank setup
tank = Tank(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 3, 'images/tank1.svg')  # Provide path to tank image
projectiles = []
health = 100

# Enemy setup
enemys = []
dam = 0.00002
while i < en3:
    enemys.append(Enemy())  #makes some at some points
    i += 1

# Game loop
clock = pygame.time.Clock()
while True:
    screen.fill(BACKGROUND_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        tank.rotate(-1)  # Rotate left
    if keys[pygame.K_RIGHT]:
        tank.rotate(1)  # Rotate right
    if keys[pygame.K_UP]:
        tank.move(forward=True)  # Move forward
    if keys[pygame.K_DOWN]:
        tank.move(forward=False)  # Move backward
    if keys[pygame.K_SPACE]:
        projectiles.append(tank.fire_projectile())  # Fire projectile

     # Update enemys
    for enemy in enemys[:]:
        enemy.update(tank.position.x,tank.position.y,tank.angle)
        if enemy.get_tank(tank.position.x,tank.position.y,tank.angle):
            health -= dam
            print(health)
        if enemy.is_off_screen():
            enemys.remove(enemy)  # Remove enemys that go off-screen
        enemy.draw(screen)

    # Update projectiles
    for projectile in projectiles[:]:
        projectile.update()
        if projectile.is_off_screen():
            projectiles.remove(projectile)  # Remove projectiles that go off-screen
        projectile.draw(screen)

   

    # Draw the tank
    tank.draw(screen)

    pygame.display.update()
    clock.tick(FPS)
