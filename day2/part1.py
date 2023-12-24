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
    values = {
        "rock": 1,
        "paper": 2,
        "scissor": 3
    }
    
    def __init__(self, games, playerA, playerB) -> None:
        self.games = games
        self.playerA = playerA
        self.playerB = playerB
        
        
    def Score(self):
        spa, spb = 0 ,0
        for a,b in self.games:
            if self.playerA[a] == self.playerB[b]:
                spa += 3 + Game.values[self.playerA[a]]
                spb += 3 + Game.values[self.playerB[b]]
            elif Game.wins[self.playerA[a]] == self.playerB[b]:
                spb += 6 + Game.values[self.playerB[b]]
                spa += Game.values[self.playerA[a]]
            else:
                spa += 6 + Game.values[self.playerA[a]]
                spb += Game.values[self.playerB[b]]

        return (spa, spb)


if __name__ == '__main__':
    input = readInput("input.txt")
    playerA = {
        "A": "rock",
        "B": "paper",
        "C": "scissor"
    }

    playerB = {
        "X": "rock",
        "Y": "paper",
        "Z": "scissor"
    }
    scoreA, scoreB = Game(input, playerA, playerB).Score()
    print(scoreB)