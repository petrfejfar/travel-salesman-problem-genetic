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

Travelling salesman problem is NP-complete problem, so proposed algorithm is from evolutionary family.

### Genetic algorithm design

We use stationary model with tournament selection strategy.

TODO what is stationary model

TODO what is tournament selection strategy

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

Crossover is TODO.

### Genetic algorithm parameters <a name="parameters"></a>

TODO tell what each parameter means

- *N* is population size
- *M* is mutation rate
- *C* is crossover rate
- *C<sub>min</sub>* is minimal crossover size
- *C<sub>max</sub>* is maximal crossover size

### Automatic setting parameters

We choose for tuning parameters use genetic algorithm. We use different design than **TSP(** ... **)**. Difference is in initial TODO

## Results <a name="results"></a>

By manual tuning of parameters we were able to get best result about **9k** fitness on test data.

By using genetic algorithm to determine algorithm parameters we were able to get best result as **11216,56**.

![Best path](/doc/img/best_result.png "Best path")

We use for that result generated parameters:
- Population size of 0
- Mutation count of 0
- Crossover count of 0
- Minimal crossover size of 0
- Maximal crossover size of 0

Histogram of best parameters algorithm is below.

![Best algorithm - fitness histogram](/doc/img/best_alg_fitnes_hist.png "Best algorithm - fitness histogram")
