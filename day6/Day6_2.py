"""
--- Day 6: Tuning Trouble ---

Detect a start-of-message marker
"""

def checkCharacters(characterString):
    # check if all characters in string are unique
    for n in range(len(characterString)):
        if characterString.count(characterString[n]) > 1:
            return False
    # print(characterString)
    return True


inputFile = open("C:\\Users\\Tom\\Documents\\GitHub\\Advent-of-Code-2022\\day6\\input")
signal = inputFile.read().strip("\n")


for n in range(len(signal)):
    if checkCharacters(signal[n:n+14]):
        # message start is after start-of-message marker
        print(n+14)
        break
