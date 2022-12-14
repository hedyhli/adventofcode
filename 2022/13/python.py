# from pysnooper import snoop

# @snoop()
def diff(a, b):
    if type(a) == int:
        if type(b) == int:
            return a - b
        return diff([a], b)

    if type(b) == int and not type(a) == int:
        return diff(a, [b])

    for x, y in zip(a, b):
        d = diff(x, y)
        if d != 0:
            return d

    return len(a) - len(b)


if __name__ == '__main__':
    from functools import cmp_to_key

    from more_itertools import grouper
    from aocd import submit

    with open("input.txt") as f:
        packets = [ eval(l) for l in f.read().strip().replace("\n\n", "\n").split("\n") ]

    orderedsum = 0
    for i, (left, right) in enumerate(grouper(packets, 2)):
        if diff(left, right) < 0:
            orderedsum += i+1

    print(orderedsum)
    submit(orderedsum, "a", 13, 2022)

    packetslist = [[[2]], [[6]]]
    packetslist.extend(packets)
    packetslist.sort(key=cmp_to_key(diff))

    print(d:=(packetslist.index([[2]])+1)*(packetslist.index([[6]])+1))
    submit(d, "b", 13, 2022)
