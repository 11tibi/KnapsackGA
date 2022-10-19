import numpy as np
import random


class Solver:
    def __init__(self, instance: dict):
        self.instance = instance

        self.population_size = 6
        self.num_genes = self.instance['no_objects']
        self.population = np.random.randint(2, size=(self.population_size, self.num_genes))
        self.num_generations = 100
        self.crossover_rate = 0.5
        self.mutation_rate = 0.05
        self.population_fitness = np.array(0)

    def solve(self):
        self.fitness()
        self.tournament_selection()

    def fitness(self):
        self.population_fitness = np.empty(self.population_size)
        for i in range(self.population_size):
            current_value = np.sum(self.population[i] * self.instance['objects'])
            current_weight = np.sum(self.population[i] * self.instance['weights'])
            if current_weight > self.instance['max_weight']:
                self.population_fitness[i] = 0
            else:
                self.population_fitness[i] = current_value

    def mutation(self):
        for i in range(self.population_size):
            if random.uniform(0, 1) <= self.mutation_rate:
                index = random.randint(0, self.num_genes)
                # self.population[i][index] = 0 if self.population[i][index] == 1 else self.population[i][index] = 1

    def tournament_selection(self):
        parents = random.choices(self.population, k=5)

        print(parents)
        # print(self.population_fitness)
        # print(np.where(self.population_fitness == np.max(self.population_fitness)))
        # print(self.population_fitness.argsort()[::-1])

    def crossover(self):
        pass

    def elitism(self):
        pass
