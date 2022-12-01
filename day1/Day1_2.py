"""
--- Day 1: Calorie Counting ---

Find the top3 elves which are carrying the most calories
"""

inputFile = open("C:\\Users\\Tom\\Documents\\GitHub\\Advent-of-Code-2022\\day1\\input")
mostCalories = [0,0,0]
currentElfCalories = 0



for line in inputFile:
    if line == "\n":
        # check if this elf is carrrying more than the 3rd most calories
        if currentElfCalories > mostCalories[2]:
            mostCalories[2] = currentElfCalories
            mostCalories.sort(reverse=True)
            #print(mostCalories)
        currentElfCalories = 0
    else:
        currentElfCalories = currentElfCalories + int(line.strip("\n"))

print(sum(mostCalories))
