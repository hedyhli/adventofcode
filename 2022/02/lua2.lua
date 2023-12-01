local f = io.open("input.txt")
local lines = {}

for line in f:lines() do
  table.insert(lines, {})
  table.insert(lines[#lines], line:sub(1, 1):byte())
  table.insert(lines[#lines], line:sub(3):byte())
end

f:close()

local score, a, x
----------
--part 1

score = 0
for i = 1, #lines do
  a, x = lines[i][1], lines[i][2]
  score = score + ({3,6,0})[(x-a)%20%3]+x-87
end
print(score)
