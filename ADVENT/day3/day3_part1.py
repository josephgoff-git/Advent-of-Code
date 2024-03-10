file = open("data.txt", "r")
lines = file.readlines()

lineCount = 0
sum = 0
for line in lines:
    lineCount += 1
    print(line)
    # go through line to find number segments
    indexes = []
    for i in range(len(line)):
        if line[i].isdigit() == True:
            indexes.append(i)
    
    groups = []
    currentGroup = []
    for i in range(len(indexes)):
        if i == 0: 
            currentGroup.append(indexes[i])
            continue
        if indexes[i] == indexes[i-1] + 1:
            currentGroup.append(indexes[i])
        else: 
            groups.append(currentGroup)
            currentGroup = []
            currentGroup.append(indexes[i])
        if i == len(indexes) - 1: 
            groups.append(currentGroup)

    print(groups)

    def checkAbove(group): 
        foundSymbol = False
        startingIndex = group[0] - 1
        if startingIndex < 0: 
            startingIndex = 0
        endingIndex = group[len(group) - 1] + 1
        if endingIndex > len(line) - 1: 
            endingIndex = len(line) - 1
        
        print(group)
        for i in range(startingIndex, endingIndex + 1):
            if line[i].isdigit() == False and line[i] != ".":
                foundSymbol = True
        return foundSymbol

    def checkBelow(group): 
        foundSymbol = False
        return foundSymbol
    
    def putTogether(group):
        print(group)
        result = ""
        for i in range(len(group)):
            result += str(line[group[i]])
        print(result)
        return int(result)

    for i in range(len(groups)):
        if lineCount == 1: 
            if (checkBelow(groups[i]) == True):
                sum += putTogether(groups[i])
        elif lineCount == len(lines): 
            if (checkAbove(groups[i]) == True):
                sum += putTogether(groups[i])
        else:
            if (checkAbove(groups[i]) == True and checkBelow(groups[i]) == True):
                sum += putTogether(groups[i])

print(sum)

        