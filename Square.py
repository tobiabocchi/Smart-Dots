from Globals import *


class Square(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((square_side, square_side))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = pop_coord
        self.dir = []
        for i in range(n_steps):
            self.dir.append(random.uniform(0.0, 2.0 * math.pi))
        #  item's characteristics
        self.curr_step = 0
        self.is_dead = False
        self.fitness = 0.0
        self.has_reached_goal = False
        self.is_best = False

    def update(self):
        if (self.curr_step >= n_steps or self.out_of_bound()) and not self.has_reached_goal:
            self.die()
        else:
            self.move()

    def move(self):
        alpha = self.dir[self.curr_step]
        self.rect.centerx += step_len * math.cos(alpha)
        self.rect.centery += step_len * math.sin(alpha)
        self.curr_step += 1

    def compute_fitness(self):
        dist_to_goal = math.hypot(self.rect.centerx - goal_coord[0], self.rect.y - goal_coord[1])
        if self.has_reached_goal:
            self.fitness = 1.0 + (1.0 / float(self.curr_step))
        else:
            self.fitness = 1.0 / dist_to_goal ** 2.0

    def get_baby(self):
        baby = Square()
        for i in range(n_steps):
            if random.random() <= mutation_rate:
                baby.dir[i] = random.uniform(0.0, 2.0 * math.pi)
            else:
                baby.dir[i] = self.dir[i]
        baby.add(all_sprites)
        baby.add(pop_sprites)
        return baby

    def winner(self):
        self.has_reached_goal = True
        if not self.is_best:
            self.image.fill(BLUE)
        self.remove(pop_sprites)
        self.add(winner_sprites)

    def out_of_bound(self):
        if self.rect.left <= 0 or self.rect.top <= 0 or\
                self.rect.right >= resolution[0] or self.rect.bottom >= resolution[1]:
            return True
        else:
            return False

    def die(self):
        self.is_dead = True
        self.image.fill(RED)
        self.remove(pop_sprites)
        self.add(dead_sprites)
