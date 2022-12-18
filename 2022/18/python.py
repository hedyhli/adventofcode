import sys

fn = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

from aocd import submit


def isadj(a, b):
    diff = 0
    for i, j in zip(a, b):
        diff += abs(i-j)
    return diff <= 1


if __name__ == '__main__':
    with open(fn) as f:
        lines = list(tuple(map(int, line.split(','))) for line in f.read().splitlines())


    SA = 0
    for i, cube in enumerate(lines):
        SA += 6
        for cubecheck in lines[i+1:]:
            if isadj(cube, cubecheck):
                # print(cube, cubecheck)
                SA -= 2

    print(SA)

    if not "test" in fn:
        submit(SA, "a", 18, 2022)

    # submit( , "b", 18, 2022)
