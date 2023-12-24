# https://adventofcode.com/2022/day/1

import os
import sys


def readInput(inputfile):
    elves = []
    lines = open(os.path.join(sys.path[0], inputfile), "r")
    sum = 0
    for line in lines:
        if line == "\n":
            elves.append(sum)
            sum = 0
            continue
        sum += int(line)
    return elves
    
def MaxCalories(elves):
    maxcalorie3 = sorted(elves, reverse= True)
    return sum(maxcalorie3[0:3])

if __name__ == '__main__':
    input = readInput("input.txt")
    print(MaxCalories(input))