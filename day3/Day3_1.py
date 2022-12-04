"""
--- Day 3: Rucksack Reorganization ---

Find items that are in both compartments of rucksacks
"""

def getRucksackItem(rucksackContents):
    midpoint = len(rucksackContents)//2 # integer division
    # print(rucksackContents)
    # print(midpoint)
    firstCompartmentContents = rucksackContents[:midpoint]
    secondCompartmentContents = rucksackContents[midpoint:]
    for item in firstCompartmentContents:
        if item in secondCompartmentContents:
            return item
    

inputFile = open("C:\\Users\\Tom\\Documents\\GitHub\\Advent-of-Code-2022\\day3\\input")

rucksackPriority = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

runningTotal = 0

for line in inputFile:
    if line != "\n":
        # get score
        rucksackItem = getRucksackItem(line.strip("\n"))
        priority = rucksackPriority.find(rucksackItem) + 1
        runningTotal = runningTotal + priority

print(runningTotal)
