# https://adventofcode.com/2022/day/2

import os
import sys


def readInput(inputfile):
    game = []
    lines = open(os.path.join(sys.path[0], inputfile), "r")
    for line in lines:
        game.append(line.strip().split())
    return game


class Game:
    wins= {
        "rock": "paper",
        "paper": "scissor",
        "scissor": "rock"
    }
    loss = {
        "paper": "rock",
        "scissor": "paper",
        "rock": "scissor"
    }
    values = {
        "rock": 1,
        "paper": 2,
        "scissor": 3
    }
    
    def __init__(self, games, playerA, strategy) -> None:
        self.games = games
        self.playerA = playerA
        self.strategy = strategy
        
    
    def StrategyScore(self):
        spa, spb = 0, 0
        for a, st in self.games:
            if self.strategy[st] == 'loose':
                spa += 6 + Game.values[self.playerA[a]]
                spb += Game.values[Game.loss[self.playerA[a]]]
            elif self.strategy[st] == 'draw':
                spa += 3 + Game.values[self.playerA[a]]
                spb += 3 + Game.values[self.playerA[a]]
            elif self.strategy[st] =="win":
                spa += 0 + Game.values[self.playerA[a]]
                spb += 6 + Game.values[Game.wins[self.playerA[a]]]
        return (spa, spb)



if __name__ == '__main__':
    input = readInput("input.txt")
    playerA = {
        "A": "rock",
        "B": "paper",
        "C": "scissor"
    }

    playerBStrategy = {
        "X": "loose",
        "Y": "draw",
        "Z": "win"
    }
    scoreA, scoreB = Game(input, playerA, playerBStrategy).StrategyScore()
    print(scoreB)