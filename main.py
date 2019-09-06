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
__version__ = "0.1.0"
__license__ = "N/A"


def main():
    finances, num_chromosomes, num_generations, selection_algorithm, \
    selection_percent, init_mutation, crossover, decrease_rate = \
                                                                parseArguments()

    runGeneticAlgorithm(finances,
                        num_chromosomes,
                        num_generations,
                        selection_algorithm,
                        selection_percent,
                        init_mutation,
                        crossover,
                        decrease_rate)


if __name__ == "__main__":
    main()
else:
    exit("use as module not supported")