import random

# Define the cities and their distances
cities = {
    'A': {'B': 12, 'C': 10, 'G': 12},
    'B': {'A': 12, 'C': 8, 'D': 12},
    'C': {'A': 10, 'B': 8, 'D': 11, 'E': 3, 'G': 9},
    'D': {'B': 12, 'C': 11, 'E': 11, 'F': 10},
    'E': {'C': 3, 'D': 11, 'F': 6, 'G': 7},
    'F': {'D': 10, 'E': 6, 'G': 9},
    'G': {'A': 12, 'C': 9, 'F': 9, 'E': 7}
}

# Genetic algorithm parameters
population_size = 50
generations = 1000
mutation_rate = 0.01

def calculate_route_distance(route):
    return sum(cities.get(route[i], {}).get(route[i + 1], float('inf')) for i in range(len(route) - 1))

def create_random_route(city_names):
    route = city_names[:]
    random.shuffle(route)
    return route

def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 2)
    child = parent1[:crossover_point]
    for city in parent2:
        if city not in child:
            child.append(city)
    return child

def mutate(route):
    if random.random() < mutation_rate:
        i, j = random.sample(range(len(route)), 2)
        route[i], route[j] = route[j], route[i]
    return route

# Initialize the population
population = [create_random_route(list(cities.keys())[1:]) for _ in range(population_size)]

# Main loop
for generation in range(generations):
    # Calculate the fitness of each route
    fitness = [1 / calculate_route_distance(route) for route in population]

    # Select parents for reproduction
    parents = random.choices(population, weights=fitness, k=population_size)

    # Create the next generation
    next_generation = []
    while len(next_generation) < population_size:
        parent1, parent2 = random.sample(parents, 2)
        child = crossover(parent1, parent2)
        child = mutate(child)
        next_generation.append(child)

    population = next_generation

# Find the best route in the final population
best_route = min(population, key=calculate_route_distance)
best_distance = calculate_route_distance(best_route)

# Print the best route and distance
print("Best Route:", ['A'] + best_route + ['A'])
print("Shortest Distance:", best_distance)