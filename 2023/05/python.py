# https://adventofcode.com/2023/day/5
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
#     aoc d -y 2023 -d 5 -oi /dev/stdout | python3 python.py -
#     aocd 5 2023 | python3 python.py -
#     pbpaste | python3 python.py -

# from functools import reduce

 
def in_range(r, item):
    return r[0] <= item <= r[1]

def lt(r, item):
    return r[1] < item

def binarysearch(arr, item, lo, up):
    mid = (lo+up)//2
    if lo > up:
        return "ALFJDLKFJSDLFK NOT FOUND"
    if in_range(arr[mid][0], item):
        return mid
    elif lt(arr[mid][0], item):
        return binarysearch(arr, item, mid, up)
    else:
        return binarysearch(arr, item, lo, mid)


D = {(0, 5_000_000_000): 0}


def merge_map(r: tuple[int,int], old, a, b, new):
    global D
    o0, o1 = r

    if o0 == a and o1 == b:
        D[(a, b)] = new
        return a, b

    if o0 <= a and b <= o1:
        if old == new:
            return a, b
        del D[r]
        if o0 != a:
            D[(o0, a - 1)] = old
        D[(a, b)] = new
        if o1 != b:
            D[(b + 1, o1)] = old
        return a, b

    if a <= o0 and o1 <= b:
        if old == new:
            del D[r]
            D[(a, b)] = new
            return a, b
        if a != o0:
            D[(a, o0-1)] = new
        if b != o1:
            return o1 + 1, b
        return a, b

    if a <= o0 and o0 <= b <= o1:
        del D[r]
        D[(a, b)] = new
        if b != o1:
            D[(b + 1, o1)] = old
        return a, b

    if b >= o1 and o0 <= a <= o1:
        del D[r]
        if a != o0:
            D[(o0, a - 1)] = old
        D[(a, b)] = new
        if b != o1:
            return o1 + 1, b
        else:
            return a, b

    if b < o0:
        return a, b

    return a, b


if __name__ == '__main__':
    import sys
    inputfn = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

    from aocd import submit

    with open(0 if inputfn == '-' else \
              ('example.txt' if inputfn == 'e' else inputfn)) as f:
        seeds: list[int] = [int(i) for i in f.readline()[7:].strip().split(' ')]
        f.readline()
        sections: list[list[str]] = [
            i.strip().split('\n') for i in f.read().split('\n\n')
        ]

    level = 0
    Ds = []
    for sec in sections:
        D = {(0, 5_000_000_000): 0}
        level += 1
        for line in sec[1:]:
            dest, a, n = [int(i) for i in line.strip().split(' ')]
            new = dest - a
            b = a + n - 1

            for r in sorted(D):
                old = D[r]
                ret = merge_map(r, old, a, b, new)
                if ret:
                    a, b = ret
                else:
                    break
        Ds.append(D)

    Ms = []
    for D in Ds:
        M:list[tuple[tuple[int,int], int]] = list(sorted(D.items()))
        Ms.append(M)


    # part 1
    location = 10**10

    for seed in seeds:
        # print(seed, end = ' ')
        for M in Ms:
            i = binarysearch(M, seed, 0, len(M))
            seed += M[i][1]
            # print(seed)
        location = min(location, seed)

    print(location)
    if inputfn == "input.txt":
        submit(location, "a", day=5, year=2023, reopen=False)

    # part 2
    for M in Ms:
        s = 0
        nextseeds = []
        while s < len(seeds):
            seed, n = seeds[s], seeds[s + 1]
            before = seed + n
            s += 2

            i = binarysearch(M, seed, 0, len(M))
            newseed = seed + M[i][1]
            nextseeds.append(newseed)
            nextseeds.append(min(n, M[i][0][1] - seed))
            seed = M[i][0][1] + 1

            while seed < before:
                i += 1
                newseed = seed + M[i][1]
                nextseeds.append(newseed)
                nextseeds.append(min(before - seed, M[i][0][1] - seed))
                seed = M[i][0][1] + 1

        seeds = nextseeds

    location = min(seeds[i] for i in range(0, len(seeds), 2))

    print(location)
    if inputfn == "input.txt":
        submit(location, "b", day=5, year=2023, reopen=False)
