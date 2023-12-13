import numpy as np

f = open("input.txt")
lines = f.read().strip().splitlines()

def defineTable(array):
    table = []
    iterator = 1
    for t in array:
        line = []
        for letters in t:
            line.append(0)
        table.append(line)
        iterator += 1
    return table

refindex = defineTable(lines)
currentLine = 0
sCoordinates = np.array([0,0])

for t in lines:    
    if "S" in t:
        np.put(sCoordinates, [0, 1], [currentLine, t.index("S")])
        break
    currentLine += 1

def matchchar(transform, cursor):
    match(lines[cursor[0]][cursor[1]]):
        case "|":
            return transform
        case "-":
            return transform
        case "L":
            if transform[0] == 1:
                return np.array([0,1])
            else:
                return np.array([-1,0])
        case "J":
            if transform[0] == 1:
                return np.array([0,-1])
            else:
                return np.array([-1,0])
        case "7":
            if transform[0] == -1:
                return np.array([0,-1])
            else:
                return np.array([1,0])
        case "F":
            if transform[0] == -1:
                return np.array([0,1])
            else:
                return np.array([1,0])

def calculate(start, starttransform):
    currentCursor = start
    pathlength = 1
    while (lines[currentCursor[0]][currentCursor[1]] != "S"):
        if pathlength < refindex[currentCursor[0]][currentCursor[1]] or refindex[currentCursor[0]][currentCursor[1]] == 0:
            refindex[currentCursor[0]][currentCursor[1]] = pathlength
        starttransform = matchchar(starttransform, currentCursor)    
        currentCursor = np.add(currentCursor, starttransform)
        pathlength += 1

calculate(np.add(sCoordinates, [-1,0], np.array([-1,0])), np.array([-1,0]))
calculate(np.add(sCoordinates, [0,-1], np.array([0,-1])), np.array([0,-1]))      
print(refindex)
np.savetxt("refindex.csv", refindex, delimiter=",")
furthestpoint = []
highestn = 0
leline = 0
for line in refindex:
    lechar = 0
    for character in line:
        if character > highestn:
            furthestpoint = [leline,lechar]
            highestn = character
        lechar += 1
    leline += 1
print(highestn)