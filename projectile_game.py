import pygame, sys, math
import Projectile

pygame.init()

SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 700
IMAGE_WIDTH = 100
BALL_RADIUS = 10

# Colors
BACKGROUND_COLOR = (221,234,243)
BALL_COLOR = (111,204,227)
FONT_COLOR = (43,102,158)

# Game Setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Drawing an image and Rotating")

# Fonts
font = pygame.font.SysFont("Arial", 32)
text = font.render("Projectile", True, FONT_COLOR)

# Set up image
img_pos = [SCREEN_WIDTH//2, SCREEN_HEIGHT//2]
img_speed = [2,2]
img = pygame.image.load('images/star.png')
img = pygame.transform.scale(img, (IMAGE_WIDTH, IMAGE_WIDTH))

# Rotation Angle
angle = 0

# Projectile Speed
projectile_speed = 4

# Set Balls initial position to the center of the screen
ball_pos = [SCREEN_WIDTH//2, SCREEN_HEIGHT//2]
ball_speed = [2,2]

# Clock Speed
clock = pygame.time.Clock()
fps = 120

# Projectile List
projectiles = []


def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image

projectile = False
x = SCREEN_WIDTH//2
y = SCREEN_HEIGHT//2

# Game Loop
while True:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            key = pygame.key.name(event.key)
            projectile = True
            projectile_angle = angle
    


    screen.fill(BACKGROUND_COLOR)
    screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width()//2, 100))   # Centering title in the screen

    if projectile:
        x += projectile_speed *math.sin(projectile_angle)
        y += projectile_speed *math.cos(projectile_angle)
        pygame.draw.circle(screen, BALL_COLOR, (x, y), BALL_RADIUS)

    angle += 1
    rotated_img = rot_center(img, angle)
    screen.blit(rotated_img,(SCREEN_WIDTH//2,SCREEN_HEIGHT//2))
    pygame.display.update()
            