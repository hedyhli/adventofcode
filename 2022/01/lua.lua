local f = io.open("input.txt")

if f == nil then
  print("error: could not open input file")
  os:exit()
end

function max_of(topN)
  -- Returns sum of the highest topN
  local n = 0
  local sums = {}

  for line in f:lines() do
    if line == "" then
      table.insert(sums, n)
      n = 0
    else
      n = n + line
    end
  end
  table.insert(sums, n)  -- Add last item
  table.sort(sums)
  local sum = 0
  for i = #sums, #sums-topN+1, -1 do
    sum = sum + sums[i]
  end
  return sum
end

print(max_of(1))
f:seek("set")
print(max_of(3))
f:close()
