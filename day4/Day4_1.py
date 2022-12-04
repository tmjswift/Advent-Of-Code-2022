"""
--- Day 4: Camp Cleanup ---

Find pairs of ranges where one range includes the other
"""

def checkRanges(range1, range2):
    range1Start, range1End = range1.split("-")
    range2Start, range2End = range2.split("-")
    
    # print(range1Start, range1End, range2Start, range2End)
    
    if int(range1Start) <= int(range2Start) and int(range1End) >= int(range2End):
        # print("range1 contains range2")
        return True
    
    if int(range2Start) <= int(range1Start) and int(range2End) >= int(range1End):
        # print("range2 contains range1")
        return True
    
    return False


inputFile = open("C:\\Users\\Tom\\Documents\\GitHub\\Advent-of-Code-2022\\day4\\input")

runningTotal = 0

for line in inputFile:
    if line != "\n":
        # get ranges
        ranges = line.strip("\n")
        range1, range2 = ranges.split(",")
        if checkRanges(range1, range2):
            runningTotal = runningTotal + 1

print(runningTotal)
