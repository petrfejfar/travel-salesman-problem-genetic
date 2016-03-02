from city import City
from population import Population
from time import time
from random import randint, random

import matplotlib.pyplot as plt
import csv

# simulation constants
GENERATION_SIZE = 8
MUTATE_COUNT = 1
CROSSOVER_COUNT = 3

# simulation settings
SIMULATION_TIME = 300  # sec

# plotting settings
PLOT_AVERAGE_HISTOGRAM = True
PLOT_AVERAGE_HISTOGRAM_SAMPLE_COUNT = 1
PLOT_PATH = True


def preprocessData(filename):
    with open(filename, 'r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=' ', quoting=csv.QUOTE_NONNUMERIC)
        data = []
        for row in csv_reader:
            # 1 565.0 575.0
            # 2 25.0 185.0
            # ...
            data.append(City(row[1], row[2], str(int(row[0]))))

        return data


def logRand(min, max):
    exp_max = 10 ** 5
    exp = 10 ** (random()*5)

    return


class GArun:
    def __init__(self):
        self.__GENERATION_SIZE = int(10 ** (random()*5))+1
        self.__MUTATE_COUNT = randint(0, self.__GENERATION_SIZE//3)
        self.__CROSSOVER_COUNT = randint(0, self.__GENERATION_SIZE//3)
        self.__CROSSOVER_SIZE_MIN = 0  # randint(0, 51)
        self.__CROSSOVER_SIZE_MAX = randint(self.__CROSSOVER_SIZE_MIN, 51)

        # self.__GENERATION_SIZE = 2569
        # self.__MUTATE_COUNT = 289
        # self.__CROSSOVER_COUNT = 263
        # self.__CROSSOVER_SIZE_MIN = 0
        # self.__CROSSOVER_SIZE_MAX = 10

        self._fitness = None
        self._iteration = None

    def __repr__(self):
        return "gen_size " + str(self.__GENERATION_SIZE) + " mut " + str(self.__MUTATE_COUNT) + " cro " + str(self.__CROSSOVER_COUNT) +\
            " cro_min" + str(self.__CROSSOVER_SIZE_MIN) + " cro_max " + str(self.__CROSSOVER_SIZE_MAX) + " fit " + str(int(self._fitness)) +\
            " iter " + str(self._iteration)

    def mutate(self):
        pass

    def fitness(self, num):
        if self._fitness:
            return self._fitness
        cities = preprocessData("berlin.tsp")

        pop = Population(cities, self.__GENERATION_SIZE)
        history = []
        timestamps = []
        i = 0
        iteration = 0
        best = pop.getBestMember().length()
        start_time = time()
        while(True):
            iteration += 1

            # get next generation
            pop = pop.copyPopulation()
            pop.crossover(self.__CROSSOVER_COUNT, self.__CROSSOVER_SIZE_MIN, self.__CROSSOVER_SIZE_MAX)
            # TODO some comment what lower index do
            lower_index = min(self.__GENERATION_SIZE-self.__CROSSOVER_COUNT, self.__MUTATE_COUNT)
            pop.mutate(lower_index, self.__MUTATE_COUNT)

            duration = time() - start_time
            if(duration >= SIMULATION_TIME):
                break

            best_member = pop.getBestMember()
            new_fitness = best_member.length()

            history.append(new_fitness)
            timestamps.append(duration)

            if(best > new_fitness):
                best = new_fitness

                if(PLOT_PATH):
                    gra = int(122)
                    plt.clf()
                    for c in best_member._cities:
                        plt.plot([c.x], [c.y], color="red", aa=True, marker="o")
                        plt.annotate(int(c.name), (c.x, c.y), color="red")

                    plt.title('Fitness = %.2fkm' % new_fitness)
                    best_member.draw(plt, "#%02x%02x%02x" % (gra, gra, gra))
                    plt.savefig("stats/fig%s.png" % i)
                    i += 1

        self._iteration = iteration
        self._fitness = best

        plt.clf()
        plt.title(self.__repr__())
        plt.ylim([0, 30000])
        plt.plot(timestamps, history)
        plt.savefig("stats/histogram%s.png" % num)

        return best

if __name__ == '__main__':
    # print("Started simulation with:")
    # print("GENERATION_SIZE = ", GENERATION_SIZE)
    # print("MUTATE_COUNT = ", MUTATE_COUNT)
    # print("CROSSOVER_COUNT = ", CROSSOVER_COUNT)
    # print("CROSSOVER_SIZE_MIN = ", CROSSOVER_SIZE_MIN)
    # print("CROSSOVER_SIZE_MAX = ", CROSSOVER_SIZE_MAX)

    runs = []
    for i in range(PLOT_AVERAGE_HISTOGRAM_SAMPLE_COUNT):
        run = GArun()
        runs.append(run.fitness(i))
        print(run)

    if(PLOT_AVERAGE_HISTOGRAM):
        plt.clf()
        plt.ylim([0, 30000])
        plt.plot(runs)
        plt.savefig("stats/avg_histogram.png")
        print(runs)
