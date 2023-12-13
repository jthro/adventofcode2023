f = open("input.txt")
file = f.read().strip().splitlines()
output = file.copy()

currstring = 0
offset = 0
for line in file:
    if "#" not in line:
        for _ in range(1000000):        
            output.insert(currstring+offset, line)
        offset += 1000000
    currstring += 1

print("added rows")

currchar = 0
offset = 0
while currchar < len(file[0]):
    column = ""
    for line in file:
        column += line[currchar]        
    if "#" not in column:
        for i, line in enumerate(output):
            output[i] = line[0:currchar+offset] + "."*1000000 + line[currchar+offset:]
        offset += 1000000   
    currchar += 1 
print("added columns")    
class Coordinate:
    def __init__(self, x, y):
        self.y = y
        self.x = x
    
    def distance(self, coord):
        return abs(self.x - coord.x) + abs(self.y - coord.y)

galaxies = []
for i, line in enumerate(output):
    for j, character in enumerate(line):
        if character == "#":
            c = Coordinate(j, i)
            galaxies.append(c)
print("galaxies obtained")        
distances = []
for i, obj in enumerate(galaxies):
    for remainder in galaxies[i:]:
        distances.append(obj.distance(remainder))

print(sum(distances))