from aocd import submit

with open(0) as f:
    # tuple of tree heights, for each line, in a list
    # [(1, 2, 3), (4, 5, 6), ...]
    lines = [tuple(map(int, line)) for line in f.read().strip().splitlines()]


def viewdist(current: int, view: list[int], reverse=False) -> int:
    """Calculate the viewing distance of a tree

    Parameters:
        current (int)        Height of current tree in question
        view    (list(int))  List of heights of trees from current view
        reverse (bool)       Whether to reverse the `view` list when checking
                             (used for viewing left and top)

    Returns:
        The number of trees visible from this view.
    """
    n = 0
    iterator = view
    if reverse: iterator = reversed(iterator)
    for i in iterator:
        n += 1
        if current <= i:
            break
    return n


# Part 1
# Number of trees visible from at least 1 side
# Edges     = left/right-most trees + top/bottom-most trees
# Basically = perimeter - 4 (corners repeated)
n_visible = len(lines)*2 + (len(lines[0])-2)*2  # Edges
# Part 2
# Edge trees excluded in part 2 score summation, as at least 1 of the
# view dists =0, hence their scores would be 0
max_score = 0

# For every row excluding first and last
for i in range(1, len(lines)-1):
    row = lines[i]
    # For every column excluding first and last
    for j in range(1, len(row)-1):
        current = row[j]
        # List of tree heights in 4 directions excluding current one
        # top, left, bottom, right: like in CSS :D
        top     = [ l[j] for l in lines[:i] ]
        left    = row[:j]
        bottom  = [ l[j] for l in lines[i+1:] ]
        right   = row[j+1:]
        # Part 1
        if (current > max(left) or current > max(right) or
            current > max(top) or current > max(bottom)):
            n_visible += 1
        # Part 2
        score = 1
        for view in left, top:
            vd = viewdist(current, view, reverse=True)
            score *= vd
        for view in right, bottom:
            vd = viewdist(current, view, reverse=False)
            score *= vd
        # Find the highest score (max_score initialized to 0)
        if score > max_score:
            max_score = score

print(n_visible)
submit(n_visible, "a", 8, 2022)
print(max_score)
submit(max_score, "b", 8, 2022)
