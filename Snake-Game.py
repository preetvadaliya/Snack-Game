#import all required python module
import pygame
import sys
import random
from pygame.locals import  *

#init pygame
pygame.init()
clock = pygame.time.Clock()

#score counting
global score
global snakeLength
global snakeList
score = 0
snakeLength = 1
snakeList = []

#define screen properties
screenHeight = 600
screenWidth = 1000
screenColor = (0, 0, 0)

#create screen
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Snake Game")

#create snake
snakeSize = 20
snakeColor = (255, 255, 255)
snakeX = (screenWidth - snakeSize) // 2
snakeY = (screenHeight - snakeSize) // 2
snakeSpeedX = 0
snakeSpeedY = 0
snake = pygame.Rect(snakeX, snakeY, snakeSize, snakeSize)

#create food on random place
foodSize = 20
foodX = random.randint(20, screenWidth - 20)
foodY = random.randint(20, screenHeight - 20)
global foodColor 
global food 
foodColor = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
food = pygame.Rect(foodX, foodY, foodSize, foodSize)


#main game loop
while True:

  #movement of snake
  snake.centerx += snakeSpeedX
  snake.centery += snakeSpeedY

  #snake position checking
  if snake.right < 0:
    snake.left = screenWidth 

  if snake.left > screenWidth:
    snake.right = 0

  if snake.bottom < 0:
    snake.top = screenHeight 
  
  if snake.top > screenHeight:
    snake.bottom = 0

  #event checking for game
  for event in pygame.event.get():

    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
  
    #user input checking
    if event.type == pygame.KEYDOWN:

      if event.key == pygame.K_LEFT and snakeSpeedX != 1:
        snakeSpeedX = -1
        snakeSpeedY = 0
      
      if event.key == pygame.K_RIGHT and snakeSpeedX != -1:
        snakeSpeedX = 1
        snakeSpeedY = 0

      if event.key == pygame.K_UP and snakeSpeedY != 1:
        snakeSpeedX = 0
        snakeSpeedY = -1
      
      if event.key == pygame.K_DOWN and snakeSpeedY != -1:
        snakeSpeedX = 0
        snakeSpeedY = 1

  #filling color in screen
  screen.fill(screenColor)

  #draw shape in screen
  pygame.draw.rect(screen,snakeColor, snake)
  
  #update food when snake eat food
  pygame.draw.ellipse(screen, foodColor, food)

  if snake.colliderect(food):
    food = pygame.Rect(random.randint(20, screenWidth - 20), random.randint(20, screenHeight - 20), foodSize, foodSize)
    foodColor = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    score += 1
    snakeLength += 1

     
  snakeList.append((snake.x, snake.y))
  snakeList = snakeList[-snakeLength-4:]

  for i in range(snakeLength):
    pygame.draw.rect(screen, snakeColor, pygame.Rect(snakeList[i][0], snakeList[i][1], snakeSize, snakeSize))
    
  #flip display for update screen
  pygame.display.flip()

  #set FPS of screen
  clock.tick(128)