import matplotlib.pyplot as plt
import math
import random
import csv
import copy

GENERATION_SIZE = 40
MUTATE_COUNT = 6
CROSSOVER_COUNT = 6

CROSSOVER_SIZE = 5

class City:
    x = 0
    y = 0
    name = ""
    def __init__(self, x, y, name):
        self.x = x;
        self.y = y;
        self.name = name;
    
    def __repr__(self):
        return "City %s" % self.name;

class Path:
    cities = []
    def __init__(self, cities):
        self.cities = copy.deepcopy(cities);
        random.shuffle(self.cities);

    def length(self):
        sumPairs = zip(self.cities, [self.cities[-1]] + self.cities[0:-1]);
        return sum(map(lambda tup: distance(tup[0],tup[1]), sumPairs));
            
    def draw(self, color):
        sumPairs = zip(self.cities, [self.cities[-1]] + self.cities[0:-1]);

#        l = list(map(lambda x: int(x.name), self.cities));
#        l.sort();
#        l = map(lambda x: str(x), l)                
#        bef = len(list(l));
#        
#        l = list(map(lambda x: int(x.name), self.cities));
#        l.sort();
#        l = map(lambda x: str(x), l)                
#        j = []        
#        for i in l:
#            if i not in j:
#                j.append(str(i));
#        aft = len(j)
#        print(bef - aft)
#        
        for (a, b) in sumPairs:
            plt.plot([a.x, b.x], [a.y, b.y], color = color, aa = True)
            
        
        return;  

    def mutated(self):
        result = copy.deepcopy(self);
        n = len(result.cities);
        first_index = random.randint(0, n-1)
        second_index = random.randint(0, n-1)

        # make sure that we are swapping different cities         
        while first_index == second_index:
            second_index = random.randint(0, n-1)
    
        # swap cities
        tmp = result.cities[first_index];
        result.cities[first_index] = result.cities[second_index];
        result.cities[second_index] = tmp;
        
        return result;
        
    def crossovered(self, other):
        print("--------------");
        l = list(map(lambda x: int(x.name), self.cities));
        l.sort();
        l = map(lambda x: str(x), l)                
        j = []        
        for i in l:
            if i not in j:
                j.append(str(i));
        l = map(lambda x: str(x), j)                
        bef = len(list(l));
        
        n = len(self.cities);        
        first_index = random.randint(0, n-1-CROSSOVER_SIZE);
        second_index = first_index + CROSSOVER_SIZE;
        
        same_cities = self.cities[first_index:second_index];
        rest_cities = list(x for x in other.cities if x not in same_cities);
        
        
        reassebmled = rest_cities[0:first_index] + same_cities + rest_cities[second_index:];
        
        result = copy.deepcopy(self);
        result.cities = copy.deepcopy(reassebmled);   
        
        l = list(map(lambda x: int(x.name), result.cities));
        l.sort();
        l = map(lambda x: str(x), l)                
        j = []        
        for i in l:
            if i not in j:
                j.append(str(i));
        aft = len(j)
        print(bef - aft)
        
        return result;

class Generation:
    members = []    
    def __init__(self, cities):
        for i in range(GENERATION_SIZE):
            self.members.append(Path(cities))
        
    def sort(self):
        self.members.sort(key = lambda x: x.length())
        
    def __repr__(self):
        return "<" + "; ".join(map(lambda x: str(x.length()), self.members)) + ">";
        
    def generateNext(self):
        g = copy.deepcopy(self);
        g.sort()
        survive_count = GENERATION_SIZE - MUTATE_COUNT - CROSSOVER_COUNT;
        g.members = g.members[0:survive_count];
        
        # mutate
        for i in range(MUTATE_COUNT):
            rand_index = random.randint(0, survive_count-1);
            mutated = g.members[rand_index].mutated()
            g.members.append(mutated)                
        
        # crossover
        for i in range(CROSSOVER_COUNT):
            father_index = random.randint(0, survive_count-1);
            mother_index = random.randint(0, survive_count-1);
            while father_index == mother_index:
                mother_index = random.randint(0, survive_count-1);    
            crossed = g.members[father_index].crossovered(g.members[mother_index])
            g.members.append(crossed)                
        
        g.sort();
                
        return g;
        
def distance(a, b):
    dx = a.x - b.x;
    dy = a.y - b.y;
    return math.sqrt(dx*dx+dy*dy);


def preprocessData(filename):
    with open(filename, 'r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=' ', quoting=csv.QUOTE_NONNUMERIC)
        data = [];
        for row in csv_reader:
            data.append(City(row[1], row[2], str(int(row[0]))))
                
        return data;

print("start");

def run():
    cities = preprocessData("berlin.tsp");
    
    g = Generation(cities)
    g.sort()

    history = [];
    i = 0;
    best = g.members[0].length();
    for j in range(1500):
        g = g.generateNext();  
        
        best_member = g.members[0];
        new_fitness = best_member.length();
        
        history.append(new_fitness)
            
        
        if(best > new_fitness):
            best = new_fitness;
            
            gra = int(122);
            plt.clf();    
            for c in best_member.cities:
                plt.plot([c.x], [c.y], color = "red", aa = True, marker = "o");
                plt.annotate(int(c.name), (c.x, c.y), color = "red");
            
            plt.title('Fitness = %.2fkm' % new_fitness);
            best_member.draw("#%02x%02x%02x" % (gra, gra, gra) );
            plt.savefig("fig%s.png" % i);
            i += 1;
            #print(g)
    #plt.clf();    
    #plt.plot(history);    
    #plt.savefig("histogram.png");
    
    return history

runs = []    
for i in range(10):
    runs.append(run());
    print("run", i)    
plt.clf();    
plt.ylim([0,30000])
plt.plot(list(map(lambda x: float(sum(x))/len(x), zip(*runs))));    
plt.savefig("avg_histogram.png");
        

print("end");