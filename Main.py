import pygame
import random

WINDOW_WIDTH = 945
WINDOW_HEIGHT = 600
FPS = 60

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Catch the Clown")

PLAYER_STARTING_LIVES = 5
PLAYER_STARTING_VELOCITY = 5
CLOWN_STARING_VELOCITY = 5
CLOWN_ACCELERATION = 1
score = 0
player_lives = PLAYER_STARTING_LIVES
clown_velocity = CLOWN_STARING_VELOCITY

random.choice([-1, 1])
clown_dx = random.choice
clown_dy = random.choice

BLUE = (1, 175, 209)
YELLOW = (248, 231, 28)

pygame.font.Font("assets/Franxurter.ttf", 32)





pygame.init()
clock = pygame.time.Clock()
clock.tick(FPS)
