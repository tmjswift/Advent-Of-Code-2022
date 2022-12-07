"""
--- Day 7: No Space Left On Device ---

determine the total size of each directory
"""


def changeDirectory(currentDirectory, command):
    # Add an _ to the end of folder names to workaround paths with similar names
    if command == "$ cd /":
        newDirectory = "ROOT_"
    elif command == "$ cd ..":
        lastSlashPos = currentDirectory.rfind("/")
        newDirectory = currentDirectory[:lastSlashPos]
    else:
        folder = command[5:] + "_"
        newDirectory = currentDirectory + "/" + folder
    print("Changed Directory to:")
    print(newDirectory)
    return newDirectory

def processLS(fileList, currentDirectory, lsOutput):
    for item in lsOutput:
        if not item.startswith("dir "):
            fileSizeText, fileName = item.split(" ")
            fileSize = int(fileSizeText)
            filePath = currentDirectory + "/" + fileName + "_"
            if [filePath, fileSize] not in fileList:
                fileList.append([filePath, fileSize])
            # print("Found file ")
            # print(filePath)
    return

def getDirSize(directory, fileList):
    dirSize = 0
    for item in fileList:
        if item[0].startswith(directory):
            dirSize = dirSize + item[1]
    return dirSize


inputFile = open("C:\\Users\\Tom\\Documents\\GitHub\\Advent-of-Code-2022\\day7\\input")

currentDirectory = ""
fileList = []
directoryList = []
lsOutput = []

for line in inputFile:
    if line.startswith("$ cd"):
        processLS(fileList, currentDirectory, lsOutput)
        lsOutput = []
        currentDirectory = changeDirectory(currentDirectory, line.strip("\n"))
        if currentDirectory not in directoryList:
            directoryList.append(currentDirectory)
    if line.startswith("$ ls"):
        processLS(fileList, currentDirectory, lsOutput)
        lsOutput = []
    if not line.startswith("$"):
        lsOutput.append(line.strip("\n"))
# handle last command in file
processLS(fileList, currentDirectory, lsOutput)


directoryList.sort()
# for item in directoryList:
#     print(item)
# fileList.sort()
# for item in fileList:
#     print(item)

runningTotal = 0
for item in directoryList:
    dirSize = getDirSize(item, fileList)
    print(item, dirSize)
    if dirSize <= 100000:
        runningTotal = runningTotal + dirSize
print(runningTotal)