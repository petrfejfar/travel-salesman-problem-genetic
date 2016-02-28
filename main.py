from city import City
from population import Population

import matplotlib.pyplot as plt
import csv

GENERATION_SIZE = 40
MUTATE_COUNT = 6
CROSSOVER_COUNT = 6
CROSSOVER_SIZE = 5

def preprocessData(filename):
    with open(filename, 'r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=' ', quoting=csv.QUOTE_NONNUMERIC)
        data = [];
        for row in csv_reader:
            # 1 565.0 575.0
            # 2 25.0 185.0
            # ...
            data.append(City(row[1], row[2], str(int(row[0]))))

        return data;

def run():
    cities = preprocessData("berlin.tsp");

    pop = Population(cities, GENERATION_SIZE)

    history = [];
    i = 0;
    best = pop.getBestMember().length();
    for j in range(1500):
        # get next generation
        pop = pop.copyPopulation();
        #pop.crossover(CROSSOVER_COUNT, CROSSOVER_SIZE)
        #pop.mutate(MUTATE_COUNT)
        print(list(map(lambda x: x.length(), pop._members)))

        best_member = pop.getBestMember();
        new_fitness = best_member.length();
        print(new_fitness)
        import time
        time.sleep(2.5)
        history.append(new_fitness)

        if(best > new_fitness):
            best = new_fitness;

            # gra = int(122);
            # plt.clf();
            # for c in best_member.cities:
            #     plt.plot([c.x], [c.y], color = "red", aa = True, marker = "o");
            #     plt.annotate(int(c.name), (c.x, c.y), color = "red");

            # plt.title('Fitness = %.2fkm' % new_fitness);
            # best_member.draw("#%02x%02x%02x" % (gra, gra, gra) );
            # plt.savefig("stats/fig%s.png" % i);
            # i += 1;

            print(best)
    #plt.clf();
    #plt.plot(history);
    #plt.savefig("histogram.png");

    return history

if __name__ == '__main__':
    runs = []
    for i in range(10):
        runs.append(run());
        print("run", i)

    plt.clf()
    plt.ylim([0,30000])
    plt.plot(list(map(lambda x: float(sum(x))/len(x), zip(*runs))))
    plt.savefig("stats/avg_histogram.png")
    print("end")
