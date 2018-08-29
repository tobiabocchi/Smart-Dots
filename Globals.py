import pygame


pygame.init()
pygame.font.init()

# COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
LIGHT_BLUE = (0, 255, 255)
GREY = (96, 96, 96)

# DISPLAY VARIABLES
frame_per_second = 100
resolution = (1300, 700)
game_display = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()
clock.tick(frame_per_second)
pygame.display.set_caption("Smart Dots")
data_font = pygame.font.SysFont('Comic Sans MS', 30)


# SIMULATION VARIABLES
simulation_over = False
dot_pos = (1100, 350)
dot_radius = 2
step_len = 20
n_steps = 400
goal_top_left = (50, 340)
goal_size = (20, 20)
goal_center = (int(goal_top_left[0] + goal_size[0] / 2), int(goal_top_left[1] + goal_size[1] / 2))
goal = pygame.Rect(goal_top_left, goal_size)
pop_size = 1500
mutation_rate = 0.05
obs_size = (40, 400)
obs_a_top_left = (500, 0)
obs_b_top_left = (650, 300)
obs_c_top_left = (800, 0)
obs_d_top_left = (350, 300)
obs_a = pygame.Rect(obs_a_top_left, obs_size)
obs_b = pygame.Rect(obs_b_top_left, obs_size)
obs_c = pygame.Rect(obs_c_top_left, obs_size)
obs_d = pygame.Rect(obs_d_top_left, obs_size)
