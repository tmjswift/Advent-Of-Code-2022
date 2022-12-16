"""
--- Day 10: Cathode-Ray Tube ---

calculate signal strength
"""

inputFile = open("C:\\Users\\Tom\\Documents\\GitHub\\Advent-of-Code-2022\\day10\\input")

cycle = 0
registerX = 1
cycleTimes = [20,60,100,140,180,220]
runningTotal = 0

for line in inputFile:
    if line == "\n":
        break
    if line == "noop\n":
        cycle = cycle + 1
        if cycle in cycleTimes:
            signalStrength = cycle * registerX
            print("signalStrength:", signalStrength)
            runningTotal = runningTotal + signalStrength
    else:
        instruction = line.strip("\n")
        if instruction.split(" ")[0] == "addx":
            cycle = cycle + 1
            if cycle in cycleTimes:
                signalStrength = cycle * registerX
                print("signalStrength:", signalStrength)
                runningTotal = runningTotal + signalStrength
            cycle = cycle + 1
            if cycle in cycleTimes:
                signalStrength = cycle * registerX
                print("signalStrength:", signalStrength)
                runningTotal = runningTotal + signalStrength
            # updating register happens at the very end of the 2nd cycle
            value = int(instruction.split(" ")[1])
            registerX = registerX + value
    print("Cycle:", cycle, "registerX:", registerX)
            
print("runningTotal:", runningTotal)
