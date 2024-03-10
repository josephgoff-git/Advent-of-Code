file = open("data.txt", "r")
lines = file.readlines()

sum = 0

totals = []
for line in lines: 
    totals.append(1)

count = 0
for line in lines: 
    print()
    sides = line.split("|")
    
    leftSide = sides[0].split(" ")
    rightSide = sides[1].split(" ")

    # Remove white spcae
    for i in range(len(leftSide) - 1, -1, -1):
        if leftSide[i] == '':
            leftSide.pop(i)

    for i in range(len(rightSide) -1, -1, -1):
        if rightSide[i] == '':
            rightSide.pop(i)

    # print(leftSide)
    # print(rightSide)

    def countMatches(leftSide, rightSide):
        matches = 0
        for i in range(len(rightSide)):
            for j in range(len(leftSide)):
                if rightSide[i].strip() == leftSide[j].strip():
                    matches += 1
                    continue
        return matches

    for i in range(totals[count]):
        matches = countMatches(leftSide, rightSide)
        print(matches)
        tip = 1
        while (matches > 0):
            totals[count + tip] += 1
            tip += 1
            matches -= 1
        print(totals)

    count += 1

sum = 0
for i in range(len(totals)):
    sum += totals[i]
print(sum)
    