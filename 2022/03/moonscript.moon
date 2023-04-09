letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
f = io.open "input.txt"

part1 = ->
  p = 0
  for line in f\lines!
    half = #line / 2 + 1
    left = line\sub 1, half
    right = line\sub half, #line
    for char in left\gmatch "."
      if right\match char
        p = p + letters\find char
        break
  return p

part2 = ->
  p = 0
  for line in f\lines!
    line1 = line
    line2 = f\read!
    line3 = f\read!

    for char in line1\gmatch "."
      if (line2\match char) and (line3\match char)
        p = p + letters\find char
        break
  return p

print part1!
f\seek 'set'
print part2!
f\close!
