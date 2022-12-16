"""
--- Day 8: Treetop Tree House ---

find the best spot to build a tree house hidden
"""

def isEdgeTree(xPos, yPos, xMax, yMax):
    if xPos == 0 or xPos == xMax-1 or yPos == 0 or yPos == yMax-1:
        return True
    else:
        return False

def getScore(treeMap, xPos, yPos, xMax, yMax):
    # score is the number of trees visible in each direction multiplied together

    # trees on the edge have score 0
    if isEdgeTree(xPos, yPos, xMax, yMax):
        return 0

    # Check North
    northDistance = 0
    # work backwards from the nearest tree
    for j in range(yPos-1,-1,-1):
        northDistance = northDistance + 1
        if treeMap[j][xPos] >= treeMap[yPos][xPos]:
            break

    # Check South
    southDistance = 0
    for j in range(yPos+1,yMax):
        southDistance = southDistance + 1
        if treeMap[j][xPos] >= treeMap[yPos][xPos]:
            break
    
    # Check West
    westDistance = 0
    # work backwards from the nearest tree
    for i in range(xPos-1,-1,-1):
        westDistance = westDistance + 1
        if treeMap[yPos][i] >= treeMap[yPos][xPos]:
            break
    
    # Check East
    eastDistance = 0
    for i in range(xPos+1,xMax):
        eastDistance = eastDistance + 1
        if treeMap[yPos][i] >= treeMap[yPos][xPos]:
            break
        
    # Calculate score
    # print("Tree distances N S E W:",northDistance,southDistance,eastDistance,westDistance)
    return (northDistance * southDistance * westDistance * eastDistance)


inputFile = open("C:\\Users\\Tom\\Documents\\GitHub\\Advent-of-Code-2022\\day8\\input")

rows = 99
columns = 99
treeMap = [[0 for i in range(columns)] for j in range(rows)]
xPos = 0
yPos = 0


for line in inputFile:
    if line != "\n":
        xPos = 0
        for number in line.strip("\n"):
            treeMap[yPos][xPos] = int(number)
            xPos = xPos + 1
    # print(treeMap[yPos])
    yPos = yPos + 1


bestScore = 0
for i in range(rows):
    for j in range(columns):
        # print("----------")
        # print("Getting score for Tree",i,j)
        score = getScore(treeMap, i, j, columns, rows)
        # print("Score for tree",i,j,"is",score)
        if score > bestScore:
            bestScore = score
print("bestScore:",bestScore)


