from random import randint
from copy import deepcopy

from path import Path


class Population:
    _members = []

    def __init__(self, cities, count):
        for i in range(count):
            self._members.append(Path(cities))

    def _sort(self):
        self._members.sort(key=lambda x: x.length())

    # TODO probably delete
    # def __repr__(self):
    #    return "<" + "; ".join(map(lambda x: str(x.length()), self._members)) + ">";

    def getBestMember(self):
        self._sort()

        return self._members[0]

    def copyPopulation(self):
        return deepcopy(self)

    def crossover(self, count, cross_size):
        # print(self._members)
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
            crossed = father.crossover(mother, cross_size)
            new_members.append(crossed)

        # replace last members by crosseovered members
        self._members = self._members[0:survive_count] + new_members

        return

    def mutate(self, count):
        # print("-------")
        # print(list(map(lambda x: x.length(), self._members)))

        # mutate
        for i in range(count):
            rand_index = randint(0, len(self._members)-1)
            self._members[rand_index].mutate()

        return
