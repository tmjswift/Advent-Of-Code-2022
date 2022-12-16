"""
--- Day 9: Rope Bridge ---

calculate positions of rope ends
"""

def isAdjacent(headPosition, tailPosition):
    # adjacent if in same position, or one space away (including diagonally)
    xDistance = abs(headPosition[0] - tailPosition[0])
    yDistance = abs(headPosition[1] - tailPosition[1])
    
    if xDistance <= 1 and yDistance <= 1:
        return True
    else:
        return False


def moveHead(curentHeadPosition, direction):
    # head moves one space in the direction given
    if direction == "L":
        curentHeadPosition[0] = curentHeadPosition[0] - 1
    if direction == "R":
        curentHeadPosition[0] = curentHeadPosition[0] + 1
    if direction == "U":
        curentHeadPosition[1] = curentHeadPosition[1] - 1
    if direction == "D":
        curentHeadPosition[1] = curentHeadPosition[1] + 1
    

def moveTail(curentHeadPosition, currentTailPosition):
    # tail moves one step towards the head (including diagonally)
    newTailPosition = [currentTailPosition[0], currentTailPosition[1]]
    
    if curentHeadPosition[0] < currentTailPosition[0]:
        # move left
        newTailPosition[0] = currentTailPosition[0] - 1
    
    if curentHeadPosition[0] > currentTailPosition[0]:
        # move right
        newTailPosition[0] = currentTailPosition[0] + 1

    if curentHeadPosition[1] < currentTailPosition[1]:
        # move up
        newTailPosition[1] = currentTailPosition[1] - 1
 
    if curentHeadPosition[1] > currentTailPosition[1]:
        # move down
        newTailPosition[1] = currentTailPosition[1] + 1         
    
    return newTailPosition


inputFile = open("C:\\Users\\Tom\\Documents\\GitHub\\Advent-of-Code-2022\\day9\\input")

curentKnotPosition = [[0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]]

tailPositions = []
tailPositions.append(curentKnotPosition[9])

for line in inputFile:
    if line != "\n":
        movement = line.strip("\n")
        # print("-----")
        # print(movement)
        direction = movement.split(" ")[0]
        distance = int(movement.split(" ")[1])
        while distance > 0:
            moveHead(curentKnotPosition[0], direction)
            for i in range(1,10):
                if not isAdjacent(curentKnotPosition[i-1], curentKnotPosition[i]):
                    curentKnotPosition[i] = moveTail(curentKnotPosition[i-1], curentKnotPosition[i])
                    if curentKnotPosition[9] not in tailPositions:
                        tailPositions.append(curentKnotPosition[9])
            distance = distance - 1
        # for i in range(10):
        #     print("Knot", i, ":", curentKnotPosition[i])
        
print(len(tailPositions))

