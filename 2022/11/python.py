import sys
inputfn = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
import re

from aocd import submit


if __name__ == '__main__':

    # setup
    with open(inputfn) as f:
        lines = f.read().splitlines()

    length = (len(lines)+1)//7
    counts = [0]*length
    mops = [0]*length
    mdivrules = [0]*length

    mqueue = [0]*length
    starting = [0]*length

    reduce = 1

    for monkey in range(length):
        base = monkey*7+1
        itemline = lines[base].split(": ")

        items = list(map(int, itemline[1].split(", ")))
        op = lines[base+1].split(" = ")[1]
        div = int(re.search("(\d+)$", lines[base+2]).groups()[0])
        true = int(lines[base+3][-1])
        false = int(lines[base+4][-1])

        reduce *= div
        starting[monkey] = items          # for use in part 2
        mqueue[monkey] = items.copy()     # directly used in part 1
        mops[monkey] = eval("lambda old: " + op)
        mdivrules[monkey] = (div, {"true": true, "false": false})


    def inspect(mqueue, f3=True):
        for monkey, (op, divtest) in enumerate(zip(mops, mdivrules)):
            counts[monkey] += len(mqueue[monkey])
            while len(mqueue[monkey]):
                item = op(mqueue[monkey].pop())
                if f3:
                    item //= 3
                else:  # part 1 somehow doesn't work with this
                    if item > 10000:
                        item %= reduce
                if item%divtest[0] == 0:
                    mqueue[divtest[1]["true"]].append(item)
                else:
                    mqueue[divtest[1]["false"]].append(item)

    # part 1
    # 20 rounds
    # (r can be used in debug eg:'print("round", r)')
    for r in range(1, 21):
        inspect(mqueue)

    counts.sort()
    a, b = counts[-2:]
    print(mb := a * b, end="\n")
    if "test" not in inputfn:
        submit(mb, "a", 11, 2022)

    # part 2
    # reset
    counts = [0]*length
    mqueue = starting
    # 10000 rounds
    for r in range(1, 10001):
        inspect(mqueue, False)

    counts.sort()
    a, b = counts[-2:]
    print(mb := a * b)
    if "test" not in inputfn:
        submit(mb, "b", 11, 2022)
