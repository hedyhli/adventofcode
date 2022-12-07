from aocd import submit

with open("input.txt") as f:
    lines = f.read().strip().split("\n")


parents = []
dirs = {}

i = -1
while i < len(lines)-1:
    i += 1
    cmd = lines[i][2:]
    if lines[i].startswith("$ cd"):
        if " " in cmd:
            cmd, arg = cmd.split(" ")
        if arg == "..":
            parents.pop(); continue
        parents.append(arg)
        if "/".join(parents) not in dirs.keys():
            dirs["/".join(parents)] = 0
        continue

    elif lines[i] == "$ ls":
        while i < len(lines)-1 and not lines[i+1].startswith('$ '):
            i += 1
            a, b = lines[i].split(" ")
            if a == "dir": continue
            a = int(a)
            for j in range(1, len(parents)+1):
                dirs["/".join(parents[:j])] += int(a)
    else:
        print(lines[i])


print(s:=sum( i for i in dirs.values() if i <= 100_000 ))
submit(s, part="a", day=7, year=2022)

# part 2
available = 70_000_000
free_req  = 30_000_000
total = dirs["/"]

should_free = free_req - (available - total)
print(s := sorted(size for size in dirs.values() if size >= should_free)[0])
submit(s, part="b", day=7, year=2022)
