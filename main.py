from city import City
from population import Population

import matplotlib.pyplot as plt
import csv

# simulation constants
GENERATION_SIZE = 80
MUTATE_COUNT = 3
CROSSOVER_COUNT = 12
CROSSOVER_SIZE_MIN = 3
CROSSOVER_SIZE_MAX = 7

# simulation settings
SIMULATED_POPULATION_COUNT = 100

# plotting settings
PLOT_AVERAGE_HISTOGRAM = True
PLOT_AVERAGE_HISTOGRAM_SAMPLE_COUNT = 3
PLOT_PATH = False


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


def run():
    cities = preprocessData("berlin.tsp")

    pop = Population(cities, GENERATION_SIZE)
    history = []
    i = 0
    best = pop.getBestMember().length()
    for j in range(SIMULATED_POPULATION_COUNT):
        # get next generation
        pop = pop.copyPopulation()
        pop.crossover(CROSSOVER_COUNT, CROSSOVER_SIZE_MIN, CROSSOVER_SIZE_MAX)
        pop.mutate(GENERATION_SIZE-CROSSOVER_COUNT, MUTATE_COUNT)

        best_member = pop.getBestMember()
        new_fitness = best_member.length()

        history.append(new_fitness)

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
    return history

if __name__ == '__main__':
    print("Started simulation with:")
    print("GENERATION_SIZE = ", GENERATION_SIZE)
    print("MUTATE_COUNT = ", MUTATE_COUNT)
    print("CROSSOVER_COUNT = ", CROSSOVER_COUNT)
    print("CROSSOVER_SIZE_MIN = ", CROSSOVER_SIZE_MIN)
    print("CROSSOVER_SIZE_MAX = ", CROSSOVER_SIZE_MAX)

    runs = []
    for i in range(PLOT_AVERAGE_HISTOGRAM_SAMPLE_COUNT):
        runs.append(run())
        print(runs[-1][-1])
        print("run", i)

    if(PLOT_AVERAGE_HISTOGRAM):
        plt.clf()
        plt.ylim([0, 30000])
        plt.plot(list(map(lambda x: float(sum(x))/len(x), zip(*runs))))
        plt.savefig("stats/avg_histogram.png")
