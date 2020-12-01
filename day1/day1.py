f = open("day1_input.txt", "r")

input = f.read().split("\n")
input = [int(x) for x in input]
test_input = [1721,979,366,299,675,1456]


def twoFinder(input):
    finished = False
    for index in range(len(input)):
        for number in input:
            if input[index]+number == 2020:
                finished = True
                print("Numbers found! They are: " + str(input[index]) + " and " + str(number) + "!")
                print("Multiplying...")
                print(input[index]*number)
                break
            else:
                continue
        print("Loop " + str(index) + " complete...")
        if finished == True:
            break

#twoFinder(input)
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
        print("Loop " + str(index) + " complete...")

threeFinder(input)