file = open("data.txt", "r")
lines = file.readlines()

def findPower(gameData):
    highestValues = [0,0,0]
    # For each handful revealed
    for i in range(len(gameData)):
        # For each color shown
        values = gameData[i].split(",")
        for j in range(len(values)):
            if (values[j]).endswith("red"):
                if int(values[j].strip().split(" ")[0]) > highestValues[0]:
                    highestValues[0] = int(values[j].strip().split(" ")[0])
            if (values[j]).endswith("green"):
                if int(values[j].strip().split(" ")[0]) > highestValues[1]:
                    highestValues[1] = int(values[j].strip().split(" ")[0])
            if (values[j]).endswith("blue"):
                if int(values[j].strip().split(" ")[0]) > highestValues[2]:
                    highestValues[2] = int(values[j].strip().split(" ")[0])
    return highestValues[0] * highestValues[1] * highestValues[2]

sum = 0
for line in lines: 
    line = line.strip()[5:]
    split1 = line.split(":")
    gameData = split1[1].split(";")
    sum += findPower(gameData)

print(sum)

