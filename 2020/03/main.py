with open("input.txt") as f:
    li = [list(i.strip()) for i in f.readlines()]



def count_trees(right, down):
    count = x = y = 0

    for y in range(0, len(li), down):
        if li[y][x % len(li[0])] == '#':
            count += 1
        x += right
    return count

def one():
    return count_trees(3, 1)

def two():
    return count_trees(1,1) * count_trees(3,1) * count_trees(5,1) * count_trees(7,1) * count_trees(1,2)

print(one())
print(two())
