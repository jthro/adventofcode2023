f = open("mock.txt")
input = f.read().strip().splitlines()
energizedx = [[0 for x in input[0]] for x in input]
energizedy = [[0 for x in input[0]] for x in input]
queue = []
startposition = [0,0,1,0]
subtractforsomereason = 0

queue.append(startposition)

while True:
    if len(queue) == 0:
        break
    x = queue[0][0]
    y = queue[0][1]
    xmov = queue[0][2]
    ymov = queue[0][3]
    print(x,y,xmov,ymov)
    if energizedx[x][y] and ymov == 0:
        queue.pop(0)
        continue
    elif energizedy[x][y] and xmov == 0:
        queue.pop(0)
        continue
    if xmov == 0:       
        energizedy[x][y] = 1    
        match(input[y][x]):
            case "/":                
                x -= ymov
                ymov = 0               
            case "\\":
                xmov += ymov
                ymov = 0
            case "-":
                queue.append([x,y,1,0])
                xmov = -1
                ymov = 0
    else:        
        energizedx[x][y] = 1
        match(input[y][x]):            
            case "|":
                queue.append([x,y,0,1])
                ymov = -1
                xmov = 0
            case "/":
                ymov -= xmov
                xmov = 0
            case "\\":
                ymov += xmov
                xmov = 0
    if queue[0][0] > len(input[0]) or queue[0][1] > len(input):
        queue.pop(0)
        continue
    
    queue[0] = [x + xmov, y + ymov, xmov, ymov]
    
totalenergized = 0

for j,c in enumerate(energizedx):
    for i,d in enumerate(energizedx[0]):
        if energizedx[j][i] or energizedy[j][i]:
            totalenergized += 1

print(totalenergized)