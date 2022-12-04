"""
--- Day 3: Rucksack Reorganization ---

Find items that are in each group of rucksacks
"""

def getRucksackItem(rucksackContents):
    for item in rucksackContents[0]:
        if item in rucksackContents[1] and item in rucksackContents[2]:
            return item
    

inputFile = open("C:\\Users\\Tom\\Documents\\GitHub\\Advent-of-Code-2022\\day3\\input")

rucksackPriority = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

runningTotal = 0
groupIndex = 0
group = ["","",""]

for line in inputFile:
    if line != "\n":
        # get group
        group[groupIndex] = line.strip("\n")
        groupIndex = groupIndex + 1
        if groupIndex == 3:
            groupIndex = 0
            rucksackItem = getRucksackItem(group)
            priority = rucksackPriority.find(rucksackItem) + 1
            runningTotal = runningTotal + priority

print(runningTotal)
