import numpy as np


class KnapsackGreedy:
    def __init__(self, instance):
        if len(instance["weights"]) != len(instance["objects"]):
            raise ValueError('"weights" and "values" should have the same length')
        self.weights = np.array(instance["weights"], dtype=float)
        self.values = np.array(instance["objects"], dtype=float)
        self.max_weight = instance["max_weight"]

    def knapsack_greedy(self):
        max_profit = 0
        current_weight = 0
        profit = np.divide(self.values, self.weights)
        sorted_indexes = profit.argsort()[::-1]
        for i in sorted_indexes:
            if (current_weight + self.weights[i]) <= self.max_weight:
                max_profit += self.values[i]
                current_weight += self.weights[i]
            else:
                break
        return max_profit


if __name__ == '__main__':
    instance = {
        "weights": [40, 28, 46, 33, 17, 26, 46, 3, 36, 37],
        "objects": [54, 53, 39, 44, 14, 28, 29, 0, 0, 2],
        "max_weight": 200
    }
    print(KnapsackGreedy(instance).knapsack_greedy())
