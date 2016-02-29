from random import randint
from copy import deepcopy

from path import Path


class Population:
    def __init__(self, cities, count):
        self._members = []
        for i in range(count):
            self._members.append(Path(cities))
        self._sort()

    def _sort(self):
        self._members.sort(key=lambda x: x.length())

    def __repr__(self):
        return "Population with" + str(len(self._members)) + " members, fitnesses: <" + \
            "; ".join(map(lambda x: str(x.length()), self._members)) + ">"

    def getBestMember(self):
        self._sort()

        return self._members[0]

    def copyPopulation(self):
        copy = Population(None, 0)
        copy._members = self._members
        return copy

    def crossover(self, count, cross_size_min, cross_size_max):
        survive_count = len(self._members) - count

        # crossover new members
        new_members = []
        for i in range(count):
            father_index = randint(0, survive_count-1)
            mother_index = randint(0, survive_count-1)
            while father_index == mother_index:
                mother_index = randint(0, survive_count-1)

            father = self._members[father_index]
            mother = self._members[mother_index]
            cross_size = randint(cross_size_min, cross_size_max)
            crossed = father.crossover(mother, cross_size)
            new_members.append(crossed)

        # replace last members by crosseovered members
        self._members = self._members[0:survive_count] + new_members

        return

    def mutate(self, lower_index, count):
        # mutate
        n = len(self._members)
        for i in range(count):
            # we mutate only in selection of <lower_index, n) to mutate only cross members
            rand_index = randint(lower_index, n-1)
            self._members[rand_index].mutate()

        return
