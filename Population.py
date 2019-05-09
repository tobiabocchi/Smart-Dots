from Dot import *


class Population:
    def __init__(self):
        self.dots = []
        for i in range(pop_size):
            s = Dot()
            self.dots.append(s)
            all_sprites.add(s)
            pop_sprites.add(s)
        self.total_fitness = 0.0
        self.generation = 1
        self.best_dot_dir = []
        self.best_dot = Dot

    def boost_fitness(self):
        best_steps = self.best_dot.curr_step
        fixed_direction = best_steps
        new_dots = []
        for i in range(pop_size):
            if i < 50:  #  for the first 50 keep evolving normally
                baby = self.select_parent().get_baby()
                new_dots.append(baby)
            elif best_steps < n_steps and not self.best_dot.has_reached_goal:  #  the best crushed somewhere
                baby = Dot()
                if i < pop_size / 2:
                    explosion = 50
                else:
                    explosion = 15
                for j in range(fixed_direction - explosion):
                    baby.dir[j] = self.best_dot_dir[j]
                new_dots.append(baby)
                baby.add(all_sprites)
                baby.add(pop_sprites)
            else:
                baby = Dot()
                remainder = i % 50
                if remainder == 0:
                    fixed_direction -= 15
                    baby.dir = cardinal_dir[remainder].copy()
                elif remainder < 4:
                    baby.dir = cardinal_dir[remainder].copy()
                for j in range(fixed_direction):
                    baby.dir[j] = self.best_dot_dir[j]
                new_dots.append(baby)
                baby.add(all_sprites)
                baby.add(pop_sprites)
        self.dots = new_dots.copy()
        self.keep_best()
        self.generation += 1

    def compute_total_fitness(self):
        self.total_fitness = 0.0
        fittest = 0.0
        for dot in self.dots:
            dot.compute_fitness()
            if fittest < dot.fitness:
                fittest = dot.fitness
                self.best_dot = dot
                self.best_dot_dir = dot.dir.copy()
            self.total_fitness += dot.fitness
            dot.kill()

    def natural_selection(self):
        new_dots = []
        for i in range(0, pop_size):
            baby = self.select_parent().get_baby()
            new_dots.append(baby)
        self.dots = new_dots.copy()
        self.keep_best()
        self.generation += 1

    def select_parent(self):
        avg = self.total_fitness / pop_size
        rand = random.uniform(0.0, self.total_fitness)
        curr_sum = 0.0
        for dot in self.dots:
            curr_sum += dot.fitness
            if dot.fitness > avg and curr_sum > rand:
                return dot
        best = Dot()
        best.dir = self.best_dot_dir.copy()
        return best

    def keep_best(self):
        best = self.dots[0]
        best.dir = self.best_dot_dir.copy()
        best.is_best = True
        best.image = pygame.Surface((dot_side * 3, dot_side * 3))
        best.image.fill(MAGENTA)
