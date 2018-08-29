from Dot import *


class Population:
    def __init__(self):
        self.dots = []
        for i in range(pop_size):
            self.dots.append(Dot())
        self.total_fitness = 0.0
        self.all_dead = False
        self.generation = 1
        self.best_dot = Dot()

    def update(self):
        all_dead = True
        for dot in self.dots:
            dot.update(self.generation)
            if not dot.is_dead:
                all_dead = False
        if all_dead:
            self.all_dead = True

    def compute_total_fitness(self):
        best_dot = Dot()
        self.total_fitness = 0.0
        for dot in self.dots:
            dot.is_best = False
            dot.compute_fitness()
            if dot.fitness > best_dot.fitness:
                best_dot = dot
            self.total_fitness += dot.fitness
        self.best_dot = best_dot
        print(self.total_fitness)

    def natural_selection(self):
        new_dots = []
        for dot in range(pop_size):
            parent = self.select_parent()
            new_dots.append(parent.get_baby())
        self.dots = new_dots.copy()
        self.best_dot.is_best = True
        self.dots[0] = self.best_dot.get_baby()

    def select_parent(self):
        limit = random.uniform(0.0, self.total_fitness)
        curr_sum = 0.0
        for dot in self.dots:
            curr_sum += dot.fitness
            if curr_sum >= limit:
                return dot
        return None
