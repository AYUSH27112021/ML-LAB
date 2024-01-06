import random

POPULATION_SIZE = 100
GENES = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890, .-;:_!"#%&/()=?@${[]}'''
TARGET = "I love GeeksforGeeks"

def create_individual():
    return [random.choice(GENES) for _ in range(len(TARGET))]

def calculate_fitness(individual):
    count=0
    for gene, target_gene in zip(individual, TARGET): 
        if gene != target_gene:
            count=count+1
    return count

def mate(parent1, parent2):
    child_chromosome = []
    for p1, p2 in zip(parent1, parent2):
        prob = random.random()
        if prob < 0.45:
            child_chromosome.append(p1)
        elif prob < 0.90:
            child_chromosome.append(p2)
        else:
            child_chromosome.append(random.choice(GENES))

    return child_chromosome

def main():
    generation = 1
    found = False
    population = [create_individual() for _ in range(POPULATION_SIZE)]

    while not found:
        population = sorted(population, key=calculate_fitness)

        if calculate_fitness(population[0]) <= 0:
            found = True
            break

        new_generation = population[:int(0.1 * POPULATION_SIZE)]

        for _ in range(int(0.9 * POPULATION_SIZE)):
            parent1 = random.choice(population[:50])
            parent2 = random.choice(population[:50])
            child = mate(parent1, parent2)
            new_generation.append(child)

        population = new_generation

        print(f"Generation: {generation}\tString: {''.join(population[0])}\tFitness: {calculate_fitness(population[0])}")
        generation += 1

    print(f"Generation: {generation}\tString: {''.join(population[0])}\tFitness: {calculate_fitness(population[0])}")

main()
