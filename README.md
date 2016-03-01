# Travelling saleman problem - genetic algorithm

Petr Fejfar, pfejfar _at_ gmail.com

---

## Introduction

This task is lab assignment 3 for Learning systems course at Mälardalen University Sweden - Erasmus+ program 2016.

## Task definition

We are solving classical travelling salesman problem on given test data set by genetic algorithm.

We need find path between the cities to visit each city only once. We are trying to find as short path as possible.

By task definition we need to answer:
1. Explain the important operations of the employed algorithm (e.g. GA) to solve this problem (Answer in section [Approach](#approach))
2. Explain the representation of the individual solutions in your algorithm.
3. Give the equation of the fitness function used by your algorithm.
4. Give the parameters used in your algorithm. Examples: population size, crossover rate…
5. Illustrate how performance of the population evolves with generations (preferably with a figure)
6. Show the best result obtained by your algorithm (the order of locations to visit and the total distance of this route).

### Data set

Data set consist of 52 cities with name (first column) and position (second and third column).

Example:

    1 565.0 575.0
    2 25.0 185.0
    3 345.0 750.0
    4 945.0 685.0
    ...


## Approach <a name="approach"></a>

Travelling salesman problem is NP-complete problem, so proposed algorithm is from evolutionary family.

### Genetic algorithm architecture

#### Cycle

TSP(T, N, M, C, C<sub>min</sub>, C<sub>max</sub>)
1. Generate initial population.
2. Sort population by fitness function.
3. Remove last C population members.
4. Generate new members by crossover of first (N-C) members.
5. Mutate M new members created in previous step.
6. Sort population by fitness function.
7. If time of simulation i greater than T return fitness of first member, go to step 2 otherwise.

Where
- T is maximal time of simulation
- N is population size
- M is mutation rate
- C is crossover rate
- C<sub>min</sub> is minimal crossover size
- C<sub>max</sub> is maximal crossover size

#### Population

### Genetic algorithm parameters

### Automatic setting parameters

## Results

By manual tuning of parameters we were able to get best result about 9k fitness on test data.

By using genetic algorithm to determine algorithm parameters we were able to get best result as __*11216,56*__.

![Best path](/doc/img/best_result.png "Best path")

We use for that result generated parameters:
- Population size of 0
- Mutation count of 0
- Crossover count of 0
- Minimal crossover size of 0
- Maximal crossover size of 0

Histogram of best parameters algorithm is below.

![Best algorithm - fitness histogram](/doc/img/best_alg_fitnes_hist.png "Best algorithm - fitness histogram")
