import random

# Fitness function: returns the number of conflicts in a given solution
def fitness(solution):
    conflicts = 0
    n = len(solution)
    for i in range(n):
        for j in range(i + 1, n):
            # Check if two queens are attacking each other
            if solution[i] == solution[j] or abs(solution[i] - solution[j]) == j - i:
                conflicts += 1
    return conflicts

# Generate a random solution (chromosome)
def generate_random_solution(n):
    return random.sample(range(n), n)

# Tournament selection: pick the best two solutions from a population
def tournament_selection(population, tournament_size=5):
    selected = random.sample(population, tournament_size)
    selected.sort(key=lambda x: fitness(x))
    return selected[0], selected[1]

# Single-point crossover: combines two parents to create an offspring
def crossover(parent1, parent2):
    n = len(parent1)
    crossover_point = random.randint(1, n - 1)
    offspring = parent1[:crossover_point] + parent2[crossover_point:]
    return offspring

# Mutation: randomly change a queen's position
def mutate(solution):
    n = len(solution)
    idx = random.randint(0, n - 1)
    new_position = random.randint(0, n - 1)
    solution[idx] = new_position
    return solution

# Genetic Algorithm to solve the 8-Queen problem
def genetic_algorithm(n=8, population_size=100, generations=1000, mutation_rate=0.1):
    # Initialize population with random solutions
    population = [generate_random_solution(n) for _ in range(population_size)]
    
    # Evolve the population
    for generation in range(generations):
        # Sort population by fitness (solutions with fewer conflicts are better)
        population.sort(key=lambda x: fitness(x))
        
        # Check if we have a solution with no conflicts (fitness == 0)
        if fitness(population[0]) == 0:
            print(f"Solution found in generation {generation}: {population[0]}")
            return population[0]
        
        # Create a new population (offspring)
        new_population = population[:2]  # Elitism: keep the best two solutions
        
        while len(new_population) < population_size:
            # Select two parents
            parent1, parent2 = tournament_selection(population)
            
            # Crossover to create offspring
            offspring = crossover(parent1, parent2)
            
            # Mutate the offspring with some probability
            if random.random() < mutation_rate:
                offspring = mutate(offspring)
            
            # Add the offspring to the new population
            new_population.append(offspring)
        
        # Replace the old population with the new one
        population = new_population
    
    # If no solution was found after all generations
    print("Solution not found in the given generations")
    return population[0]

# Run the Genetic Algorithm
solution = genetic_algorithm()
print("Final Solution: ", solution)
