"""
Mark Fraser
m_fraser3@u.pacific.edu
COMP 151:  Project 1
"""

from chromosome import (
    Chromosome
)

from constants import (
    BUY,
    DAY_ONE,
    DAY_TWO,
    ELITIST,
    KPOINT,
    MATCH_NOT_FOUND,
    MILESTONE_GENERATION,
    PROFIT,
    TOURNAMENT,
    UNIFORM
)

from math import (
    ceil
)

from operator import (
    itemgetter
)

from random import (
    choice,
    gauss,
    randint,
    random
)

from sys import (
    exit
)


def runGeneticAlgorithm(finances, num_chromosomes, num_generations,
        selection_algorithm, selection_percent, init_mutation_rate,
        crossover_algorithm, decrease_rate):
    # initialize algorithm variables
    best_chromosome = None
    curr_generation = 1
    mutation_rate = init_mutation_rate
    chromosomes = generateChromosomePopulation(num_chromosomes)
    
    while curr_generation <= num_generations:
        fitness_dict = {}   # stores <K,V> pair of chromosome and fitness score

        # gather fitness data for current chromosomes
        for chromosome in chromosomes:
            fitness_dict[chromosome] = calculateFitnessScore(chromosome,
                                                                finances)

        rankings = sorted(fitness_dict.items(), key=lambda i: i[1],
                            reverse=True)

        # intermediary command output every MILESTONE_GENERATION generations
        if curr_generation % MILESTONE_GENERATION == 0:
            fitness_scores = fitness_dict.values()
            print('Generation ' + str(curr_generation) + ':\n' +
                    '    max fitness score:  ' + str(max(fitness_scores)) + '\n'
                    + '    min fitness score:  ' + str(min(fitness_scores)) +
                    '\n    mean fitness score: ' + str(average(fitness_scores))
                    + '\n\n')

        if curr_generation == num_generations:
            best_chromosome = rankings[0]
        else:
            chromosomes = generateNextGeneration(rankings,
                                                    selection_algorithm,
                                                    selection_percent,
                                                    crossover_algorithm,
                                                    num_chromosomes,
                                                    mutation_rate)

            mutation_rate = mutation_rate * (1 - decrease_rate)

        curr_generation = curr_generation + 1

    return best_chromosome


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


def average(array):
    return sum(array) / len(array)


def generateNextGeneration(rankings, selection_algorithm, selection_percent,
                            crossover_algorithm, num_chromosomes,mutation_rate):
    selected_chromosomes = runSelectionAlgorithm(rankings,
                                                    selection_algorithm,
                                                    selection_percent)

    next_gen_chromosomes = runCrossoverAlgorithm(selected_chromosomes,
                                                    crossover_algorithm,
                                                    num_chromosomes)

    next_gen_chromosomes = performMutations(next_gen_chromosomes, mutation_rate)

    return next_gen_chromosomes


def runSelectionAlgorithm(rankings, selection_algorithm,
                                            selection_percent):
    if selection_algorithm == ELITIST:
        chromosomes = runElitistAlgorithm(rankings, selection_percent)
    elif selection_algorithm == TOURNAMENT:
        chromosomes = runTournamentAlgorithm(rankings, selection_percent)
    else:
        exit('selection algorithm not supported: ' + selection_algorithm)

    return chromosomes


def runElitistAlgorithm(rankings, selection_percent):
    cutoff_index = ceil(len(rankings) * selection_percent)
    chromosomes = [c[0] for c in rankings]
    return chromosomes[:cutoff_index]


def runTournamentAlgorithm(rankings, selection_percent):
    i = 0
    chromosomes = []
    length = len(rankings)
    num_tournaments = ceil(length * selection_percent)

    # check if tournament can be held
    if length * selection_percent <= 1:
        exit('unable to hold tournament: not enough chromosomes')

    # hold num_tournaments tournaments
    while i <= num_tournaments:
        c1 = rankings[randint(0, length-1)]
        c2 = rankings[randint(0, length-1)]
        
        # ensure uniqueness of chromosomes
        if c1 != c2:
            if c1[1] > c2[1]:
                chromosomes.append(c1[0])
            else:
                chromosomes.append(c2[0])

            i = i + 1

    return chromosomes


def runCrossoverAlgorithm(chromosomes, crossover_algorithm,
                            num_total_chromosomes):
    if crossover_algorithm == UNIFORM:
        chromosomes = runUniformAlgorithm(chromosomes, crossover_algorithm,
                            num_total_chromosomes)
    elif crossover_algorithm == KPOINT:
        chromosomes = runKpointAlgorithm(chromosomes, crossover_algorithm,
                            num_total_chromosomes)
    else:
        exit('crossover algorithm not supported: ' + crossover_algorithm)

    return chromosomes


def runUniformAlgorithm(sample_chromosomes, crossover_algorithm,
                            num_total_chromosomes):
    num_sample_chromosomes = len(sample_chromosomes)
    if num_sample_chromosomes <= 1:
        exit('not enough sample chromosomes to perform uniform crossover' +
                ' (must have >= 2 chromosomes)')
    
    chromosomes = sample_chromosomes # set of chromosomes to return

    while len(chromosomes) != num_total_chromosomes:
        c1 = sample_chromosomes[randint(0, num_sample_chromosomes-1)]
        c2 = sample_chromosomes[randint(0, num_sample_chromosomes-1)]

        # ensure uniqueness of chromosomes
        if c1 != c2:
            lb1 = choice([c1.getLowerBoundDayOne(), c2.getLowerBoundDayOne()])
            ub1 = choice([c1.getUpperBoundDayOne(), c2.getUpperBoundDayOne()])
            lb2 = choice([c1.getLowerBoundDayTwo(), c2.getLowerBoundDayTwo()])
            ub2 = choice([c1.getUpperBoundDayTwo(), c2.getUpperBoundDayTwo()])
            rec = choice([c2.getRecommendation(), c2.getRecommendation()])

            chromosomes.append(Chromosome(lb1, ub1, lb2, ub2, rec))

    return chromosomes


def runKpointAlgorithm(sample_chromosomes, crossover_algorithm,
                            num_total_chromosomes):
    num_sample_chromosomes = len(sample_chromosomes)
    if num_sample_chromosomes <= 1:
        exit('not enough sample chromosomes to perform kpoint crossover' +
                ' (must have >= 2 chromosomes)')
    
    chromosomes = sample_chromosomes # set of chromosomes to return

    while len(chromosomes) != num_total_chromosomes:
        c1 = sample_chromosomes[randint(0, num_sample_chromosomes-1)]
        c2 = sample_chromosomes[randint(0, num_sample_chromosomes-1)]

        # ensure uniqueness of chromosomes
        if c1 != c2:
            lb1 = c1.getLowerBoundDayOne()
            ub1 = c1.getUpperBoundDayOne()
            lb2 = c2.getLowerBoundDayTwo()
            ub2 = c2.getUpperBoundDayTwo()
            rec = c2.getRecommendation()

            chromosomes.append(Chromosome(lb1, ub1, lb2, ub2, rec))

    return chromosomes


def performMutations(next_gen_chromosomes, mutation_rate):
    mu = 0
    sigma = 1.5
    chromosomes = []

    for chromosome in next_gen_chromosomes:
        # TODO this breaks encapsulation, but is more concise
        data = chromosome.data
        gene_range = len(data) - 1  # confines range to percentage bound values
        for i in range(gene_range):
            # check whether to mutate chromosome
            if random() <= mutation_rate:
                data[i] = gauss(mu, sigma)

        # create chromosome with (potentially new) data
        chromosomes.append(Chromosome(data[0], data[1], data[2], data[3],
                                        data[4]))

    return chromosomes