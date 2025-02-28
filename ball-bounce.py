import pygame, sys

pygame.init()

SCREEN_WIDTH = 2500
SCREEN_HEIGHT = 1600
BALL_RADIUS = 60

# Colors
BACKGROUND_COLOR = (221,234,243)
BALL_COLOR = (111,204,227)
FONT_COLOR = (43,102,158)

# Game Setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Bouncing a Ball")

# Fonts
font = pygame.font.SysFont("Arial", 64)
text = font.render("Let's Bounce", True, FONT_COLOR)

# Set Balls initial position to the center of the screen
ball_pos = [SCREEN_WIDTH//2, SCREEN_HEIGHT//2]
ball_speed = [2,2]

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # move the ball based on the speed
    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    #bounce off of the walls
    if ball_pos[0] <= BALL_RADIUS or ball_pos[0] >= SCREEN_WIDTH- BALL_RADIUS:
        ball_speed[0] = -ball_speed[0]

    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= SCREEN_HEIGHT - BALL_RADIUS:
        ball_speed[1] = - ball_speed[1]

    screen.fill(BACKGROUND_COLOR)
    screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width()//2, 100))   # Centering title in the screen
    pygame.draw.circle(screen, BALL_COLOR, (ball_pos[0], ball_pos[1]), BALL_RADIUS)
    pygame.display.update()
            