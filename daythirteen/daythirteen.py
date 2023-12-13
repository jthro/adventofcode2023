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
        while k < min(j, len(field)-j):                
            print(j-k-1, j+k)
            print(field[j-k-1])
            print(field[j+k])
            if field[j-k-1] != field[j+k]:
                mirror = False
                break
            k += 1
        if mirror:
            answers.append(j*100)
        
print(answers)