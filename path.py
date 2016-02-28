from random import randint, shuffle

from city import City

class Path:
    _cities = [];

    def __init__(self, cities):
        self._cities = cities;
        shuffle(self._cities);

    def length(self):
        sumPairs = zip(self._cities, [self._cities[-1]] + self._cities[0:-1]);
        return sum(map(lambda tup: City.distance(tup[0],tup[1]), sumPairs));

    def draw(self, color):
        sumPairs = zip(self._cities, [self._cities[-1]] + self._cities[0:-1]);

        for (a, b) in sumPairs:
            plt.plot([a.x, b.x], [a.y, b.y], color = color, aa = True)

        return;

    def mutate(self):
        n = len(self._cities);
        first_index = randint(0, n-1)
        second_index = randint(0, n-1)

        # make sure that we are swapping different cities
        while first_index == second_index:
            second_index = randint(0, n-1)

        # swap cities
        tmp = self._cities[first_index];
        self._cities[first_index] = self._cities[second_index];
        self._cities[second_index] = tmp;

        return

    def crossover(self, other, size):
        # print("--------------");
        # print(self._cities);


        # l = list(map(lambda x: int(x.name), self.cities));
        # l.sort();
        # l = map(lambda x: str(x), l)
        # j = []
        # for i in l:
        #     if i not in j:
        #         j.append(str(i));
        # l = map(lambda x: str(x), j)
        # bef = len(list(l));

        n = len(self._cities);
        first_index = randint(0, n-1-size);
        second_index = first_index + size;
        #print(first_index, ", ", second_index);

        same_cities = self._cities[first_index:second_index];
        rest_cities = list(x for x in other._cities if x not in same_cities);
        # print(same_cities);
        # print(rest_cities);

        reassebmled = rest_cities[0:first_index] + same_cities + rest_cities[second_index:];
        self._cities = reassebmled;

        # l = list(map(lambda x: int(x.name), result.cities));
        # l.sort();
        # l = map(lambda x: str(x), l)
        # j = []
        # for i in l:
        #     if i not in j:
        #         j.append(str(i));
        # aft = len(j)
        # print(bef - aft)

        return
