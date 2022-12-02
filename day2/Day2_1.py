"""
--- Day 2: Rock Paper Scissors ---

Calculate score for playig RPS
"""

inputFile = open("C:\\Users\\Tom\\Documents\\GitHub\\Advent-of-Code-2022\\day2\\input")

# Opponent plays A for Rock, B for Paper, and C for Scissors. 
# You play X for Rock, Y for Paper, and Z for Scissors.
#
# Score is 1 for Rock, 2 for Paper, and 3 for Scissors
# plus 0 if you lost, 3 if the round was a draw, and 6 if you won
scoreLookup = {"A X": 4, "A Y": 8, "A Z": 3, "B X": 1, "B Y": 5, "B Z": 9, "C X": 7, "C Y": 2, "C Z": 6}
runningTotal = 0

for line in inputFile:
    if line != "\n":
        # get score
        play = line.strip("\n")
        runningTotal = runningTotal + scoreLookup[play]

print(runningTotal)
