"""
--- Day 10: Cathode-Ray Tube ---

draw image
"""

inputFile = open("C:\\Users\\Tom\\Documents\\GitHub\\Advent-of-Code-2022\\day10\\input")

cycle = 0
registerX = 1
crtOutput = ""


for line in inputFile:
    if line == "\n":
        break
    if line == "noop\n":
        # draw at current position
        if (cycle % 40) == registerX-1 or (cycle % 40) == registerX or (cycle % 40) == registerX+1:
            crtOutput = crtOutput + "#"
        else:
            crtOutput = crtOutput + " "
        cycle = cycle + 1
            
    else:
        instruction = line.strip("\n")
        if instruction.split(" ")[0] == "addx":
            # draw at current position
            if (cycle % 40) == registerX-1 or (cycle % 40) == registerX or (cycle % 40) == registerX+1:
                crtOutput = crtOutput + "#"
            else:
                crtOutput = crtOutput + " "
            cycle = cycle + 1

            # draw at current position
            if (cycle % 40) == registerX-1 or (cycle % 40) == registerX or (cycle % 40) == registerX+1:
                crtOutput = crtOutput + "#"
            else:
                crtOutput = crtOutput + " "
            cycle = cycle + 1
            
            # updating register happens at the very end of the 2nd cycle
            value = int(instruction.split(" ")[1])
            registerX = registerX + value

# CRT is 40 wide and 6 high
print(crtOutput[0:40])
print(crtOutput[40:80])
print(crtOutput[80:120])
print(crtOutput[120:160])
print(crtOutput[160:200])
print(crtOutput[200:240])
