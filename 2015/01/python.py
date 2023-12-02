# https://adventofcode.com/2015/day/1
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
#     aoc d -y 2015 -d 1 -oi /dev/stdout | python3 python.py -
#     aocd 1 2015 | python3 python.py -
#     pbpaste | python3 python.py -

# from functools import reduce



if __name__ == '__main__':
    import sys
    inputfn = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

    from aocd import submit

    with open(0 if inputfn == '-' else \
              ('example.txt' if inputfn == 'e' else inputfn)) as f:
        inp = f.read().strip()


    floor = 0
    for ch in inp:
        floor += 1 if ch == '(' else -1


    # part 1
    print(floor)
    if inputfn == "input.txt":
        submit(floor, "a", day=1, year=2015, reopen=False)

    floor = 0
    for c in range(len(inp)):
        ch = inp[c]
        floor += 1 if ch == '(' else -1
        if floor == -1:
            break


    # part 2
    c += 1
    print(c)
    if inputfn == "input.txt":
        submit(c, "b", day=1, year=2015, reopen=False)
