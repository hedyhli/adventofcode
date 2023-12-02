# https://adventofcode.com/2015/day/3
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
#     aoc d -y 2015 -d 3 -oi /dev/stdout | python3 python.py -
#     aocd 3 2015 | python3 python.py -
#     pbpaste | python3 python.py -

# from functools import reduce



if __name__ == '__main__':
    import sys
    inputfn = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

    from aocd import submit

    with open(0 if inputfn == '-' else \
              ('example.txt' if inputfn == 'e' else inputfn)) as f:
        inp = f.read().strip()


    S = {(0,0)}
    x = y = 0

    for d in inp:
        if d == '^':
            y += 1
        elif d == 'v':
            y -= 1
        elif d == '>':
            x += 1
        elif d == '<':
            x -= 1
        S.add((x,y))

    # part 1
    print(len(S))
    if inputfn == "input.txt":
        submit(len(S), "a", day=3, year=2015, reopen=False)

    S = {(0,0)}
    c = ([0,0],[0,0])
    r = True

    for d in inp:
        r = not r
        l = c[int(r)]
        if d == '^':
            l[1] += 1
        elif d == 'v':
            l[1] -= 1
        elif d == '>':
            l[0] += 1
        elif d == '<':
            l[0] -= 1
        S.add((l[0],l[1]))

    # part 2
    print(len(S))
    if inputfn == "input.txt":
        submit(len(S), "b", day=3, year=2015, reopen=False)
