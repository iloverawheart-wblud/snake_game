import pygame
import random
import sys

pygame.init()

WIDTH = 640
HEIGHT = 480
CELL = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

font = pygame.font.SysFont(None, 35)


def random_food():
    x = random.randint(0, (WIDTH // CELL) - 1) * CELL
    y = random.randint(0, (HEIGHT // CELL) - 1) * CELL
    return [x, y]

def draw_snake(snake):
    for block in snake:
        pygame.draw.rect(screen, GREEN, (block[0], block[1], CELL, CELL))

def show_score(score):
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

def game_over(score):
    screen.fill(GREEN)

    text1 = font.render("GAME OVER", True, RED)
    text2 = font.render(f"Final Score: {score}", True, WHITE)

    screen.blit(text1, (WIDTH // 2 - 100, HEIGHT // 2 - 40))
    screen.blit(text2, (WIDTH // 2 - 100, HEIGHT // 2 + 10))

    pygame.display.update()
    pygame.time.delay(3000)

    pygame.quit()
    sys.exit()

snake = [
    [100, 100],
    [80, 100],
    [60, 100]
]

direction = "RIGHT"

food = random_food()

score = 0

while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP and direction != "DOWN":
                direction = "UP"

            elif event.key == pygame.K_DOWN and direction != "UP":
                direction = "DOWN"

            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                direction = "LEFT"

            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                direction = "RIGHT"

    head_x = snake[0][0]
    head_y = snake[0][1]

    if direction == "UP":
        head_y -= CELL

    elif direction == "DOWN":
        head_y += CELL

    elif direction == "LEFT":
        head_x -= CELL

    elif direction == "RIGHT":
        head_x += CELL

    new_head = [head_x, head_y]

    snake.insert(0, new_head)

    if snake[0] == food:
        score += 1
        food = random_food()

    else:
        snake.pop()

    if (
        head_x < 0
        or head_x >= WIDTH
        or head_y < 0
        or head_y >= HEIGHT
    ):
        game_over(score)

    if snake[0] in snake[1:]:
        game_over(score)

    screen.fill(BLACK)

    draw_snake(snake)

    pygame.draw.rect(
        screen,
        RED,
        (food[0], food[1], CELL, CELL)
    )

    show_score(score)

    pygame.display.update()

    clock.tick(10)