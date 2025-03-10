import pygame, sys, math

pygame.init()

SCREEN_WIDTH = 2500
SCREEN_HEIGHT = 1600
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

# Set Balls initial position to the center of the screen
ball_pos = [SCREEN_WIDTH//2, SCREEN_HEIGHT//2]
ball_speed = [2,2]

def rot_center(image, angle):
    """rotate a Surface, maintaining position."""
    
    loc = image.get_rect().center  #rot_image is not defined 
    rot_sprite = pygame.transform.rotate(image, angle)
    rot_sprite.get_rect().center = loc
    return rot_sprite

projectile = False
x = SCREEN_WIDTH//2
y = SCREEN_HEIGHT//2

# Game Loop
while True:
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
        x += 4 *math.sin(projectile_angle)
        y += 4 *math.cos(projectile_angle)
        pygame.draw.circle(screen, BALL_COLOR, (x, y), BALL_RADIUS)

    angle += 1
    rotated_img = rot_center(img, angle)
    screen.blit(rotated_img,(SCREEN_WIDTH//2,SCREEN_HEIGHT//2))
    pygame.display.update()
            