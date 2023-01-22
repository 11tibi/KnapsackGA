from pathlib import Path
from Solver import Solver
from KnapsackGreedy import KnapsackGreedy
import re
import matplotlib.pyplot as plt


class KnapsackGA:
    def __init__(self):
        self.instances = []
        self.read_instances()

    def read_instance(self, instance: str) -> dict:
        data = {}
        instance = re.sub(re.compile(r'/[*].*?[*]/', re.DOTALL), '', instance)
        instance = re.sub(re.compile(r'//.*?\n'), '', instance)
        instance = re.sub(r' +', ' ', instance)
        instance = re.sub(r'\n', '', instance)
        data['no_objects'] = int(re.search(r'no_objects = (\d*)', instance).group(1))
        data['max_weight'] = int(re.search(r'max_weight = (\d*)', instance).group(1))
        data['weights'] = list(map(int, re.search(r'weights = \[ (\d+( \d+)+) ]', instance).group(1).split(' ')))
        data['objects'] = list(map(int, re.search(r'objects = \[ (\d+( \d+)+) ]', instance).group(1).split(' ')))
        return data

    def read_instances(self):
        instances = list(Path('./knapsack_instances').rglob('*.[tT][xX][tT]'))
        for instance in instances:
            with open(instance) as f:
                data = self.read_instance(''.join(f.readlines()))
                self.instances.append(data)

    def solve_instances(self):
        results_ga = []
        results_greedy = []
        for instance in self.instances:
            results_ga.append(Solver(instance).solve())
            results_greedy.append(KnapsackGreedy(instance).knapsack_greedy())
        return results_ga, results_greedy, self.instances


if __name__ == '__main__':
    knapsack_ga = KnapsackGA()
    res = knapsack_ga.solve_instances()
    for i in res:
        print(i)
    plt.plot(range(len(res[0])), res[0], label="GA")
    plt.plot(range(len(res[0])), res[1], label="knapsack")
    plt.legend()
    plt.show()
