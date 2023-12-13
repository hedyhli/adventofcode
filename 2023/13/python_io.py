# https://adventofcode.com/2023/day/13

from typing import Optional

HORZ_S = 100
VERT_S = 1

def find_mirror(case: list[str], smudges = 0) -> Optional[int]:
    case_t = list(map(''.join, zip(*case)))
    for m, c in ((HORZ_S, case), (VERT_S, case_t)):
        for i in range(len(c)-1):
            if sum(
                sum(int(a != b) for a, b in zip(line1, line2))
                for line1, line2 in zip(c[i+1:], c[i::-1])
            ) == smudges:
                return m * (i+1)

    print(*case, sep='\n')
    return None

with open(0) as f:
    cases = list(map(str.splitlines, f.read().split('\n\n')))

for smudge in (0, 1):
    print(sum(find_mirror(case, smudge) for case in cases))
