import math
input = open("day5_input.txt").read().split("\n")


def boardingIDCalc(boardingpasses):
    boardingIDMax = 0
    allIDs = []
    realIDs = []
    for i in range(0, 127*8+7):
        allIDs.append(i)

    for bp in boardingpasses:
        boardingID = binarysearch(bp)
        if boardingID > boardingIDMax:
            boardingIDMax = boardingID
        realIDs.append(boardingID)
    ourID = list(set(allIDs) - set(realIDs))
    for index, ID in enumerate(ourID):
        if (ourID[index-1] != ID-1) and (ourID[index+1] != ID+1):
            ourID = ID
            break
    return boardingIDMax, ourID


def binarysearch(bp):
    lat_low = 0
    lat_high = 127
    hor_low = 0
    hor_high = 7
    for char in bp:
        if char == "F" or char == "B":
            if char == "F":
                lat_high = math.floor((lat_high+lat_low)/2)
            elif char == "B":
                lat_low = math.ceil((lat_high+lat_low)/2)
            else:
                print("ERROR")
        if char == "L" or char == "R":
            if char == "L":
                hor_high = math.floor((hor_high+hor_low)/2)
            elif char == "R":
                hor_low = math.ceil((hor_high+hor_low)/2)
            else:
                print("ERROR")
    return lat_high*8+hor_high


print(boardingIDCalc(input))