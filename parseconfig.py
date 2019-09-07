"""
Mark Fraser
m_fraser3@u.pacific.edu
COMP 151:  Project 1
"""

from configparser import (
    ConfigParser
)

from constants import (
    CONFIG_FILE,
    ELITIST,
    KPOINT,
    NUM_COLUMNS,
    TOURNAMENT,
    UNIFORM
)

from re import (
    split
)

from sys import (
    exit
)


def parseArguments():
    config_object = ConfigParser()
    config_object.read(CONFIG_FILE)

    financial_data = parseFinancialData(config_object)
    num_chromosomes = parseNumChromosomes(config_object)
    num_generations = parseNumGenerations(config_object)
    selection_algorithm = parseSelectionAlgorithm(config_object)
    selection_percent = parseSelectionPercent(config_object)
    crossover_algorithm = parseCrossoverAlgorithm(config_object)
    initial_mutation_rate = parseMutationRate(config_object)
    decrease_rate = parseMutationDecreaseRate(config_object)

    return (financial_data, num_chromosomes, num_generations,
            selection_algorithm, selection_percent, crossover_algorithm,
            initial_mutation_rate, decrease_rate)


def parseFinancialData(config_object):
    # open file
    file_name = getConfigFieldValue(config_object, 'file', 'FINANCIALDATA',
                                    fallback='DEFAULT')

    file = open(file_name, 'r')
    if file is None:
        exit('unable to open ' + file_name)

    # process and verify file formatting
    contents = file.readlines()
    financial_data = []
    for line in contents:
        line = line.replace('\n', '')
        data = split('\s+', line)
        if len(data) is not NUM_COLUMNS:
            exit('invalid row of data: ' + str(data) + ' ' + line)
        financial_data += [data]

    financial_data = convertStrArrayToFloats(financial_data)

    return financial_data


def parseNumChromosomes(config_object):
    num_chromosomes = getConfigFieldValue(config_object, 'numchromosomes',
                                            'ALGORITHM', fallback='DEFAULT')

    return int(num_chromosomes)


def parseNumGenerations(config_object):
    num_generations = getConfigFieldValue(config_object, 'numgenerations',
                                            'ALGORITHM', fallback='DEFAULT')

    num_generations = int(num_generations)
    if num_generations <= 0:
        exit('invalid number of generations (must be > 0): ' + num_generations)

    return num_generations


def parseSelectionAlgorithm(config_object):
    selection_algorithm = getConfigFieldValue(config_object, 'selectionalg',
                                                'ALGORITHM', fallback='DEFAULT')

    if selection_algorithm != ELITIST and \
                                        selection_algorithm != TOURNAMENT:
        exit('invalid selection algorithm provided (not \'elitist\' or' +
            '\'tournament\'): ' + selection_algorithm)

    return selection_algorithm


def parseSelectionPercent(config_object):
    selection_percent = getConfigFieldValue(config_object, 'selectionper',
                                                'ALGORITHM', fallback='DEFAULT')

    selection_percent = float(selection_percent)

    if selection_percent <= 0 or 1 <= selection_percent:
        exit('invalid selection percentage (not between 0 and 1): ' +
            str(selection_percent))

    return selection_percent


def parseCrossoverAlgorithm(config_object):
    crossover_algorithm = getConfigFieldValue(config_object, 'crossoveralg',
                                                'ALGORITHM', fallback='DEFAULT')

    if crossover_algorithm != UNIFORM and \
                                        crossover_algorithm != KPOINT:
        exit('invalid crossover algorithm provided (not \'uniform\' or' +
            '\'kpoint\'): ' + crossover_algorithm)

    return crossover_algorithm


def parseMutationRate(config_object):
    mutation_rate = getConfigFieldValue(config_object, 'initmutation',
                                                'ALGORITHM', fallback='DEFAULT')

    mutation_rate = float(mutation_rate)

    if mutation_rate <= 0 or 1 <= mutation_rate:
        exit('invalid intial mutation rate (not between 0 and 1): ' +
            str(mutation_rate))

    return mutation_rate


def parseMutationDecreaseRate(config_object):
    decrease_rate = getConfigFieldValue(config_object, 'ratedecrease',
                                                'ALGORITHM', fallback='DEFAULT')

    decrease_rate = float(decrease_rate)

    if decrease_rate <= 0 or 1 <= decrease_rate:
        exit('invalid mutation decrease rate (not between 0 and 1): ' +
            str(decrease_rate))

    return decrease_rate


def getConfigFieldValue(config, field, section, fallback=None):
    value = config[section].get(field)
    if (value is None or value is '') and (fallback is not None):
        value = config[fallback].get(field)
    
    if value is None or value is '':
        exit('no value found for ' + field + ' in ' + section + ' and no' +
            + ' fallback provided or found')

    return value


def convertStrArrayToFloats(data):
    for i in range(len(data)):
        for j in range(len(data[i])):
            data[i][j] = float(data[i][j])

    return data