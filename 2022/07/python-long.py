# goal: minimal but readable and maintainable though definetely not golfed (YET)

from collections import defaultdict

from aocd import submit


with open("input.txt") as f:
    lines = f.read().strip().split("\n")


class Path():
    """List of parent directory names

    - Always absolute path from /
    - Path representation, eg: //a/b
    - Allows for slicing of internal path list in self.s(start, end)

    - __add__: append to internal path list
    - __len__: length of internal path list
    - pop:     wraps internal path list's .pop() with no modification
    """
    def __init__(self):
        self.path = []

    def __add__(self, item):
        """Add a dir to the path"""
        self.path.append(item)
        return self

    def s(self, start=0, end=0):
        """__str__ but with list slicing

        Path with leading double slash, each dir joined with "/"
        """
        if not self.path:
            return "/"
        return "/".join(self.path[start:end or len(self.path)])

    def pop(self, *args, **kwargs):
        return self.path.pop(*args, **kwargs)

    def __len__(self):
        return len(self.path)


# ["/", "a", "b", "c"]
parents = Path()
# {"//a/b/c": size (int), ...}
# value = 0 for unknown keys
dirs = defaultdict(int)

i = -1
while i < len(lines)-1:
    i += 1
    if (line:=lines[i]).endswith(".."):
        parents.pop()

    elif line.startswith("$ cd"):
        arg = line[5:]
        parents += arg
        continue

    elif line[0].isdigit():  # file listing
        a = int(line.split(" ")[0])
        for j in range(1, len(parents)+1):
            dirs[parents.s(end=j)] += int(a)


# sum of all **/* dirs with size <1e5
print(s := sum( i for i in dirs.values() if i <= 100_000 ))
submit(s, part="a", day=7, year=2022)

# part 2
#             should free
#           = wanted free - current free
#           = wanted free - (total avai - total used)
should_free = 30_000_000  - 70_000_000 + dirs["/"]
# smallest **/* dir to remove from total, so free space >= 3e7
print(s := sorted( size for size in dirs.values() if size >= should_free )[0])
submit(s, part="b", day=7, year=2022)
