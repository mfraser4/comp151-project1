"""
Mark Fraser
m_fraser3@u.pacific.edu
COMP 151:  Project 1

Constants shared across multiple files and/or global to module
"""

# config file
CONFIG_FILE = 'config.ini'  # configuration file path

# financial data formatting
NUM_COLUMNS = 3             # number of columns in financial data file
DAY_ONE = 0                 # index for change in percentage of first day
DAY_TWO = 1                 # index for change in percentage of second day
PROFIT = 2                  # index for profits if recommended BUY

# chromosome constants
SHORT = 0                   # value of recommendation to short stock
BUY = 1                     # value of recommendation to purchase stock
VALID_PERCENTAGE = 100      # absolute value of valid percentage range

# selection algorithm constants
ELITIST = 'elitist'         # string type for elitist selection algorithm
TOURNAMENT = 'tournament'   # string type for tournament selection algorithm

# crossover algorithm constants
UNIFORM = 'uniform'         # string type for uniform crossover algorithm
KPOINT = 'kpoint'           # string type for kpoint crossover algorithm

# output constants
MILESTONE_GENERATION = 10   # generation increment to display intermediary data

# fitness constants
MATCH_NOT_FOUND = -5000     # fitness score for chromosome with no matches