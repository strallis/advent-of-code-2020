f = open("day3_input.txt", "r")

input = f.read().split("\n")
input = [list(sub) for sub in input]

def tobogganNavigation(input, right, down):
    row_len = len(input[0])
    col_len = int((len(input[:])-1)/down)
    pos = [0,0]
    trees = 0
    for _ in range(col_len):
        pos[0] += down
        pos[1] += right
        if pos[1] < row_len:
            pass    
        else:
            pos[1] = pos[1]-row_len
        if input[pos[0]][pos[1]] == '#':
            trees += 1
    return(trees)

a = tobogganNavigation(input, 1, 1)
b = tobogganNavigation(input, 3, 1)
c = tobogganNavigation(input, 5, 1)
d = tobogganNavigation(input, 7, 1)
e = tobogganNavigation(input, 1, 2)
print(a*b*c*d*e)