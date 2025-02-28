import pygame, sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
IMAGE_WIDTH = 100

# Colors
BACKGROUND_COLOR = (221,234,243)
BALL_COLOR = (111,204,227)
FONT_COLOR = (43,102,158)

# Game Setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Drawing an image and Rotating")

# Fonts
font = pygame.font.SysFont("Arial", 32)
text = font.render("Rotation", True, FONT_COLOR)

# Set up image
img_pos = [SCREEN_WIDTH//2, SCREEN_HEIGHT//2]
img_speed = [2,2]
img = pygame.image.load('images/star.png')
img = pygame.transform.scale(img, (IMAGE_WIDTH, IMAGE_WIDTH))

# Rotation Angle
angle = 0

def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    


    screen.fill(BACKGROUND_COLOR)
    screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width()//2, 100))   # Centering title in the screen

    angle += 1
    rotated_img = rot_center(img, angle)
    screen.blit(rotated_img,(SCREEN_WIDTH//2,SCREEN_HEIGHT//2))
    pygame.display.update()
            