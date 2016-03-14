# Travelling saleman problem - genetic algorithm

Petr Fejfar, pfejfar \_at\_ gmail.com

---

## Introduction

This task is lab assignment 3 for Learning systems course at Mälardalen University Sweden - Erasmus+ program 2016.

## Task definition

We are solving classical travelling salesman problem on given test data set by genetic algorithm.

We need find path between the cities to visit each city only once. We are trying to find as short path as possible.

By task definition we need to answer:

1. Explain the important operations of the employed algorithm (e.g. GA) to solve this problem
    - Answer is in section [Approach](#approach)
2. Explain the representation of the individual solutions in your algorithm.
    - Answer is in section [Population](#population)
3. Give the equation of the fitness function used by your algorithm.
    - Answer is in section [Fitness](#fitness)
4. Give the parameters used in your algorithm. Examples: population size, crossover rate…
    - Answer is in section [Genetic algorithm parameters](#parameters)
5. Illustrate how performance of the population evolves with generations (preferably with a figure)
    - Answer is in section [Results](#results)
6. Show the best result obtained by your algorithm (the order of locations to visit and the total distance of this route).
    - Answer is in section [Results](#results)

### Data set <a name="dataset"></a>

Data set consist of 52 cities with name and position.

| First column  | Second column | Third column  |
| ------------- |---------------| --------------|
| City name     | x position    | y position    |


Example:

    1 565.0 575.0
    2 25.0 185.0
    3 345.0 750.0
    4 945.0 685.0
    ...


## Approach <a name="approach"></a>

Travelling salesman problem is NP-complete problem. We use as approximation algorithm from evolutionary family.

### Genetic algorithm design

We use stationary model with tournament linear order strategy.

In stationary model we are using stable set of population. Every population we alter only subset of this population. Best members of population survives to next generation.

In linear order strategy we choose the best individuals to evolve new population.

#### Population <a name="population"></a>

[Data set](#dataset) is reprenting *G = (V, E)*, where *V* are cities and *E* are path between them. We set distance function as Euclidean distance *d(e) = d(a, b) = sqrt( (a<sub>x</sub>-b<sub>x</sub>)<sup>2</sup> + (a<sub>y</sub>-b<sub>y</sub>)<sup>2</sup> )*, where *e&#8712;E.* and *(a, b) = e*.

By member *M&#8834;E* we mean Hamiltonian path on graph *G* and population *P* is set of members *M&#8834;P*. Members are easily represented as permutation of *V*.

#### Fitness <a name="fitness"></a>

We set fitness of member *M* as function *f(M) = &#931;<sub>e&#8834;M</sub> f(e)*, therefore as path length.

#### Cycle

Algorithm cycle we set as below:

function **TSP(** *T*, *N*, *M*, *C*, *C<sub>min</sub>*, *C<sub>max</sub>* **)**:

1. Generate initial population.
2. Sort population by fitness function.
3. Remove last *C* population members.
4. Generate new members by crossover of first *(N-C)* members.
5. Mutate *M* new members created in previous step.
6. Sort population by fitness function.
7. If time of simulation is greater than *T* return fitness of first member, go to step 2 otherwise.

Where

- *T* is maximal time of simulation
- *N* is population size
- *M* is mutation rate
- *C* is crossover rate
- *C<sub>min</sub>* is minimal crossover size
- *C<sub>max</sub>* is maximal crossover size

#### Initial population, crossover and mutation

Initial population members are generated as random Hamiltonian paths on graph *G*. This is done easily as generting random permutation of **V**.

Mutation is done by swapping two elements in permutation.

Crossover is done by taking 2 parent members and generation offspring from them. Generation is done by taking random fixed sizes sequence in *parent A* and copying to offspring. Then we takes rest of permutation from *parent B* and fill offspring in same order as it was in *parent A*. By this way we create valid permutation.

Example (choose sequence of length 3 on index 2):

| Member/permutation | p<sub>0</sub> | p<sub>1</sub> | p<sub>2</sub> | p<sub>3</sub> | p<sub>4</sub> | p<sub>5</sub> | p<sub>6</sub> |
| ------------------ | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| **Parent A**       | 7             | 3             | **5**         | **2**         | **1**         | 6             | 4             |
| **Parent B**       | 1             | *6*           | *4*           | 2             | *3*           | 5             | *7*           |
| **Offspring**      | *6*           | *4*           | **5**         | **2**         | **1**         | *3*           | *7*           |

### Genetic algorithm parameters <a name="parameters"></a>

Choose of right parameters has huge impact on simulation performance.

*N* is population size and by increasing *N* we slower the generation, but if we use small population size we can not transfer information about good member to next generation.

*M* is mutation rate. By increasing it we increase chance to tweak result in longer runs. In early stages of simulation it has lower impact on improving fitness than crossover. This is **O(*1*)** operation.

*C* is crossover rate. By increasing it we speed up approach to best fitness in early stage of simulation. In later phase of simulation there is no huge impact. This is because in early stage is bigger chance to find big sequence, from *parent A* which update result. In later phases only smaller sequence will improve result - this is basically mutation. Crossover is **O(*N*)** operation so is slowest part in generation next population. It has impact on speed of generation.

*C<sub>min</sub>* is minimal crossover size and *C<sub>max</sub>* is maximal crossover size. We need to find proper value. Too small interval has same properties as mutation and to big interval has same properties as crossover. So there is trade off in this parameter.

### Automatic setting parameters

We choose for tuning parameters use genetic algorithm. We use different design than **TSP(** ... **)**. Difference we use only generational model. Generational model generate new initial population every population. This model was chosen because of lack of time on this task. In future we want to tweak this model by adding mutation and crossover.

Members are parameters for **TSP(** ... **)**. Fitness in this case is best fitness of **TSP(** ... **)** in time *T*. We chose *T* to 300sec. This is dependent of computer computational force. As reference machine we use Intel Core i7-4900MQ CPU @ 2.80 GHz, 32GB RAM, SSD disc.

## Results <a name="results"></a>

By manual tuning of parameters we were able to get best result about **9k** fitness on test data.

By using genetic algorithm to determine algorithm parameters we were able to get best result as **8007,56**.

![Best path](/doc/img/best_result.png "Best path")

We use for that result generated parameters:
- Population size of 2569
- Mutation count of 289
- Crossover count of 263
- Minimal crossover size of 0
- Maximal crossover size of 10

Histogram of best parameters algorithm is below.

![Best algorithm - fitness histogram](/doc/img/best_alg_fitnes_hist.png "Best algorithm - fitness histogram")

## Future work

This task was limited by time to work on it. In future we want to tweak parameters generation and let simulation work for longer time. We actually had best result around 7.7k, but we have unfortunately have no record of that.
