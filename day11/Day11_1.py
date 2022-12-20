"""
--- Day 11: Monkey in the Middle ---

calculate the level of monkey business
"""

# Easier to hard code values instead of reading from file
# inputFile = open("C:\\Users\\Tom\\Documents\\GitHub\\Advent-of-Code-2022\\day11\\input")

monkeyItems = [[50, 70, 54, 83, 52, 78],[71, 52, 58, 60, 71],[66, 56, 56, 94, 60, 86, 73],[83, 99],[98, 98, 79],[76],[52, 51, 84, 54],[82, 86, 91, 79, 94, 92, 59, 94]]
monkeyInspectionCount = [0,0,0,0,0,0,0,0]

for i in range(20):
    # Monkey 0
    # Operation: new = old * 3
    # Test: divisible by 11
    # If true: throw to monkey 2
    # If false: throw to monkey 7
    for worryValue in monkeyItems[0]:
        monkeyInspectionCount[0] = monkeyInspectionCount[0] + 1
        newWorryValue = (worryValue * 3) // 3
        if newWorryValue % 11 == 0:
            monkeyItems[2].append(newWorryValue)
        else:
            monkeyItems[7].append(newWorryValue)
    monkeyItems[0] = []
    
    # Monkey 1:
    # Operation: new = old * old
    # Test: divisible by 7
    # If true: throw to monkey 0
    # If false: throw to monkey 2
    for worryValue in monkeyItems[1]:
        monkeyInspectionCount[1] = monkeyInspectionCount[1] + 1
        newWorryValue = (worryValue * worryValue) // 3
        if newWorryValue % 7 == 0:
            monkeyItems[0].append(newWorryValue)
        else:
            monkeyItems[2].append(newWorryValue)
    monkeyItems[1] = []
    
    # Monkey 2:
    # Operation: new = old + 1
    # Test: divisible by 3
    # If true: throw to monkey 7
    # If false: throw to monkey 5
    for worryValue in monkeyItems[2]:
        monkeyInspectionCount[2] = monkeyInspectionCount[2] + 1
        newWorryValue = (worryValue + 1) // 3
        if newWorryValue % 3 == 0:
            monkeyItems[7].append(newWorryValue)
        else:
            monkeyItems[5].append(newWorryValue)
    monkeyItems[2] = []
    
    # Monkey 3:
    # Operation: new = old + 8
    # Test: divisible by 5
    # If true: throw to monkey 6
    # If false: throw to monkey 4
    for worryValue in monkeyItems[3]:
        monkeyInspectionCount[3] = monkeyInspectionCount[3] + 1
        newWorryValue = (worryValue + 8) // 3
        if newWorryValue % 5 == 0:
            monkeyItems[6].append(newWorryValue)
        else:
            monkeyItems[4].append(newWorryValue)
    monkeyItems[3] = []
    
    # Monkey 4:
    # Operation: new = old + 3
    # Test: divisible by 17
    # If true: throw to monkey 1
    # If false: throw to monkey 0
    for worryValue in monkeyItems[4]:
        monkeyInspectionCount[4] = monkeyInspectionCount[4] + 1
        newWorryValue = (worryValue + 3) // 3
        if newWorryValue % 17 == 0:
            monkeyItems[1].append(newWorryValue)
        else:
            monkeyItems[0].append(newWorryValue)
    monkeyItems[4] = []
    
    # Monkey 5:
    # Operation: new = old + 4
    # Test: divisible by 13
    # If true: throw to monkey 6
    # If false: throw to monkey 3
    for worryValue in monkeyItems[5]:
        monkeyInspectionCount[5] = monkeyInspectionCount[5] + 1
        newWorryValue = (worryValue + 4) // 3
        if newWorryValue % 13 == 0:
            monkeyItems[6].append(newWorryValue)
        else:
            monkeyItems[3].append(newWorryValue)
    monkeyItems[5] = []
    
    # Monkey 6:
    # Operation: new = old * 17
    # Test: divisible by 19
    # If true: throw to monkey 4
    # If false: throw to monkey 1
    for worryValue in monkeyItems[6]:
        monkeyInspectionCount[6] = monkeyInspectionCount[6] + 1
        newWorryValue = (worryValue * 17) // 3
        if newWorryValue % 19 == 0:
            monkeyItems[4].append(newWorryValue)
        else:
            monkeyItems[1].append(newWorryValue)
    monkeyItems[6] = []
    
    # Monkey 7:
    # Operation: new = old + 7
    # Test: divisible by 2
    # If true: throw to monkey 5
    # If false: throw to monkey 3
    for worryValue in monkeyItems[7]:
        monkeyInspectionCount[7] = monkeyInspectionCount[7] + 1
        newWorryValue = (worryValue + 7) // 3
        if newWorryValue % 2 == 0:
            monkeyItems[5].append(newWorryValue)
        else:
            monkeyItems[3].append(newWorryValue)
    monkeyItems[7] = []
    
print(monkeyInspectionCount)
monkeyInspectionCount.sort(reverse=True)
monkeyBusiness = monkeyInspectionCount[0] * monkeyInspectionCount[1]
print(monkeyBusiness)
