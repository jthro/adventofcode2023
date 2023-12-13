f = open("input.txt")
g = f.read().split("\n\n")
input = []
for field in g:
    input.append(field.strip().splitlines())
answers = []
mirror = True
for i,field in enumerate(input):
    for j,line in enumerate(field):
        k = 0
        mirror = True
        fuzzyUsed = False
        while k < min(j, len(field)-j):
            for l, characters in enumerate(line):
                if field[j-k-1][l] != field[j+k][l]:
                    if fuzzyUsed == False:
                        fuzzyUsed = True
                    else:
                        mirror = False
                        break
            k += 1
        if mirror and fuzzyUsed:
            answers.append(j*100)

for i, field in enumerate(input):
    mirrorbar = 1
    while mirrorbar < len(field[0]):
        mirror = True
        fuzzyUsed = False
        for j, line in enumerate(field):
            charactercounter = 0
            while charactercounter < min(mirrorbar, len(field[j])-mirrorbar):
                if line[mirrorbar-1-charactercounter] != line[mirrorbar+charactercounter]:
                    if fuzzyUsed == False:
                        fuzzyUsed = True
                    else:
                        mirror = False
                        break
                charactercounter += 1
        if mirror and fuzzyUsed:
            answers.append(mirrorbar)
            break
        mirrorbar += 1
            
print(sum(answers))        