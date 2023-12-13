f = open("input.txt")
lines = f.read().strip().splitlines()
directions = lines[0]
for line in lines[2:]:
    index,content = line.split(" = ")
    L,R = content.removeprefix("(").removesuffix(")").split(", ")
    print(L,R)