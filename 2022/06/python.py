from aocd import submit

with open("input.txt") as f:
    s = f.read()

def chars_after_marker(l: int = 4) -> int:
    for i in range(len(s)):
        if len(set(s[i:i+l])) == l: return i+l

print(n := chars_after_marker(4))
submit(n, "a", 6, 2022)
print(n := chars_after_marker(14))
submit(n, "b", 6, 2022)
