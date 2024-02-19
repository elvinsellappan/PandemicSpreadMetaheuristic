import random
import csv
import math

# Objective function (Egg Crate)
def egg_crate(x, y):
    return x**2 + y**2 + 25 * (math.sin(x)**2 + math.sin(y)**2)

# Decode bitstring to real numbers for 2 dimensions
def decode(bounds, n_bits, bitstring):
    x_bits = bitstring[:n_bits]
    y_bits = bitstring[n_bits:]
    x = bounds[0] + int(''.join(map(str, x_bits)), 2) * (bounds[1] - bounds[0]) / (2**n_bits - 1)
    y = bounds[0] + int(''.join(map(str, y_bits)), 2) * (bounds[1] - bounds[0]) / (2**n_bits - 1)
    return x, y

# Tournament selection
def selection(pop, scores, k=3):
    selected = []
    for _ in range(len(pop)):
        candidates = random.sample(range(len(pop)), k)
        selected_agent = min(candidates, key=lambda x: scores[x])
        selected.append(pop[selected_agent])
    return selected

# Crossover two parents to create two children
def crossover(p1, p2, r_cross):
    c1, c2 = list(p1), list(p2)
    if random.random() < r_cross:
        point = random.randint(1, len(p1) - 1)
        c1[point:], c2[point:] = p2[point:], p1[point:]
    return c1, c2

# Mutation operator
def mutation(bitstring, r_mut):
    for i in range(len(bitstring)):
        if random.random() < r_mut:
            bitstring[i] = 1 - bitstring[i]

def genetic_algorithm(objective, bounds, n_bits, n_iter, n_pop, r_cross, r_mut, best_score):
    pop = [[random.randint(0, 1) for _ in range(2 * n_bits)] for _ in range(n_pop)]
    for gen in range(n_iter):
        decoded = [decode(bounds, n_bits, p) for p in pop]
        scores = [objective(*d) for d in decoded]
        for i in range(n_pop):
            if scores[i] < best_score:
                best, best_score = pop[i], scores[i]
        selected = selection(pop, scores)
        children = []
        for i in range(0, n_pop, 2):
            p1, p2 = selected[i], selected[i + 1]
            c1, c2 = crossover(p1, p2, r_cross)
            mutation(c1, r_mut)
            mutation(c2, r_mut)
            children.extend([c1, c2])
        pop = children
    return best, best_score

bounds = [-2 * math.pi, 2 * math.pi]

n_iter = 100

n_bits = 16

n_pop = 100

r_cross = 0.9

r_mut = 1.0 / (float(n_bits) * 2)  # Two dimensions

best, best_score = None, float('inf')

csv_file = "geneticAlgorithmEggCrateOutput.csv"
if __name__ == "__main__":
    csv_file = "geneticAlgorithmEggCrateOutput.csv"
    with open(csv_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        # Write the header row
        writer.writerow(['x', 'y', 'score'])

        # Perform the genetic algorithm search
        for i in range(100):
            best, score = genetic_algorithm(egg_crate, bounds, n_bits, n_iter, n_pop, r_cross, r_mut, best_score)
            output_tuple = decode(bounds, n_bits, best)

            # Write the data to the CSV file
            writer.writerow([output_tuple[0], output_tuple[1], score])

            # Print the best solution and its score
            print("Iteration:", i)
            print("Best Solution:", output_tuple)
            print("Best Score:", score)

    print("Data has been written to", csv_file)
