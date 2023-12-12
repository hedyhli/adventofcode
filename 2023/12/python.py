# https://adventofcode.com/2023/day/12
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
#     aoc d -y 2023 -d 12 -oi /dev/stdout | python3 python.py -
#     aocd 12 2023 | python3 python.py -
#     pbpaste | python3 python.py -

from functools import cache


def solve(row: str, groups: list[int]) -> int:
    """Generic solver for both parts, for each row of springs"""
    L: int = len(row)
    G: int = len(groups)

    def fill_hash(i: int, g: int) -> int:
        """Current char assumed to be #"""
        current_w = 0
        while i < L and row[i] != '.' and current_w < groups[g]:
            current_w += 1
            i += 1
        if groups[g] == current_w:
            if i >= L or row[i] == '.':
                return rec(i, g+1)
            elif row[i] == '?': # next '?' has to be '.'
                return rec(i+1, g+1)
        return 0

    @cache
    def rec(i: int = 0, g: int = 0) -> int:
        """i = index in row of springs, g = index in groups"""
        if i >= L: return int(g >= G)
        if g >= G: return int(row.find('#', i) == -1)

        if row[i] == '.': return rec(i+1, g)
        if row[i] == '#': return fill_hash(i, g)
        return fill_hash(i, g) + rec(i+1, g)

    return rec()


if __name__ == '__main__':
    import sys
    inputfn = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    from aocd import submit
    with open(0 if inputfn == '-' else \
              ('example.txt' if inputfn == 'e' else inputfn)) as f:
        lines = [
            ((p := line.split(' '))[0], list(map(int, p[1].split(','))))
            for line in f.read().splitlines()
        ]

    ############################################################################
    # part 1

    S = sum(solve(*line) for line in lines)
    print(S)
    if inputfn == "input.txt":
        submit(S, "a", day=12, year=2023, reopen=False)


    ############################################################################
    # part 2

    S = 0
    for i, line in enumerate(lines):
        string, fills = line
        string = '?'.join([string] * 5)
        fills *= 5
        s = solve(string, fills)
        S += s
    print(S)
    if inputfn == "input.txt":
        submit(S, "b", day=12, year=2023, reopen=False)
