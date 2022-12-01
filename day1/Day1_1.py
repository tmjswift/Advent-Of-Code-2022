"""
--- Day 1: Calorie Counting ---

Find the elf which is carrying the most calories
"""

inputFile = open("C:\\Users\\Tom\\Documents\\GitHub\\Advent-of-Code-2022\\day1\\input")
mostCalories = 0
currentElfCalories = 0



for line in inputFile:
    if line == "\n":
        # check if this elf is carrrying the most calories
        if currentElfCalories > mostCalories:
            mostCalories = currentElfCalories
        currentElfCalories = 0
    else:
        currentElfCalories = currentElfCalories + int(line.strip("\n"))

print(mostCalories)
