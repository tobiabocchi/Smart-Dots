import pygame
import random
import math

pygame.init()
pygame.font.init()

# COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
GREY = (96, 96, 96)

# DISPLAY VARIABLES
frame_per_second = 100
resolution = (1300, 700)
game_display = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()
pygame.display.set_caption("Smart Dots")
data_font = pygame.font.SysFont('Comic Sans MS', 30)


# SIMULATION VARIABLES
simulation_over = False
pop_coord = (1250, 350)
square_side = 3
step_len = 15
n_steps = 600
goal_coord = (10, 350)
goal_size = (10, 40)
pop_size = 2000
mutation_rate = 0.02
all_sprites = pygame.sprite.Group()
pop_sprites = pygame.sprite.Group()
winner_sprites = pygame.sprite.Group()
dead_sprites = pygame.sprite.Group()
obs_sprites = pygame.sprite.Group()
obs_index = 0
obs_size = (30, 400)
obs_topleft_list = [(1100, 300), (1100, -200), (900, 0), (900, 500), (700, 300), (700, -200), (500, 0), (500, 500),
                    (300, 300), (300, -200)]
font_name = pygame.font.match_font('arial')
lvl_up = False
dir_right = [0] * n_steps
dir_left = [math.pi] * n_steps
dir_up = [(1 / 2) * math.pi] * n_steps
dir_down = [(3 / 2) * math.pi] * n_steps
cardinal_dir = [dir_up, dir_right, dir_down, dir_left]
