"""
Mark Fraser
m_fraser3@u.pacific.edu
COMP 151:  Project 1

A genetic learning algorithm program that analyzes 2-day chart patterns in
financial data 
"""


__author__ = "Mark Fraser"
__version__ = "0.1.0"
__license__ = "N/A"


# global constants
CONFIG_FILE = 'config.ini'    # configuration file path
NUM_COLUMNS = 3                 # number of columns in financial data file


def main():
    finances, num_chromosomes, selection_algorithm, selection_percent, \
                    init_mutation, crossover, decrease_rate = parseArguments()

if __name__ == "__main__":
    main()