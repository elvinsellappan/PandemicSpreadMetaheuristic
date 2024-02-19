import random
import csv
import statistics
import time;
class ViralReproductionOptimizer:

    def __init__(self, objective_function, population_size=100000, mutation_rate=0.9, crossover_rate=0.99, pandemic_rate=0.08, pandemic_spread_factor=0.9):
        self.objective_function = objective_function
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.pandemic_rate = pandemic_rate
        self.pandemic_spread_factor = pandemic_spread_factor

    def initialize_population(self):
        self.population = []
        for _ in range(self.population_size):
            solution = [random.uniform(-500, 500), random.uniform(-10, 10)]
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

                for i in range(2):
                    if random.random() < self.mutation_rate:
                        new_solution[i] += random.uniform(-0.1, 0.1)
                        new_solution[i] = max(-5, min(5, new_solution[i]))  # Ensure within range [-5, 5]


                fitness = self.objective_function(new_solution)
                new_solutions.append({"solution": new_solution, "fitness": fitness})

            self.population = new_solutions

        self.population.sort(key=lambda x: x["fitness"])
        return self.population[0]["solution"]

def rosenbrock_objective_function(solution):
    x, y = solution[0], solution[1]
    return (1 - x) ** 2 + 100 * (y - x ** 2) ** 2

if __name__ == "__main__":
    csv_file = "fireOutput.csv"
    with open(csv_file, mode='w', newline='') as file:
        #writer = csv.writer(file)
        #writer.writerow(["X", "Y", "Objective Value"])  # Write column headers
        start = time.time();
        for k in range(100):
            optimizer = ViralReproductionOptimizer(rosenbrock_objective_function)
            optimizer.initialize_population()
            best_solution = optimizer.optimize(1000)
            objective_value = rosenbrock_objective_function(best_solution)

            print("1000 Iterations Best Solution: x={}, y={}, Objective Value={}".format(best_solution[0],
                                                                                         best_solution[1],
                                                                                         objective_value))

            #writer.writerow([best_solution[0], best_solution[1], objective_value])

    end = time.time();
    print(time);