# https://adventofcode.com/2015/day/2
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
#     aoc d -y 2015 -d 2 -oi /dev/stdout | python3 python.py -
#     aocd 2 2015 | python3 python.py -
#     pbpaste | python3 python.py -

from functools import reduce



if __name__ == '__main__':
    import sys
    inputfn = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

    from aocd import submit

    C = [(0,1),(1,2),(0,2)]

    with open(0 if inputfn == '-' else \
              ('example.txt' if inputfn == 'e' else inputfn)) as f:
        lines = f.read().splitlines()


    s = 0
    for line in lines:
        d = [int(i) for i in line.split('x')]
        a = []
        for combo in C:
            a.append(d[combo[0]] * d[combo[1]])
            s += 2 * a[-1]
        s += min(a)

    # part 1
    print(s)
    if inputfn == "input.txt":
        submit(s, "a", day=2, year=2015, reopen=False)

    s = 0
    for line in lines:
        d = [int(i) for i in line.split('x')]
        a = []
        for combo in C:
            a.append(d[combo[0]] + d[combo[1]])
        s += 2 * min(a) + reduce(lambda x,y: x*y, d, 1)

    # part 2
    print(s)
    if inputfn == "input.txt":
        submit(s, "b", day=2, year=2015, reopen=False)
