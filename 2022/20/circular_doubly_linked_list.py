# https://adventofcode.com/2022/day/20
#
# Using a Circular Doubly Linked List as the data structure for storing and
# manipulating the list of numbers. Each Node object keeps a reference of the node
# after it as well as prior to it. It also retaisn the original order of the list
# for use during mixing as well as resetting.
#
# This implementation is significantly faster than static_linked_list.py,
# possibly due to these differences:
# - This impl has backward references so list traversal can be sped up
#
# - Indexing lists (as in static_linked_list.py) is slower than using object
#   attribute references (as in this impl).
#
# - The static linked list did not keep index references to previous elements
#   in the list, hence for each iteration in mix(), a list.index() (of O(n))
#   was needed to brute-force the element that is before the current.
#
# - In mix(): When checking whether the current number requires any movement at all,
#   this implementation uses `if n % (self.len-1) == 0` which can catch all
#   known cases where as static_linked_list.py first checks `if num == 0`,
#   manipulate the number as with optimize_traverse_index, then check `if num
#   == 0` again.
#
# - For each mix() call, (which could be many for part 2), the index of the
#   element 0 is set within it, hence a check `if i0 == 0` is done for every
#   iteration, in every mix call. In circular_doubly_linked_list.py, obtaining
#   the node 0 is done during setup, eliminating such need of checking whether a
#   reference to it should be saved on every iteration.
#
# The rest of the details of the two implementations are kept similar.
#
# Nonetheless, this implementation had the need to re-iterate through the input
# during setup to initiate the linked list, whereas in static_linked_list.py,
# input data could be used directly, yet, this impl is still faster.
#
# TODO: Benchmarking required for time and space complexity.
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

import typing as t


def optimize_traverse_index(n: int, total: int) -> int:
    """Flip direction of n if n < 0 to optimize traversal.

    If total length of list is 5:
        1, 2, 3, 4, 5

    - Looking up 7 forward is the same as 2 (forward) (mod total-1)
    - Looking up 4 forward is the same as -1 (backward)

    Returns: int: Optimized index
    """
    backwards = n < 0
    n = abs(n) % total
    if n > total//2:
        n = total - n
        backwards = not backwards
    return -n if backwards else n


class Node:
    """A node in CircularDoublyLinkedList that references the next and previous node.

    Also retains the reference to the node that was originally after it before
    self.next may be modified by CircularDoublyLinkedList.mix().
    """
    def __init__(self, value):
        self.value: int = value
        self.next: Node = None
        self.prev: Node = None
        # Preserving original order of list before mix()-ing
        self.ognext: Node = None
        # Only a .next is needed for iteration, but a .prev is needed for part
        # 2 where the list needs to be reset.
        self.ogprev: Node = None

    def nth_after(self, n: int):
        """Find the nth item after/before self (n != 0)

        Traverse forward if n > 0, backwards if n < 0, and return the resulting
        node.

        Does NOT mod by the list's length for optimization, as the Node object
        does not have the context of the list length, nor is it ideal to keep
        passing that value during this method.
        """
        cur = self
        if n > 0:
            # Branch out early to prevent checking on every iteration
            for _ in range(n):
                cur = cur.next
            return cur
        # n < 0, traverse backwards
        for _ in range(abs(n)):
            cur = cur.prev
        return cur

class CircularDoublyLinkedList:
    """A linked list that wraps with reference to its previous and next node"""

    def __init__(self):
        self.len: int = 0        # Only updated in self.appendleft
        self.tail: Node = None   # Use self.tail.next as iter starting point
        self.node0: Node = None  # Node of the item 0

    def setup(self, numbers: list[int], decryption_key: int = 1):
        """Setup the CDL list using input numbers and optional decryption_key

        Only part one uses this method, where a decryption_key is not used, but
        the feature is still supported if we want to skip part one and setup
        directly with a key.

        NGL it's a bit weird that for the puzzle the decryption_key makes the
        numbers in the data larger, whereas in reality shouldn't encryption
        normally do that?
        """
        for num in reversed(numbers):
            self.appendleft(node := Node(num*decryption_key))
            if self.node0 is None and num == 0:
                self.node0 = node  # Set the node 0 only once when found

    def reset_with_decrkey(self, key: int = 1):
        """Reset the list order and apply a decryption key"""
        for node in self:
            node.next = node.ognext
            node.prev = node.ogprev
            node.value *= key

    def is_empty(self) -> bool:
        return self.tail is None

    def appendleft(self, node: Node):
        """Add a node to the front of the list"""
        self.len += 1
        # Mirror operations to ognext & ogprev
        if self.is_empty():
            self.tail = node
            node.next = node.ognext = node
            node.prev = node.ogprev = node
        else:
            node.next = node.ognext                     = self.tail.next
            self.tail.next.prev = self.tail.next.ogprev = node
            self.tail.next = self.tail.ognext           = node
            node.prev = node.ogprev                     = self.tail

    def __iter__(self) -> t.Generator[Node, None, None]:
        """Iterate through the original order of the list using self.ognext refs"""
        if self.is_empty():
            return
        node = self.tail.ognext
        while node is not self.tail:
            yield node
            node = node.ognext
        yield self.tail

    def iter_mixed(self) -> t.Generator[Node, None, None]:
        """Like self.__iter__ but uses self.next refs possibly modified by self.mix()"""
        if self.is_empty():
            return
        node = self.tail.next
        while node is not self.tail:
            yield node
            node = node.next
        yield self.tail

    def __str__(self) -> str:
        """String reprsentation of items in original order separated by ', '"""
        return ", ".join(str(i.value) for i in self)

    def __repr__(self) -> str:
        return f"<CircularLinkedList {self} of length {self.len}>"

    def print_mixed(self):
        """Print items in the list after mixing"""
        print(", ".join(str(i.value) for i in self.iter_mixed()))

    def mix(self):
        """Do 1 round of mixing"""
        for cur in self:  # Original order must be preserved for mixing order
            n = cur.value
            if n % (self.len-1) == 0:
                # No movement required for these values of n.
                continue
            ## Find where to move it to ##
            # NOTE: Using (self.len-1) because we are looking for the GAPS
            # between items in the list, not the list itself. So for say a list
            # of length 7, where n=6,12,18..., they're equivelent to no
            # movement operation at all.
            n = optimize_traverse_index(n, self.len-1)
            # XXX: If n=0 not caught before this, the following doesn't work,
            # ends up losing .next references. Perhaps it really is better to
            # check n == 0 AFTER optimize_traverse_index()?
            targ = cur.nth_after(n)
            prev = cur.prev
            if n < 0:
                # Do one more as we are moving BEFORE the target this time
                targ = targ.prev
            # Example: To move CUR to the position after TARGET:
            # ... PREV ⇆ CUR ⇆ NEXT ... TARGET ⇆ TNEXT ...
            # 1) Link between PREV and CUR
            prev.next = cur.next
            cur.prev = targ
            # 2) Link between CUR and NEXT
            cur.next.prev = prev
            cur.next = targ.next
            # 3) Link between TARGET and TNEXT
            targ.next.prev = cur
            targ.next = cur

    def result(self, output: bool = True) -> int | tuple[int, list[int]]:
        """Find the 1000th, 2000th, and 3000th item after 0, and their sum"""
        s = 0; coords = []
        start = self.node0
        p = 0
        for n in (1000, 2000, 3000):
            step = optimize_traverse_index(n-p, self.len)
            coords.append(d := start.nth_after(step).value)
            # Sum while looping, so no need to use sum(*coords) outside the
            # method which costs another O(n)
            s += d
            # Incremental lookup: search 1000th from 0, then 1000th from the
            # previous to get 2000th from 0, etc.
            start = start.nth_after(step)
            p = n
        if output:
            print(*coords, sep="  ")
            print("Sum:", s)
            return s
        return s, coords


if __name__ == '__main__':
    import sys
    inputfn = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    from aocd import submit

    ## Setup ##
    with open(0 if inputfn == '-' else inputfn) as f:
        numbers = [ int(l) for l in f.read().splitlines() ]

    cdll = CircularDoublyLinkedList()
    cdll.setup(numbers)
    numbers = None

    ## part 1 ##
    cdll.mix()
    if inputfn == "input.txt":
        submit(cdll.result(), "a", day=20, year=2022)
    else:
        cdll.result()

    ## part 2 ##
    # Reset
    DECR = 811589153; print()
    cdll.reset_with_decrkey(DECR)
    # Vamos!
    for r in range(10):
        print("round", r+1, end="\r")
        cdll.mix()
    if inputfn == "input.txt":
        submit(cdll.result(), "b", day=20, year=2022)
    else:
        cdll.result()
