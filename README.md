# COMP 151 Project 1

Mark Fraser

m_fraser3@u.pacific.edu

# Table of Contents

1. [COMP 151 Project 1](#comp-151-project-1)
2. [Table of Contents](#table-of-contents)
3. [Usage](#usage)
    1. [Args](#args)
        1. [file](#file)
        2. [numchromosomes](#numchromosomes)
        3. [numgenerations](#numgenerations)
        4. [selectionalg](#selectionalg)
        5. [crossoveralg](#crossoveralg)
        6. [initmutation](#initmutation)
        7. [ratedecrease](#ratedecrease)
4. [Best Combinations](#best-combinations)
    1. [genAlgData1](#genalgdata1)
    2. [genAlgData2](#genalgdata2)
5. [Testing](#testing)
    1. [Debug Files](#debug-files)
    2. [Test Files](#test-files)

# Usage

To run the program, use the following command in the project's root directory.

On Windows (assuming running Python 3):

```
/PATH/TO/comp-151-project1$ python main.py
```

On Linux:

```
/PATH/TO/comp-151-project1$ python3 main.py
```

## Args

The program parameters can be set in `config.ini`.  The file `constants.py` acts
as an internal file for global constants and is not to be edited.

(NOTE:  The 'DEFAULT' category is meant as a fallback if no user args are
provided.  Add to the 'FINANCIALDATA' and 'ALGORITHM' parameter settings to run
personal configurations.)

### file

This is the file path to the financial data relative to the root directory.  For
this project, financial data files have been sorted into `financial_data/`.  If
the data does not conform to the specifications in the Project 1 GAs PDF file,
an error will be thrown with a corresponding error message.

### numchromosomes

The number of chromosomes in each generation.  This number must be greater than
0.  If the provided argument cannot be converted to an integer, an error will be
thrown.

### numgenerations

The number of generations to be run.  This number must be greater than 0.  If
the provided argument cannot be converted to an integer, an error will be
thrown.

### selectionalg

The selection algorithm to be used in the program.  If the provided argument is
not equal to any of the selection algorithm constants in `constants.py`, an
error for an invalid input will be thrown.  Currently valid input strings are:

```
elitist
tournament
```

### selectionper

The percentage of chromosomes to be selected for the next generation.  This
number must fall in the range (0,1].  However, if the selection percent is not
high enough to allow for two or more chromosomes to be selected, the crossover
algorithm will throw an error that is does not have enough chromosomes.*

*The crossover algorithm guarantees uniqueness of the two chromosomes being
selected



### crossoveralg

The crossover algorithm to be used in the program.  If the provided argument is
not equal to any of the crossover algorithm constants in `constants.py`, an
error for an invalid input will be thrown.  Currently valid input strings are:

```
uniform
kpoint
```

### initmutation

The initial mutation rate.  This number must be in the range [0,1].  A value of
0 indicates no mutation, and a value of 1 indicates every chromosome mutates.

### ratedecrease

The rate of decrease of mutation.  This number must be in the range [0,1).  A
value of 0 indicates no decrease in the mutation rate.  The number is not
allowed to equal 1 to prevent the mutation rate from reaching 0.  Roundoff error
is not protected by this algorithm and is unlikely to occur unless the program
is run with an initial mutation rate approaching 0 and rate of decrease
approaching 1.  In this scenario, the odds of mutation are already effectively
0 and is therefore not considered to be program-breaking.

# Best Combinations

## genAlgData1

The best result for `genAlgData1.txt` achieved thus far has been done with the
following parameters:

```
file = financial_data/genAlgData1.txt
numchromosomes = 50
numgenerations = 100
selectionalg = elitist
selectionper = 0.25
crossoveralg = kpoint
initmutation = 0.50
ratedecrease = 0.05
```

Result:

```
5145.41
```

The high mutation rate helps get the program out of a local optimum that was
observed with lower mutation rates (~4500).  The high elitist selection
retention rate also helps keep the results that break the local optimum.  The
kpoint algorithm choice was meant to keep bounds that worked exceptionally well
for certain days, as opposed to risk losing good combinations through uniform
crossover.

## genAlgData2

The best result for `genAlgData2.txt` achieved thus far has been done with the
following parameters:

```
file = financial_data/genAlgData2.txt
numchromosomes = 50
numgenerations = 100
selectionalg = elitist
selectionper = 0.25
crossoveralg = kpoint
initmutation = 0.50
ratedecrease = 0.05
```

Result:

```
455.51
```

# Testing

## Debug Files

Files that follow the regex expression `debug_*.txt` are files meant to help
illustrate the correctness of the genetic algorithm.  Provided below is a list
of the debug files and a short description of what the algorithm should output.

| File | Description |
|-----------------|------------------|
| debug_buy_negative_stock.txt | The ideal chromosome would buy all stock in the range [-3.0, -1.7] on day one and [-2.20, -0.05] for a profit of $14.90 |
| debug_buy_positive_stock.txt | The ideal chromosome would buy all stock in the range [1.7, 3.0] on day one and [0.05, 2.20] for a profit of $14.90  |
| debug_buy_stock.txt |  The ideal chromosome would buy all stock in the range [-1.7, 3.0] on day one and [-0.08, 2.20] for a profit of $11.90 |
| debug_short_negative_stock.txt | The ideal chromosome would short all stock in the range [-3.0, -1.7] on day one and [-2.20, -0.05] for a profit of $14.90 |
| debug_short_positive_stock.txt | The ideal chromosome would short all stock in the range [1.7, 3.0] on day one and [0.05, 2.20] for a profit of $14.90 |
| debug_short_stock.txt | The ideal chromosome would short all stock in the range [-1.0, 0.05] on day one and [-2.0, 0.5] for a profit of $14.60 |

## Test Files

The file `test_fitness_calculator.txt` has been written as a conveniently small
file with simple integers for easy calculation of the best chromosome's fitness
score after running for one generation (following the instructions from the
rubric).
