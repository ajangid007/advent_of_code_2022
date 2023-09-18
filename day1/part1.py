# https://adventofcode.com/2022/day/1

import os
import sys


def readInput(inputfile):
    elves = []
    lines = open(os.path.join(sys.path[0], inputfile), "r")
    calorieset = []
    for line in lines:
        if line == "\n":
            elves.append(calorieset)
            calorieset = []
        else:
            calorieset.append(int(line))
    return elves
    
def MaxCalories(elves):
    maxcalorie = 0
    for elve in elves:
        maxcalorie = max(maxcalorie, sum(elve))
    return maxcalorie

if __name__ == '__main__':
    input = readInput("input.txt")
    print(MaxCalories(input))