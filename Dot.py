from Globals import *
import random
import math


class Dot:
    def __init__(self):
        self.position = dot_pos
        self.shape = pygame.Rect(dot_pos[0] - dot_radius, dot_pos[1] - dot_radius, 2 * dot_radius, 2 * dot_radius)
        self.dir = []
        for i in range(n_steps):
            rand = random.random() * 2.0 * math.pi
            self.dir.append(rand)
        self.curr_step = 0
        self.is_dead = False
        self.winner = False
        self.fitness = 0
        self.is_best = False

    def compute_fitness(self):
        dist_to_goal = math.sqrt((goal_center[0] - self.position[0])**2.0 + (goal_center[1] - self.position[1])**2.0)
        if dist_to_goal != 0:
            self.fitness = 1 / (dist_to_goal ** 2)
        else:
            self.fitness = 1
        if self.winner:
            self.fitness += 1 / self.curr_step

    def move(self):
        angle = self.dir[self.curr_step]
        new_x = self.position[0] + step_len * math.cos(angle)
        new_y = self.position[1] + step_len * math.sin(angle)
        self.position = (int(new_x), int(new_y))
        self.curr_step += 1

    def check_goal(self):
        if goal.colliderect(self.shape):
            self.winner = True
            self.is_dead = True

    def check_dead(self):
        if self.curr_step >= n_steps:
            self.is_dead = True
            return
        if self.position[0] >= resolution[0] or self.position[0] <= 0 or \
                self.position[1] >= resolution[1] or self.position[1] <= 0:
            self.is_dead = True

    def check_obstacle(self, generation):
        if generation > 15:
            if self.shape.colliderect(obs_a) or self.shape.colliderect(obs_b) or \
                    self.shape.colliderect(obs_c) or self.shape.colliderect(obs_d):
                self.is_dead = True
        elif self.shape.colliderect(obs_a) or self.shape.colliderect(obs_b):
            self.is_dead = True

    def update(self, generation):
        self.check_goal()
        self.check_dead()
        if generation > 5:
            self.check_obstacle(generation)
        if self.curr_step == 0:
            self.draw()
        if not self.is_dead and not self.winner:
            self.move()
        if self.curr_step != 1:  # this is to draw them all at their initial position
            self.draw()

    def draw(self):
        if self.winner:
            self.shape = pygame.draw.circle(game_display, BLUE, self.position, dot_radius)
        elif self.is_dead:
            if self.is_best:
                self.shape = pygame.draw.circle(game_display, LIGHT_BLUE, self.position, dot_radius)
            else:
                self.shape = pygame.draw.circle(game_display, RED, self.position, dot_radius)
        elif self.is_best:
            self.shape = pygame.draw.circle(game_display, LIGHT_BLUE, self.position, dot_radius)
        else:
            self.shape = pygame.draw.circle(game_display, BLACK, self.position, dot_radius)

    def get_baby(self):
        baby = Dot()
        if self.is_best:  # keep best without mutating it
            baby.is_best = True
            baby.dir = self.dir.copy()
            return baby
        for i in range(n_steps):
            baby.dir[i] = self.dir[i]
            if random.random() <= mutation_rate:
                baby.dir[i] = random.random() * 2.0 * math.pi
        return baby

