"""
Mark Fraser
m_fraser3@u.pacific.edu
COMP 151:  Project 1
"""

from constants import (
    VALID_PERCENTAGE
)

from sys import (
    exit
)


class Chromosome(object):
    """
    Stores the matching criteria for a chromosome, as well as the 
    recommendation and basic comparison methods
    """

    LB_DAY1 = 0             # lower bound day 1 index
    UB_DAY1 = 1             # upper bound day 1 index
    LB_DAY2 = 2             # lower bound day 2 index
    UB_DAY2 = 3             # upper bound day 2 index
    RECOMMENDATION = 4      # recommendation index

    def __init__(self, lb_day1, ub_day1, lb_day2, ub_day2, r):
        super(Chromosome, self).__init__()

        # enforce valid bound values
        if not self.boundsAreValid(lb_day1, ub_day1, lb_day2, ub_day2):
            exit('invalid percentage bound provided (range must be between -' +
                str(VALID_PERCENTAGE) + ' AND ' + str(VALID_PERCENTAGE) + '): '+
                str(lb_day1) + ' ' + str(ub_day1) + ' ' + str(lb_day2) + ' ' +
                str(ub_day2))
        
        # enforce contstraint that lower bound <= upper bound
        if lb_day1 > ub_day1:
            tmp = lb_day1
            lb_day1 = ub_day1
            ub_day1 = tmp

        if lb_day2 > ub_day2:
            tmp = lb_day2
            lb_day2 = ub_day2
            ub_day2 = tmp

        # enforce recommendation is valid
        if r != 0 and r != 1:
            exit("invalid recommendation provided: " + str(r))

        self.data = [lb_day1, ub_day1, lb_day2, ub_day2, r]

    def isMatch(self, day_one, day_two):
        # create local variables for conciseness of code
        LB_DAY1 = self.LB_DAY1
        UB_DAY1 = self.UB_DAY1
        LB_DAY2 = self.LB_DAY2
        UB_DAY2 = self.UB_DAY2

        if self.data[LB_DAY1] <= day_one <= self.data[UB_DAY1] and \
                            self.data[LB_DAY2] <= day_two <= self.data[UB_DAY2]:
            return True
        else:
            return False

    def getLowerBoundDayOne(self):
        return self.data[self.LB_DAY1]

    def getUpperBoundDayOne(self):
        return self.data[self.UB_DAY1]

    def getLowerBoundDayTwo(self):
        return self.data[self.LB_DAY2]

    def getUpperBoundDayTwo(self):
        return self.data[self.UB_DAY2]

    def getRecommendation(self):
        return self.data[self.RECOMMENDATION]

    def boundsAreValid(self, lb_day1, ub_day1, lb_day2, ub_day2):
        return abs(lb_day1) <= VALID_PERCENTAGE and \
                abs(ub_day1) <= VALID_PERCENTAGE and \
                abs(lb_day2) <= VALID_PERCENTAGE and \
                abs(ub_day2) <= VALID_PERCENTAGE

    def print(self):
        LB_DAY1 = self.LB_DAY1
        UB_DAY1 = self.UB_DAY1
        LB_DAY2 = self.LB_DAY2
        UB_DAY2 = self.UB_DAY2
        RECOMMENDATION = self.RECOMMENDATION

        print(str(self) + ':\n' +
                '    LB1:  ' + str(self.data[LB_DAY1]) + '\n' +
                '    UB1:  ' + str(self.data[UB_DAY1]) + '\n' +
                '    LB2:  ' + str(self.data[LB_DAY2]) + '\n' +
                '    UB2:  ' + str(self.data[UB_DAY2]) + '\n' +
                '    REC:  ' + str(self.data[RECOMMENDATION]) + '\n')
        