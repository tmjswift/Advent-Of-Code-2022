"""
--- Day 8: Treetop Tree House ---

determine whether there is enough tree cover here to keep a tree house hidden
"""

def isEdgeTree(xPos, yPos, xMax, yMax):
    if xPos == 0 or xPos == xMax-1 or yPos == 0 or yPos == yMax-1:
        return True
    else:
        return False

def treeVisible(treeMap, xPos, yPos, xMax, yMax):
    # print("Checking Tree", xPos, ",", yPos, "with height", treeMap[yPos][xPos])
    # trees on the edge are always visible
    if isEdgeTree(xPos, yPos, xMax, yMax):
        # print("Edge Tree - visible")
        return True

    # check if all trees between this tree and the edge are shorter than it
    
    # Check North
    # print("Check North")
    visible = True
    for j in range(yPos):
        if treeMap[j][xPos] >= treeMap[yPos][xPos]:
            # print("not visible")
            visible = False
            break
    if visible:
        # print("visible")
        return True
        
    # Check South
    # print("Check South")
    visible = True
    for j in range(yPos+1,yMax):
        if treeMap[j][xPos] >= treeMap[yPos][xPos]:
            # print("not visible")
            visible = False
            break
    if visible:
        # print("visible")
        return True
    
    # Check West
    # print("Check West")
    visible = True
    for i in range(xPos):
        if treeMap[yPos][i] >= treeMap[yPos][xPos]:
            # print("not visible")
            visible = False
            break
    if visible:
        # print("visible")
        return True
        
    # Check East
    # print("Check East")
    visible = True
    for i in range(xPos+1,xMax):
        if treeMap[yPos][i] >= treeMap[yPos][xPos]:
            # print("not visible")
            visible = False
            break
    if visible:
        # print("visible")
        return True
        
    # Tree is not visible
    return False
    

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


runningTotal = 0
for i in range(rows):
    for j in range(columns):
        if (treeVisible(treeMap, i, j, columns, rows)):
            runningTotal = runningTotal + 1
print("Number of visible trees:",runningTotal)


