from aocd import submit


# Adjustable lmao (part two)
KNOTS_LEN = 9


class Coord:
    """Two dimensional x/y pair coordinates"""

    def __init__(self, x=0, y=0):
        """Initialize at origin or given point"""
        self.x = x
        self.y = y

    def __eq__(self, o):
        return self.x == o.x and self.y == o.y

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def move(self, di, units=1):
        """Move by given direction L/R/U/D by given number of units"""
        units = -units if di in ("L", "D") else units
        if di in ("R", "L"):
            self.x += units
        else:
            self.y += units

    def touching(self, o):
        """Whether two points are adjacent/diagonal/overlapping"""
        return abs(self.x - o.x) < 2 and abs(self.y - o.y) < 2

    def keepup(T, H):
        """Move self by one unit so that it becomes closer to (touching with) H

        Examples (_ = empty,  .=previous)
        ------------------

        H _ T   ->   H T .

        ------------------
          T            .
          _     ->     T
          H            H

        ------------------
        _ _ T   ->   _ _ .
        H _ _        H T _

        ------------------
        T _           . _
        _ _     ->    _ T
        _ H           _ H

        """
        if T.touching(H): return

        if T.x != H.x:
            T.move("L" if T.x > H.x else "R")
        if T.y != H.y:
            T.move("D" if T.y > H.y else "U")


H = Coord()
knots = [ Coord() for _ in range(KNOTS_LEN) ]

# set of strings
crumb1 = {"(0, 0)"}     # Part 1
crumb_tail = {"(0, 0)"} # Part 2

with open("input.txt") as f:
    movements = f.readlines()

for move in movements:
    di, amt = move.split(" ", maxsplit=2)
    amt = int(amt)
    for _ in range(amt):
        H.move(di)
        knots[0].keepup(H)
        for i in range(1, len(knots)):
            knots[i].keepup(knots[i-1])
        crumb1.add(str(knots[0]))
        crumb_tail.add(str(knots[-1]))


print(s := len(crumb1))
submit(s, "a", 9, 2022)
print(s := len(crumb_tail))
submit(s, "b", 9, 2022)
