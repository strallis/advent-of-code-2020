f = open("day2_input.txt", "r")

input = f.read().split("\n")


def passwordChecker1(input):
    valid_passwords = 0
    for i in range(len(input)):
        lower_bound = input[i].split("-")[0]
        upper_bound = input[i].split("-")[1].split()[0]
        character = input[i].split("-")[1].split()[1].replace(":", "")
        password = input[i].split("-")[1].split()[2]
        char_in_pass = password.count(character)
        if char_in_pass >= int(lower_bound) and char_in_pass <= int(upper_bound):
            valid_passwords += 1
    return valid_passwords


print(passwordChecker1(input))


def passwordChecker2(input):
    valid_passwords = 0
    for i in range(len(input)):
        first_pos = input[i].split("-")[0]
        second_pos = input[i].split("-")[1].split()[0]
        character = input[i].split("-")[1].split()[1].replace(":", "")
        password = input[i].split("-")[1].split()[2]
        check1 = password[int(first_pos)-1] == character
        check2 = password[int(second_pos)-1] == character

        if check1 ^ check2:
            valid_passwords += 1
    return valid_passwords


print(passwordChecker2(input))
