import string
input = open("day6_input.txt").read().split("\n\n")

input1 = [group.replace("\n", "") for group in input]


def groupCounter(groups):
    total = 0
    for group in groups:
        total += len(set(group))
    return total


print(groupCounter(input1))

# ------------Part 2--------------
input2 = []
for group in input:
    input2.append(group.split("\n"))


def sharedChars(s1, s2):
    return "".join(set(s1).intersection(s2))


def groupCounter2(groups):
    total = 0
    for group in groups:
        shared_chars = string.ascii_lowercase
        for index in range(len(group)):
            shared_chars = sharedChars(shared_chars, group[index])
        total += len(shared_chars)
    return total


print(groupCounter2(input2))