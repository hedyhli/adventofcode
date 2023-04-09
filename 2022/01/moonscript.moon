f = io.open "input.txt"

max_n = (topN) ->
  -- Calculate sum of the number groups and find sum of the top topN items
  n = 0
  sums = {}

  for line in f\lines!
    if line == ""
      table.insert sums, n
      n = 0
    else
      n += line

  table.insert sums, n
  table.sort sums

  sum = 0
  for i = #sums, #sums-topN+1, -1
    sum += sums[i]

  return sum

print max_n 1
f\seek "set"
print max_n 3
f\close!
    
