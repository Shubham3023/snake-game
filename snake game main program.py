import pygame
from random import *

# initialize the pygame
pygame.init()
# set the screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("snake game")
# parametes for snake
snakeX = 200
snakeY = 200
snakeX_change = 0
snakeY_change = 0

# set clock
clock = pygame.time.Clock()

# parameters for food
foodX = randint(5, 765)
foodY = randint(5, 565)

# parameters for score
score_count = 0
scoreX = 10
scoreY = 10
score_font = pygame.font.Font("freesansbold.ttf", 15)

# parameters for the logic of snake growth
snake_list = []
snake_list_num = 1
# parameters for game over
game_over_font = pygame.font.Font("freesansbold.ttf", 60)
game_over_X = 189
game_over_Y = 182


# function for snake
def snake(x, y):
    for x, y in snake_list:
        pygame.draw.rect(screen, (255, 255, 255), (x, y, 10, 10))


# function for game over
def game_over(x, y):
    game_o = game_over_font.render("GAME OVER!!", True, (0, 255, 0))
    screen.blit(game_o, (x, y))


# function for food
def food(x, y):
    pygame.draw.rect(screen, (0, 255, 0), (x, y, 20, 20))


# function for scorecard
def scoreboard(x, y):
    scr = score_font.render("score: " + str(score_count), True, (255, 255, 255))
    screen.blit(scr, (x, y))


# game loop
running = True
while running:
    # read the score which we've wrote in file mentioned bellow in string type
    f = open("highscore memmory", "r")
    highest = f.read()

    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        # key to quit the window
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            # key to return to the main window after game is over
            if event.key == pygame.K_RETURN:
                # simply recall all the variables you've assigned
                snakeX = 200
                snakeY = 200
                snakeX_change = 0
                snakeY_change = 0
                clock = pygame.time.Clock()

                foodX = randint(5, 765)
                foodY = randint(5, 565)

                score_count = 0
                scoreX = 10
                scoreY = 10
                score_font = pygame.font.Font("freesansbold.ttf", 15)

                snake_list = []
                snake_list_num = 1
            # key to move snake upward
            if event.key == pygame.K_UP:
                snakeY_change = -3
                snakeX_change = 0
            # key to move snake downward
            if event.key == pygame.K_DOWN:
                snakeY_change = 3
                snakeX_change = 0
            # key to move snake right
            if event.key == pygame.K_RIGHT:
                snakeX_change = 3
                snakeY_change = 0
            # key to move snake left
            if event.key == pygame.K_LEFT:
                snakeX_change = -3
                snakeY_change = 0
    # equations for snake movements
    snakeX += snakeX_change
    snakeY += snakeY_change
    # collision detection
    if (snakeX + 10) in range(foodX, foodX + 30) and (snakeY + 10) in range(foodY, foodY + 30):
        foodX = randint(5, 765)
        foodY = randint(5, 565)
        score_count += 1
        snake_list_num += 5

    # display the snake food and score card
    snake(snakeX, snakeY)
    food(foodX, foodY)
    scoreboard(scoreX, scoreY)

    # append position of snake head in head list and use it as head in functin snake()
    head = []
    head.append(snakeX)
    head.append(snakeY)
    snake_list.append(head)

    # condition to increase the length of snake
    if len(snake_list) > snake_list_num:
        del snake_list[0:1]
    # condition of biting the body
    if head in snake_list[:-1] or snakeX <= 0 or snakeY <= 0 or snakeX >= 800 or snakeY >= 600:
        screen.fill((0, 0, 0))
        snakeY_change = 0
        snakeX_change = 0
        game_over(game_over_X, game_over_Y)
        if score_count > int(highest):
            # write the value of scorecount if its the highest of all time otherwise just pass
            f = open("highscore memmory", "w")
            f.write(str(score_count))
        else:
            pass

    highestscore_font = pygame.font.Font("freesansbold.ttf", 15)
    highest_label = highestscore_font.render("highest score: " + highest, True, (255, 255, 255))
    screen.blit(highest_label, (10, 30))

    # set FPS
    clock.tick(60)
    pygame.display.update()
pygame.quit()
