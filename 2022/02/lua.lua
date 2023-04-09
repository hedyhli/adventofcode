-- based on shell.sh

local mapscore = {
  ['A'] = 1,
  ['B'] = 2,
  ['C'] = 3
}

local mapwin = {
  ['C'] = 'A',
  ['A'] = 'B',
  ['B'] = 'C'
}

local maplose = {
  ['C'] = 'B',
  ['A'] = 'C',
  ['B'] = 'A'
}

local xyz_abc = {
  ['X'] = 'A',
  ['Y'] = 'B',
  ['Z'] = 'C',
}


function part1(col1, col2)
  local score = 0
  abc = xyz_abc[col2]

  if abc == col1 then
    score = score + 3
  end
  if mapwin[col1] == abc then
    score = score + 6
  end
  score = score + mapscore[abc]
  return score
end

-- part 2
local xyz_036 = {
  ['X'] = 0,
  ['Y'] = 3,
  ['Z'] = 6
}

function part2(col1, col2)
  local shape
  local score = 0
  score = score + xyz_036[col2]

  shape = col1
  if col2 == 'X' then
    shape = maplose[col1]
  elseif col2 == 'Z' then
    shape = mapwin[col1]
  end
  return score + mapscore[shape]
end

-- main

local score1 = 0
local score2 = 0
local col1, col2
local f = io.open("input.txt")

for line in f:lines() do
  col1 = line:match("[ABC]")
  col2 = line:match("[XYZ]")
  score1 = score1 + part1(col1, col2)
  score2 = score2 + part2(col1, col2)
end
print(score1)
print(score2)

f:close()
