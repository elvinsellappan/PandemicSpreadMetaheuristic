# PandemicSpreadMetaheuristic
The Pandemic Spread Algorithm(PSA) is a metaheuristic optimization algorithm inspired by the spread of viruses in biological systems. It mimics the transmission and evolution of viruses to optimize a given objective function. Developed for the FIRE program at the University of Maryland, College Park

Overview
The PSA algorithm is designed to solve optimization problems by simulating the spread of a virus among a population of candidate solutions. It maintains a population of potential solutions, where each solution represents a candidate solution to the optimization problem.

The algorithm iteratively improves these solutions by allowing them to "infect" each other, resulting in a process similar to natural selection and evolution. Through mutation, crossover, and pandemic spread, the population evolves over time to pinpoint optimal or near-optimal solutions.

Features
Pandemic Spread: Solutions in the population can be infected by a "virus," which spreads based on a predefined pandemic rate and spread factor.

Mutation and Crossover: Solutions undergo mutation and crossover operations to introduce diversity and exploration in the population.

Objective Function Optimization: The algorithm aims to optimize a given objective function by finding solutions that minimize or maximize it.

The files contain 4 files. An implementation of the PSA running against the Rosenbrock function, and another against the Egg Crate Function. The file also contains versions of the Genetic Algorithm running against the same functions for testing purposes. The Genetic Algorithm was modified from the GA found in the Opytimizer library.

