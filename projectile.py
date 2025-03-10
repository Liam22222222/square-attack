import pygame, sys, math

pygame.init()

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900
IMAGE_HIGHT = 128
IMAGE_WIDTH = 200
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
img = pygame.image.load('images/tank1.svg')
img = pygame.transform.scale(img, (IMAGE_WIDTH, IMAGE_HIGHT))

# Rotation Angle
angle = 0

# Set Balls initial position to the center of the screen
ball_pos = [0,0]
ball_speed = [2,2]
ball_dir = [0,0]

def clamp(fall,rise,input):
    if input < fall:
        input = fall
    if input > rise:
        input = rise
    return(input)

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
    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE]:
        ball_pos.append(img_pos[0])
        ball_pos.append(img_pos[1])
        ball_dir.append(angle-90)
        ball_dir.append(angle-90)
    key = pygame.key.get_pressed()
    if key[pygame.K_UP]:
        img_pos[0] -= img_speed[0]*clamp(-1,1,round(math.sin(angle-90)))
        img_pos[1] -= img_speed[1]*clamp(-1,1,round(math.cos(angle-90)))
    if key[pygame.K_DOWN]:
        img_pos[0] += img_speed[0]*clamp(-1,1,round(math.sin(angle-90)))
        img_pos[1] += img_speed[1]*clamp(-1,1,round(math.cos(angle-90)))
    if key[pygame.K_LEFT]:
        angle += img_speed[1]
    if key[pygame.K_RIGHT]:
        angle -= img_speed[1]
    if 360 < angle:
        angle = 0.0
    screen.fill(BACKGROUND_COLOR)
    screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width()//2, 100))   # Centering title in the screen
    i = 0
    while i < len(ball_pos):
        ball_pos[i] += 4 *math.sin(ball_dir[i])
        ball_pos[i+1] += 4 *math.cos(ball_dir[i + 1])
        pygame.draw.circle(screen, BALL_COLOR, (ball_pos[i], ball_pos[i+1]), BALL_RADIUS)
        i += 2

    rotated_img = rot_center(img, angle)
    screen.blit(rotated_img,(img_pos[0],img_pos[1]))
    pygame.display.update()
            