from math import log
from collections import defaultdict


class Entropy:
    def __init__(self, elements):
        self.elements = elements

        self.total_occurrences = 0
        self.occurrences = defaultdict(lambda: 0)
        self.occurrences_smaller = defaultdict(lambda: 0)

    def entropy(self, n):
        self.calculate_occurrences(n)

        entropy = 0
        for key, value in self.occurrences.items():
            probability = value / self.total_occurrences
            if n > 1:
                probability_smaller = self.occurrences_smaller[key[:-1]] / self.total_occurrences
                entropy -= probability * log(probability / probability_smaller, 2)
            else:
                entropy -= probability * log(probability, 2)

        return entropy

    def calculate_occurrences(self, n):
        for i in range(0, len(self.elements) - n + 1):
            sublist = self.elements[i:i+n]
            self.occurrences[tuple(sublist)] += 1
            if n > 1:
                self.occurrences_smaller[tuple(sublist[:-1])] += 1

            self.total_occurrences += 1
