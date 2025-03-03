import pygame, sys

pygame.init()

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 800
BALL_RADIUS = 60
PADDLE = pygame.Rect((SCREEN_WIDTH // 2) + 500, SCREEN_HEIGHT // 2, 20, 100)

# Colors
BACKGROUND_COLOR = (221,234,243)
BALL_COLOR = (111,204,227)
FONT_COLOR = (43,102,158)

# Game Setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Bouncing a Ball")

# Fonts
font = pygame.font.SysFont("Arial", 64)
text = font.render("Let's Pong", True, FONT_COLOR)

# Set Balls initial position to the center of the screen
ball_pos = [SCREEN_WIDTH//2, SCREEN_HEIGHT//2]
ball_speed = [2,2]
pad_y = SCREEN_HEIGHT // 2
key = ""
score = 0

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # move player
    key = pygame.key.get_pressed()
    if key[pygame.K_DOWN]:
        pad_y += 5
    if key[pygame.K_UP]:
        pad_y += -5
    PADDLE = pygame.Rect((SCREEN_WIDTH // 2) + 500, pad_y, 20, 100)

    # move the ball based on the speed
    ball_pos[0] += ball_speed[0] * (score*0.7 + 1)
    ball_pos[1] += ball_speed[1] * (score*0.7 + 1)

    #bounce off of the walls
    if ball_pos[0] <= BALL_RADIUS or ball_pos[0] >= SCREEN_WIDTH- BALL_RADIUS:
        if ball_pos[0] >= SCREEN_WIDTH- BALL_RADIUS:
            pygame.quit()
            sys.exit()
        else:
            ball_speed[0] = -ball_speed[0]

    if PADDLE.collidepoint(ball_pos[0] + BALL_RADIUS,ball_pos[1]) or PADDLE.collidepoint(ball_pos[0],ball_pos[1] + BALL_RADIUS) or PADDLE.collidepoint(ball_pos[0] - BALL_RADIUS,ball_pos[1]) or PADDLE.collidepoint(ball_pos[0],ball_pos[1] - BALL_RADIUS):
        ball_speed[0] = -ball_speed[0]
        ball_pos[0] -= BALL_RADIUS // 2
        score += 1

    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= SCREEN_HEIGHT - BALL_RADIUS:
        ball_speed[1] = - ball_speed[1]

    screen.fill(BACKGROUND_COLOR)
    pygame.draw.circle(screen, BALL_COLOR, (ball_pos[0], ball_pos[1]), BALL_RADIUS)
    screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width()//2, 100))   # Centering title in the screen
    screen.blit(font.render("score: "+str(score), True, FONT_COLOR), (SCREEN_WIDTH // 2 - 500, 100))
    pygame.draw.rect(screen,(0,0,0),PADDLE) 
    pygame.display.update()