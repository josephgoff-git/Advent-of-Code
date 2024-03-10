file = open("data.txt", "r")
lines = file.readlines()

digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def findFirstLeftDigit(currentLine): 
    line = currentLine
    for i in range(len(currentLine)):
        if currentLine[i].isdigit() == True:
            return currentLine[i]
        else: 
            for j in range(len(digits)):
                if line.startswith(digits[j]):
                    return j+1
            line = line[1:]

def findFirstRightDigit(currentLine): 
    line = currentLine
    for i in range(len(currentLine)-1, -1, -1):
        if currentLine[i].isdigit() == True:
            return currentLine[i]
        else: 
            for j in range(len(digits)):
                if line.endswith(digits[j]):
                    return j+1
            line = line[0:-1]

values = []
for line in lines: 
    values.append(int(str(findFirstLeftDigit(line.strip())) + str(findFirstRightDigit(line.strip()))))

sum = 0
for num in values: 
    sum += num

print(sum)


