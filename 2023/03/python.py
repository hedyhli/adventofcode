# https://adventofcode.com/2023/day/3
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
#     aoc d -y 2023 -d 3 -oi /dev/stdout | python3 python.py -
#     aocd 3 2023 | python3 python.py -
#     pbpaste | python3 python.py -

import re
import typing as T


def is_sym(ch: str) -> bool:
    """Non-digit other than '.'"""
    return not ch.isdigit() and ch != "."


# Literally forgot 'in' operator existed for a sec. Was using try-except on
# list.find!
def has_sym(symlist: T.Iterable, checks: T.Iterable) -> T.Union[int, bool]:
    for i in checks:
        if i in symlist:
            return i
    return False


# POV: No inline functions
def nuf(x):
    """I am kenough"""
    return x is not False


if __name__ == "__main__":
    import sys
    inputfn = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    from aocd import submit
    with open(
        0 if inputfn == "-" else ("example.txt" if inputfn == "e" else inputfn)
    ) as f:
        lines = f.read().splitlines()

    # Setup
    nums: list[list[re.Match]] = []
    symbols: list[list[int]] = []
    for j, line in enumerate(lines):
        nums.append(list(re.finditer(r"(\d+)", line)))
        symbols.append([])
        for c in range(len(line)):
            ch = line[c]
            if is_sym(ch):
                symbols[-1].append(c)

    # part 1
    s = 0
    for j, this in enumerate(symbols):
        for match in nums[j]:
            start: int
            end: int
            # end goes after last character in match
            start, end = match.span()
            num = int(match.group())

            # We love lisp
            if (nuf(has_sym(this, (start-1, end)))
                or (j > 0
                    and nuf(has_sym(symbols[j-1], range(start-1, end+1))))
                or (j < len(symbols) - 1
                    and nuf(has_sym(symbols[j+1], range(start-1, end+1))))):
                s += num

    print(s)
    if inputfn == "input.txt":
        submit(s, "a", day=3, year=2023, reopen=False)


    # part 2 setup
    asterisks: list[dict[int, list[int]]] = []
    for j in range(len(lines)):
        line = lines[j]
        asterisks.append({})
        for c in range(len(line)):
            ch = line[c]
            if ch == "*":
                asterisks[-1][c] = []

    # part 2
    s = 0
    for j in range(len(nums)):
        for match in nums[j]:
            start, end = match.span()
            num = int(match.group())

            # We love lisp
            if nuf(i := has_sym(asterisks[j], (start-1, end))):
                asterisks[j][i].append(num)

            elif (j > 0
                    and nuf(i := has_sym(asterisks[j-1].keys(), range(start-1, end+1)))
            ): # :(
                asterisks[j-1][i].append(num)

            elif (j < len(asterisks) - 1
                    and nuf(i := has_sym(asterisks[j+1].keys(), range(start-1, end+1)))
            ): # :(
                asterisks[j+1][i].append(num)

    # List comprehensions are overrated
    # Why would anyone want to have 2n iterations just for the sake of code
    # prettiness
    #   s = sum( len(v) == 2 and v[0]*v[1] or 0 for a in asterisks for v in a.values() )
    # ???
    for a in asterisks:
        for v in a.values():
            if len(v) == 2:
                s += v[0] * v[1]

    print(s)
    if inputfn == "input.txt":
        submit(s, "b", day=3, year=2023, reopen=False)
