"""
Mark Fraser
m_fraser3@u.pacific.edu
COMP 151:  Project 1
"""

from chromosome import (
    Chromosome
)

from random import (
    gauss,
    randint
)


# global constants
BUY = 1                 # value of recommendation to purchase stock
DAY_ONE = 0             # index for change in percentage of first day
DAY_TWO = 1             # index for change in percentage of second day
PROFIT = 2              # index for profits if recommended BUY
MATCH_NOT_FOUND = -5000 # fitness score for chromosome with no matches 


def runGeneticAlgorithm(finances, num_chromosomes, num_generations,
        selection_algorithm, selection_percent, init_mutation, crossover,
        decrease_rate):
    # initialize algorithm variables
    curr_generation = 1
    chromosomes = generateChromosomePopulation(num_chromosomes)
    
    while curr_generation <= num_generations:
        fitness_dict = {}   # stores <K,V> pair of chromosome and fitness score

        # gather fitness data for current chromosomes
        for chromosome in chromosomes:
            fitness_dict[chromosome] = calculateFitnessScore(chromosome,
                                                                finances)

        print(fitness_dict)
        break


def generateChromosomePopulation(num):
    chromosomes = []
    for i in range(num):
        chromosomes.append(generateRandomChromosome())

    return chromosomes


def generateRandomChromosome():
    mu = 0
    sigma = 1.5

    # generate random percentage ranges and a random recommendation
    lb1 = gauss(mu, sigma)
    ub1 = gauss(mu, sigma)
    lb2 = gauss(mu, sigma)
    ub2 = gauss(mu, sigma)
    rec = randint(0,1)

    return Chromosome(lb1, ub1, lb2, ub2, rec)


def calculateFitnessScore(chromosome, finances):
    fitness_score = 0
    isMatchFound = False

    print(str(chromosome.data[0]) + ' ' + str(chromosome.data[1]) + ' ' + str(chromosome.data[2]) + ' ' + str(chromosome.data[3]) + ' ' + str(chromosome.data[4]))

    for data in finances:
        if chromosome.isMatch(data[DAY_ONE], data[DAY_TWO]):
            isMatchFound = True
            if chromosome.getRecommendation() == BUY:
                fitness_score = fitness_score + data[PROFIT]
            else:
                fitness_score = fitness_score - data[PROFIT]

    # invalidate chromosome if it provides no matches for finances
    if not isMatchFound:
        fitness_score = MATCH_NOT_FOUND

    return fitness_score