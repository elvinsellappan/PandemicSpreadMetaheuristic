import random
import csv
import statistics
import time
import math

class ViralReproductionOptimizer:

    def __init__(self, objective_function, dimensions=2, population_size=1000, mutation_rate=0.9, crossover_rate=0.99, pandemic_rate=0.08, pandemic_spread_factor=0.9):
        self.objective_function = objective_function
        self.dimensions = dimensions
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.pandemic_rate = pandemic_rate
        self.pandemic_spread_factor = pandemic_spread_factor

    def initialize_population(self):
        self.population = []
        for _ in range(self.population_size):
            solution = [random.uniform(-2 * math.pi, 2 * math.pi) for _ in range(self.dimensions)]  # Design variable range: [-2π, 2π]
            fitness = self.objective_function(solution)
            self.population.append({"solution": solution, "fitness": fitness})

    def pandemic_spread(self, solution):
        if random.random() < self.pandemic_rate:
            pandemic_solution = random.choice(self.population)["solution"]
            solution = [(sol + gene * self.pandemic_spread_factor) / (1 + self.pandemic_spread_factor) for sol, gene in zip(solution, pandemic_solution)]
        return solution

    def optimize(self, iterations):
        for _ in range(iterations):
            self.population.sort(key=lambda x: x["fitness"])
            best_solutions = self.population[:self.population_size // 2]

            new_solutions = []
            for best_solution in best_solutions:
                new_solution = self.pandemic_spread(best_solution["solution"].copy())

                for i in range(self.dimensions):
                    if random.random() < self.mutation_rate:
                        new_solution[i] += random.uniform(-0.1, 0.1)
                        new_solution[i] = max(-2 * math.pi, min(2 * math.pi, new_solution[i]))  # Ensure within range [-2π, 2π]

                fitness = self.objective_function(new_solution)
                new_solutions.append({"solution": new_solution, "fitness": fitness})

            self.population = new_solutions

        self.population.sort(key=lambda x: x["fitness"])
        return self.population[0]["solution"]

def egg_crate_objective_function(solution):
    x1, x2 = solution[0], solution[1]
    return x1**2 + x2**2 + 25 * (math.sin(x1)**2 + math.sin(x2)**2)

if __name__ == "__main__":
    csv_file = "eggCrateOutput.csv"
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        header = ["X1", "X2", "Objective Value"]
        writer.writerow(header)  # Write column headers
        start = time.time()
        for k in range(100):
            optimizer = ViralReproductionOptimizer(egg_crate_objective_function, dimensions=2)
            optimizer.initialize_population()
            best_solution = optimizer.optimize(1000)
            objective_value = egg_crate_objective_function(best_solution)

            print("1000 Iterations Best Solution:", best_solution)
            print("Objective Value:", objective_value)

            writer.writerow(best_solution + [objective_value])

    end = time.time()
    print("Execution Time:", end - start, "seconds")