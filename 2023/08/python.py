# https://adventofcode.com/2023/day/8
#
## USAGE ##
# Run with 'input.txt' and submit with aocd:
#     python3 python.py
# Run with 'example.txt' and don't submit:
#     python3 python.py e
# Run with 'test.txt' and don't submit:
#     python3 python.py test.txt
# Run with stdin and don't submit:
#     cat myinput | python3 python.py -
#     aoc d -y 2023 -d 8 -oi /dev/stdout | python3 python.py -
#     aocd 8 2023 | python3 python.py -
#     pbpaste | python3 python.py -

# from functools import reduce
# from collections import
# from itertools import
import math

if __name__ == '__main__':
    import sys
    inputfn = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    from aocd import submit
    with open(0 if inputfn == '-' else \
              ('example.txt' if inputfn == 'e' else inputfn)) as f:
        lines = f.read().split('\n\n')
        ins = lines[0]
        lines = lines[1].splitlines()

    ############################################################################

    M = {}
    endA = []
    for line in lines:
        parts = line.split(' = ')
        if parts[0][2] == 'A':
            endA.append(parts[0])
        M[parts[0]] = parts[1][1:][:-1].split(', ')

    # print(M)

    ############################################################################
    # part 1
    count = 0
    i = 0
    cur = 'AAA'
    while cur != 'ZZZ':
        count += 1
        pos = 0 if ins[i] == 'L' else 1
        # print(i, pos, cur)
        cur = M[cur][pos]
        i += 1
        i = i % len(ins)

    print(count)
    if inputfn == "input.txt":
        submit(count, "a", day=8, year=2023, reopen=False)


    ############################################################################
    # part 2

    gs = []
    for e in endA:
        count = 0
        i = 0
        while e[2] != 'Z':
            count += 1
            pos = 0 if ins[i] == 'L' else 1
            e = M[e][pos]
            i += 1
            i = i % len(ins)
        gs.append(count)

    count = math.lcm(*gs)
    print(count)
    if inputfn == "input.txt":
        submit(count, "b", day=8, year=2023, reopen=False)
