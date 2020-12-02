from itertools import combinations


def load_list(fname = "one.txt"):
    with open(fname) as f:
        li = [int(i.strip()) for i in f.readlines()]
    return li


def a():
    global li
    for com in combinations(li, 2):
        if sum(com) == 2020:
            print(com[0] * com[1])


def b():
    global li
    for com in combinations(li, 3):
        if sum(com) == 2020:
            print(com[0] * com[1] * com[2])


if __name__  == "__main__":
    li = load_list()
    a()
    b()
