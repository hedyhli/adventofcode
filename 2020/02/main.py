def openfile(fname = "input.txt"):
    with open(fname) as f:
        li = [i.strip().split(' ') for i in f.readlines()]
    return li

def a():
    global li
    valid = []
    for p in li:
        minn = int(p[0].split('-')[0])
        maxx = int(p[0].split('-')[1])
        letter = p[1][0]
        if minn <= p[2].count(letter) <= maxx:
            valid.append(p)
    print(valid)
    print(len(valid))

def b():
    global li
    valid = []
    for p in li:
        a = int(p[0].split('-')[0]) - 1
        b = int(p[0].split('-')[1]) - 1
        letter = p[1][0]
        s = p[2]
        first = getindex(s, a) == letter
        sec = getindex(s, b) == letter
        if (first or sec) and (not (first and sec)):
            valid.append(p)
    print(len(valid))

def getindex(a, n):
    """for b()"""
    try:
        result = a[n]
    except:
        return 0
    return result

if __name__ == '__main__':
    li = openfile()
    b()
