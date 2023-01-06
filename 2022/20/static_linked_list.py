# https://adventofcode.com/2022/day/20
#
# This version uses the static linked list concept where a list of data
# to keep the numbers that will never be modified - the input. And a
# corresponding list of _indices_ that indicated for each item, what is
# the index of the next item. This list's indices corresponds to the
# data's indices. When mixing the numbers, only the indices list will be
# modified.
#
# Optimization is used for the number of steps to move and the final
# step where the 1000th, 2000th, and 3000th number after 0 is found.
#
# The index of 0 is obtained at the same time of mixing.
#
## USAGE ##
# Run with 'input.txt' and submit with aocd:
#     python3 python.py
# Run with 'test.txt' and don't submit:
#     python3 python.py test.txt
# Run with stdin and don't submit:
#     cat myinput | python3 python.py -
#     aoc d -y 2022 -d 20 -oi /dev/stdout | python3 python.py -
#     aocd 20 2022 | python3 python.py -

def normalize(n, top):
    """Wrap around the top if n is negative"""
    if n < 0:
        n += top
    return n


if __name__ == '__main__':
    import sys
    inputfn = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    from aocd import submit

    with open(0 if inputfn == '-' else inputfn) as f:
        data = tuple( int(l) for l in f.read().splitlines() )
    LEN = len(data)
    nexts = list(range(1, LEN+1))
    nexts[-1] = 0  # :O it loops!
    i0 = 0


    def lookup(start: int, index: int) -> int:
        """Find the index of i'th item after start (i > 0)"""
        cur = nexts[start]
        for _ in range(index-1):
            cur = nexts[cur]
        return cur

    def incremental_lookup(start: int, indices: list[int]):
        """Lookup multiple indices searching incrementally, as a generator.

        Rather than starting from the same starting point each item.

        Faster than lookup() from the same starting point, where LEN is
        greater than each of the indices...supposedly

        For indices = [1000, 2000, 3000], start=0:
          - lookup(0, 1000)
          - lookup(1000, 1000)
          - lookup(2000, 1000)

        This prevents the need of having to traverse through the linked
        list repeatedly for indices 2000 and 3000, from the beginning.
        """
        i  = prev = indices[0]
        yield (start := lookup(start, i))
        for i in indices[1:]:
            yield (start := lookup(start, normalize(i-prev, LEN)))
            prev = i

    def printlist():
        """Print items in list separated by 2 spaces"""
        c = nexts[nexts.index(0)]
        print(data[c], end="  ")
        c = nexts[c]
        while c != 0:
            print(data[c], end="  ")
            c = nexts[c]

    def mix():
        """1 round of mixing and find i0 if i0 == 0"""
        global i0

        for cur in range(LEN):
            num = data[cur]  # amt to move
            if num == 0:
                if i0 == 0:
                    i0 = cur
                continue
            num %= LEN-1
            num = normalize(num, LEN-1)
            if num == 0:
                continue

            targ = lookup(cur, num) # current will be moved after targ
            prev = nexts.index(cur) # prev points to current
            # MOVE!! (*sort* of)
            nexts[prev] = nexts[cur]
            nexts[cur] = nexts[targ]
            nexts[targ] = cur

    def result():
        """Find the 1000th, 2000th, and 3000th item, and their sum"""
        s = 0
        nth = [ i%LEN for i in (1000, 2000, 3000) ]
        for i in incremental_lookup(i0, nth):
            print(d := data[i], end="  ")
            s += d
        print("\nSum:", s)
        return s


    # part 1
    mix()
    assert i0 == (verif:=data.index(0)), f"{i0} != {verif}"
    s = result()
    if inputfn == "input.txt":
        submit(s, "a", day=20, year=2022)

    # part 2
    DEC = 811589153; print()
    data = [ i*DEC for i in data ]  # Apply decryption key
    # reset
    nexts = list(range(1, LEN+1)); nexts[-1] = 0
    # Let's mix 'em!
    for r in range(10):
        print("round", r+1, end="\r")
        mix()
    s2 = result()
    assert s != s2
    if inputfn == "input.txt":
        submit(s2, "b", day=20, year=2022)
