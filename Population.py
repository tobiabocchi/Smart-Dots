from Square import *


class Population:
    def __init__(self):
        self.squares = []
        for i in range(pop_size):
            s = Square()
            self.squares.append(s)
            all_sprites.add(s)
            pop_sprites.add(s)
        self.total_fitness = 0.0
        self.generation = 1
        self.best_square_dir = []
        self.best_square = Square

    def boost_fitness(self):
        best_steps = self.best_square.curr_step
        fixed_direction = best_steps
        new_squares = []
        for i in range(pop_size):
            if i < 50:  #  for the first 50 keep evolving normally
                baby = self.select_parent().get_baby()
                new_squares.append(baby)
            elif best_steps < n_steps and not self.best_square.has_reached_goal:  #  the best crushed somewhere
                baby = Square()
                if i < pop_size / 2:
                    explosion = 50
                else:
                    explosion = 15
                for j in range(fixed_direction - explosion):
                    baby.dir[j] = self.best_square_dir[j]
                new_squares.append(baby)
                baby.add(all_sprites)
                baby.add(pop_sprites)
            else:
                baby = Square()
                remainder = i % 50
                if remainder == 0:
                    fixed_direction -= 15
                    baby.dir = cardinal_dir[remainder].copy()
                elif remainder < 4:
                    baby.dir = cardinal_dir[remainder].copy()
                for j in range(fixed_direction):
                    baby.dir[j] = self.best_square_dir[j]
                new_squares.append(baby)
                baby.add(all_sprites)
                baby.add(pop_sprites)
        self.squares = new_squares.copy()
        self.keep_best()
        self.generation += 1

    def compute_total_fitness(self):
        self.total_fitness = 0.0
        fittest = 0.0
        for square in self.squares:
            square.compute_fitness()
            if fittest < square.fitness:
                fittest = square.fitness
                self.best_square = square
                self.best_square_dir = square.dir.copy()
            self.total_fitness += square.fitness
            square.kill()

    def natural_selection(self):
        new_squares = []
        for i in range(0, pop_size):
            baby = self.select_parent().get_baby()
            new_squares.append(baby)
        self.squares = new_squares.copy()
        self.keep_best()
        self.generation += 1

    def select_parent(self):
        avg = self.total_fitness / pop_size
        rand = random.uniform(0.0, self.total_fitness)
        curr_sum = 0.0
        for square in self.squares:
            curr_sum += square.fitness
            if square.fitness > avg and curr_sum > rand:
                return square
        best = Square()
        best.dir = self.best_square_dir.copy()
        return best

    def keep_best(self):
        best = self.squares[0]
        best.dir = self.best_square_dir.copy()
        best.is_best = True
        best.image = pygame.Surface((square_side * 3, square_side * 3))
        best.image.fill(MAGENTA)
