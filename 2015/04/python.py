# https://adventofcode.com/2015/day/4
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
#     aoc d -y 2015 -d 4 -oi /dev/stdout | python3 python.py -
#     aocd 4 2015 | python3 python.py -
#     pbpaste | python3 python.py -

# from functools import reduce

from hashlib import md5


if __name__ == '__main__':
    import sys
    inputfn = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

    from aocd import submit

    with open(0 if inputfn == '-' else \
              ('example.txt' if inputfn == 'e' else inputfn)) as f:
        inp = f.read().strip()

    s = 0
    while True:
        s += 1
        if md5(bytes(inp+str(s), 'utf-8')).hexdigest().startswith('00000'):
            break

    # part 1
    print(s)
    if inputfn == "input.txt":
        submit(s, "a", day=4, year=2015, reopen=False)


    s = 0
    while True:
        s += 1
        if md5(bytes(inp+str(s), 'utf-8')).hexdigest().startswith('000000'):
            break

    # part 2
    print(s)
    if inputfn == "input.txt":
        submit(s, "b", day=4, year=2015, reopen=False)
