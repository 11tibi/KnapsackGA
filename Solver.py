import numpy as np
import random


class Solver:
    def __init__(self, instance: dict):
        self.instance = instance

        self.population_size = 100
        self.num_genes = self.instance['no_objects']
        self.population = np.random.randint(2, size=(self.population_size, self.num_genes))
        self.num_generations = 100
        self.crossover_rate = 0.5
        self.mutation_rate = 0.05
        self.population_fitness = np.array(0)

    def solve(self):
        for i in range(self.num_generations):
            self.fitness()
            self.crossover()
            self.mutation()
        return np.max(self.population_fitness)

    def fitness(self):
        self.population_fitness = np.empty(self.population_size)
        for i in range(self.population_size):
            current_value = np.sum(self.population[i] * self.instance['objects'])
            current_weight = np.sum(self.population[i] * self.instance['weights'])
            if current_weight > self.instance['max_weight']:
                self.population_fitness[i] = 0
            else:
                self.population_fitness[i] = current_value

    def tournament_selection(self):
        parents = []
        for i in range(self.population_size):
            candidates = list(np.random.choice(self.population_size, size=5, replace=False))
            candidates.sort(key=lambda item: self.population_fitness[item], reverse=True)
            parents.append(self.population[candidates[0]])
            parents.append(self.population[candidates[1]])
        return np.array(parents)

    def crossover(self):
        parents = self.tournament_selection()
        ch = np.empty((len(parents), self.num_genes))
        crossover_point = len(parents[0]) // 2
        for i in range(0, len(parents), 2):
            if random.random() > self.crossover_rate:
                ch[i] = parents[i]
                ch[i+1] = parents[i+1]
            else:
                ch[i] = np.concatenate((list(parents[i][:crossover_point]), list(parents[i+1][crossover_point:])))
                ch[i+1] = np.concatenate((list(parents[i+1][:crossover_point]), list(parents[i][crossover_point:])))
        self.population = ch
        return ch

    def mutation(self):
        for i in range(self.population_size):
            if random.uniform(0, 1) <= self.mutation_rate:
                index = random.randint(0, self.num_genes-1)
                self.population[i][index] = 0 if self.population[i][index] == 1 else 1

    def elitism(self):
        pass
