"""
AUTHOR: KRISTAL SHRESTHA
DATE: 6/15/2024
PURPOSE: Snake game
"""

import pygame
import random
import os

# Initialize Pygame and mixer
pygame.init()
pygame.mixer.init()

# Constants
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
FPS = 30
SCREEN_HEIGHT = 400
SCREEN_WIDTH = 600
SNAKE_SIZE = 30
INIT_VELOCITY = 5

# Set up font and clock
font = pygame.font.SysFont(None, 30)
clock = pygame.time.Clock()

# Set up game window dimensions
game_window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Load and scale background images
background_image = pygame.image.load('background.jpg')
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT)).convert_alpha()
background_image1 = pygame.image.load('background1.jpg')
background_image1 = pygame.transform.scale(background_image1, (SCREEN_WIDTH, SCREEN_HEIGHT)).convert_alpha()

#sound effects:
effect1=pygame.mixer.Sound('point.wav')

# Set game window title
pygame.display.set_caption("Snakes Kristal")

# Function to display text on screen
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    game_window.blit(screen_text, [x, y])

# Function to plot the snake on the game window
def plot_snake(game_window, color, snake_list, snake_size):
    for x, y in snake_list:
        pygame.draw.rect(game_window, color, [x, y, snake_size, snake_size])

# Welcome screen function
def welcome():
    pygame.mixer.music.load('background1.mp3')
    pygame.mixer.music.play(-1)
    
    exit_game = False
    while not exit_game:
        game_window.blit(background_image1, (0, 0))
        # text_screen("Welcome to Kristal Snakes Game", YELLOW, SCREEN_WIDTH // 4.5, SCREEN_HEIGHT // 2.5)
        # text_screen("Press \"space\" to play", YELLOW, SCREEN_WIDTH // 4.5, SCREEN_HEIGHT // 2.0)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('background.mp3')
                    pygame.mixer.music.play(-1)
                    game_loop()
        
        pygame.display.update()
        clock.tick(FPS)

# Game loop function
def game_loop():
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    food_x = random.randint(0, int(SCREEN_WIDTH / 1.2))
    food_y = random.randint(0, int(SCREEN_HEIGHT / 1.2))
    score = 0
    snake_list = []
    snake_length = 1
    
    # Load highscore
    if os.path.exists('highscore.txt'):
        with open('highscore.txt', 'r') as f:
            highscore = f.read()
    else:
        highscore = 0

    while not exit_game:
        if game_over:
            with open('highscore.txt', 'w') as f:
                f.write(str(highscore))
            game_window.fill(WHITE)
            text_screen("Game Over! Press Enter to continue", RED, SCREEN_WIDTH // 4.5, SCREEN_HEIGHT // 2.5)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = INIT_VELOCITY
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = -INIT_VELOCITY
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_y = -INIT_VELOCITY
                        velocity_x = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y = INIT_VELOCITY
                        velocity_x = 0
                    if event.key == pygame.K_q:
                        score += 10
            
            snake_x += velocity_x
            snake_y += velocity_y

            if abs(snake_x - food_x) < 15 and abs(snake_y - food_y) < 15:
                effect1.play()
                score += 10
                food_x = random.randint(0, int(SCREEN_WIDTH / 1.2))
                food_y = random.randint(0, int(SCREEN_HEIGHT / 1.2))
                snake_length += 5
                if score > int(highscore):
                    highscore = score

            game_window.fill(WHITE)
            game_window.blit(background_image, (0, 0))
            text_screen(f"Score: {score} Highscore: {highscore}", RED, 5, 5)
            pygame.draw.rect(game_window, RED, [food_x, food_y, SNAKE_SIZE, SNAKE_SIZE])

            head = [snake_x, snake_y]
            snake_list.append(head)

            if len(snake_list) > snake_length:
                del snake_list[0]

            if head in snake_list[:-1] or snake_x < 0 or snake_x > SCREEN_WIDTH or snake_y < 0 or snake_y > SCREEN_HEIGHT:
                game_over = True
                pygame.mixer.music.load('hit.wav')
                pygame.mixer.music.play()

            plot_snake(game_window, YELLOW, snake_list, SNAKE_SIZE)

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    quit()

if __name__ == "__main__":
    welcome()
