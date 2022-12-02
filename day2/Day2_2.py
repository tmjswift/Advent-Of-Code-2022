"""
--- Day 2: Rock Paper Scissors ---

Calculate score for playig RPS
"""

inputFile = open("C:\\Users\\Tom\\Documents\\GitHub\\Advent-of-Code-2022\\day2\\input")

# Opponent plays A for Rock, B for Paper, and C for Scissors. 
# X means you lose, Y means you draw, and Z means you win.
#
# Score is 1 for Rock, 2 for Paper, and 3 for Scissors
# plus 0 if you lost, 3 if the round was a draw, and 6 if you won
scoreLookup = {"A X": 3, "A Y": 4, "A Z": 8, "B X": 1, "B Y": 5, "B Z": 9, "C X": 2, "C Y": 6, "C Z": 7}
runningTotal = 0

for line in inputFile:
    if line != "\n":
        # get score
        play = line.strip("\n")
        runningTotal = runningTotal + scoreLookup[play]

print(runningTotal)
