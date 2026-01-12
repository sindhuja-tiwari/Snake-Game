import pygame
import random

pygame.init()

# Screen
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

# Colors
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLACK = (0,0,0)

# Snake
snake_block = 10
snake = [(300, 200)]
direction = (snake_block, 0)

# Food
food = (
    random.randrange(0, WIDTH, snake_block),
    random.randrange(0, HEIGHT, snake_block)
)

score = 0
font = pygame.font.SysFont(None, 30)

def draw_score():
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = (0, -snake_block)
            elif event.key == pygame.K_DOWN:
                direction = (0, snake_block)
            elif event.key == pygame.K_LEFT:
                direction = (-snake_block, 0)
            elif event.key == pygame.K_RIGHT:
                direction = (snake_block, 0)

    # Move snake
    head_x = snake[0][0] + direction[0]
    head_y = snake[0][1] + direction[1]
    new_head = (head_x, head_y)

    # Collision with wall
    if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
        running = False

    # Collision with self
    if new_head in snake:
        running = False

    snake.insert(0, new_head)

    # Eat food
    if new_head == food:
        score += 1
        food = (
            random.randrange(0, WIDTH, snake_block),
            random.randrange(0, HEIGHT, snake_block)
        )
    else:
        snake.pop()

    # Draw snake
    for part in snake:
        pygame.draw.rect(screen, GREEN, (*part, snake_block, snake_block))

    # Draw food
    pygame.draw.rect(screen, RED, (*food, snake_block, snake_block))

    draw_score()
    pygame.display.update()
    clock.tick(15)

pygame.quit()
