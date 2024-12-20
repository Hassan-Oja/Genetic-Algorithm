import random

POPULATION_SIZE = 20
GENE_LENGTH = 10 
MUTATION_RATE = 0.01
GENERATIONS = 100

def fitness_function(x):
    return x ** 2

def decode_chromosome(chromosome):
    return int("".join(map(str, chromosome)), 2)

def generate_population():
    return [
        [random.randint(0, 1) for _ in range(GENE_LENGTH)]
        for _ in range(POPULATION_SIZE)
    ]

def evaluate_fitness(population):
    return [fitness_function(decode_chromosome(individual)) for individual in population]


def select_parents(population, fitness):
    parents = []
    for _ in range(len(population)):
        i, j = random.sample(range(len(population)), 2)
        parents.append(population[i] if fitness[i] > fitness[j] else population[j])
    return parents

def crossover(parent1, parent2):
    point = random.randint(1, GENE_LENGTH - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

def mutate(chromosome):
    for i in range(GENE_LENGTH):
        if random.random() < MUTATION_RATE:
            chromosome[i] = 1 - chromosome[i]  
    return chromosome

def genetic_algorithm():
    population = generate_population()
    
    for generation in range(GENERATIONS):
        fitness = evaluate_fitness(population)
        
        best_individual = population[fitness.index(max(fitness))]
        best_value = decode_chromosome(best_individual)
        print(f"Generation {generation}: Best Value = {best_value}, Fitness = {max(fitness)}")
        
        parents = select_parents(population, fitness)
        
        next_population = []
        for i in range(0, len(parents), 2):
            parent1, parent2 = parents[i], parents[min(i+1, len(parents)-1)]
            child1, child2 = crossover(parent1, parent2)
            next_population.append(mutate(child1))
            next_population.append(mutate(child2))
        
        population = next_population
    
    fitness = evaluate_fitness(population)
    best_individual = population[fitness.index(max(fitness))]
    return decode_chromosome(best_individual), max(fitness)

best_solution, best_fitness = genetic_algorithm()
print(f"Best Solution Found: {best_solution} with Fitness: {best_fitness}")
