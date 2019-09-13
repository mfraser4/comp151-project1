"""
Mark Fraser
m_fraser3@u.pacific.edu
COMP 151:  Project 1

A genetic learning algorithm program that analyzes 2-day chart patterns in
financial data 
"""

from geneticalgorithm import(
    runGeneticAlgorithm
)

from parseconfig import (
    parseArguments
)

from sys import (
    exit
)


__author__ = "Mark Fraser"


def main():
    finances, num_chromosomes, num_generations, selection_algorithm, \
    selection_percent, crossover_algorithm, init_mutation, decrease_rate = \
                                                                parseArguments()

    chromosome, fitness = runGeneticAlgorithm(finances,
                                                num_chromosomes,
                                                num_generations,
                                                selection_algorithm,
                                                selection_percent,
                                                init_mutation,
                                                crossover_algorithm,
                                                decrease_rate)

    # print best chromosome settings and fitness score
    print('Final result:\n' +
            '-------------')
    chromosome.print()
    print('Fitness score:  ' + str(fitness))


if __name__ == "__main__":
    main()
else:
    exit("use as module not supported")