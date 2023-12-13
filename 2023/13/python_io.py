# https://adventofcode.com/2023/day/13

def find_mirror(case: list[str], smudges = 0) -> int:
    case_t = list(map(''.join, zip(*case)))
    for m, c in ((100, case), (1, case_t)):
        for i in range(1, len(c)):
            if sum(
                sum(int(a != b) for a, b in zip(line1, line2))
                for line1, line2 in zip(c[i:], c[i-1::-1])
            ) == smudges:
                return m * i

    raise ValueError
    return 0

with open(0) as f:
    cases = list(map(str.splitlines, f.read().split('\n\n')))

for smudge in (0, 1):
    print(sum(find_mirror(case, smudge) for case in cases))
