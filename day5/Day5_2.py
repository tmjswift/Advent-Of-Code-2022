"""
--- Day 5: Supply Stacks ---

Rearrange stacks of crates
"""

def getInitialStacks(initialPosition):
    stacks = [[],[],[],[],[],[],[],[],[]]

    for line in initialPosition:
        for position in range(0, 33, 4):
            if line[position+1] != " ":
                stacks[position//4].append(line[position+1])
                
    # print(stacks)
    return stacks

def moveCrates(line, crateStacks):
    fromPos = line.find("from")
    toPos = line.find("to")
    
    numberOfCrates = int(line[5:fromPos])
    fromStack = int(line[fromPos+5:toPos]) - 1
    toStack = int(line[toPos+3:]) - 1
    
    # print(crateStacks[fromStack], crateStacks[toStack])
    
    cratesToMove = crateStacks[fromStack][:numberOfCrates]
    # crates are moved all in one go, so no need to reverse the list
    # cratesToMove.reverse()
    # print(cratesToMove)
    crateStacks[fromStack] = crateStacks[fromStack][numberOfCrates:]
    
    crateStacks[toStack] = cratesToMove + crateStacks[toStack]
    # print(crateStacks[fromStack], crateStacks[toStack])
    return crateStacks


inputFile = open("C:\\Users\\Tom\\Documents\\GitHub\\Advent-of-Code-2022\\day5\\input")

initialPosition = []
movesList = []

for line in inputFile:
    if "move" in line:
        movesList.append(line.strip("\n"))
    elif "[" in line:
        initialPosition.append(line.strip("\n"))

# print(initialPosition)
# print(movesList)

crateStacks = getInitialStacks(initialPosition)

for line in movesList:
    crateStacks = moveCrates(line, crateStacks)

answer = ""
for stack in crateStacks:
    answer = answer + stack[0]
    
print(answer)
