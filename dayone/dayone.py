input = open("input.txt")
splitinput = input.readlines()
iterator = 0;
numberone = "0";
numbertwo = "0";
numbers = []
    
for line in range(len(splitinput)):
    currentline = splitinput[line]
    for character in range(len(currentline)):
        currentchar = currentline[character]
        if currentchar.isnumeric():
            numberone = currentchar
            break
    for character in range(len(currentline)):
        currentchar = currentline[len(currentline)-character-1]
        if currentchar.isnumeric():
            numbertwo = currentchar
            break
    linecode = numberone + numbertwo
    print(linecode)
    numbers.append(int(linecode))
print(sum(numbers)) 
        
    
    