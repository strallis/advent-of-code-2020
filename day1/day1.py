f = open("day1_input.txt", "r")

input = f.read().split("\n")
input = [int(x) for x in input]
test_input = [1721,979,366,299,675,1456]


def twoFinder(input):
    finished = False
    index = 0
    for num1 in input:
        for num2 in input:
            if num1+num2 == 2020:
                finished = True
                print("Numbers found! They are: " + str(num1) + " and " + str(num2) + "!")
                print("Multiplying...")
                print(num1*num2)
                break
            else:
                continue
        if finished == True:
            break
        else: 
            index+=1

twoFinder(input)
#-------- Part 1 complete --------

def threeFinder(input):
    finished = False
    index = 0
    for num1 in input:
        for num2 in input:
            if num1+num2 > 2020-min(input) or finished == True:
                continue
            else:
                for num3 in input:
                    if num1+num2+num3 == 2020:
                        finished = True
                        print("Numbers found! They are: " + str(num1) + ", " + str(num2) + " and " + str(num3) + "!")
                        print("Multiplying...")
                        print(num1*num2*num3)
                        break
        if finished == True:
            break
        else: 
            index+=1

threeFinder(input)
