import pygame
import time
import random

# Initialize pygame
pygame.init()

# Define colors for the game
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Set up display dimensions
width, height = 600, 400
game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Game clock for controlling frame rate
clock = pygame.time.Clock()

# Size of the snake block and game speed
snake_block = 10
snake_speed = 15

# Font styles for messages and score
font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont("comicsansms", 35)

# Function to draw our snake
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(game_display, black, [x[0], x[1], snake_block, snake_block])

# Function to display messages
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    game_display.blit(mesg, [width / 6, height / 3])

# The main loop of the game
def gameLoop():
    game_over = False
    game_close = False

    # Starting position of the snake
    x1 = width / 2
    y1 = height / 2

    # Variables to change the position of the snake
    x1_change = 0       
    y1_change = 0

    # Snake body list and initial length
    snake_list = []
    length_of_snake = 1

    # Position of the food
    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    while not game_over:

        # When the game ends (snake collides)
        while game_close:
            game_display.fill(red)
            message("You Lost! Press Q-Quit or C-Play Again", black)
            pygame.display.update()

            # Event handling when the game is over
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        # Event handling during the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Check if the snake has hit the boundary
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        game_display.fill(white)
        pygame.draw.rect(game_display, green, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Check if the snake has collided with itself
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_block, snake_list)
        pygame.display.update()

        # Check if the snake has eaten the food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        # Control the frame rate
        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Start the game
gameLoop()
