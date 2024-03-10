file = open("data.txt", "r")
lines = file.readlines()

def findFirstDigit(line): 
    for char in line: 
        if char.isdigit() == True:
            return char
    return 0

values = []
for line in lines: 
    lineSum = (findFirstDigit(line.strip()) + findFirstDigit(line.strip()[::-1]))
    values.append(int(lineSum))

sum = 0
for num in values: 
    sum += num

print(sum)


