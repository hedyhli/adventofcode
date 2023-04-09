local letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
local f = io.open("input.txt")

function part1(f)
  local p = 0
  for line in f:lines() do
    local half = #line / 2 + 1
    local left = line:sub(1, half)
    local right = line:sub(half, #line)

    for char in left:gmatch"." do
      if right:match(char) then
        p = p + letters:find(char)
        -- only finds one repeated occurence of a char
        break
      end
    end
  end
  return p
end

function part2(f)
  local p = 0
  for line in f:lines() do
    local line1 = line
    local line2 = f:read()
    local line3 = f:read()

    for char in line1:gmatch"." do
      if line2:match(char) and line3:match(char) then
        p = p + letters:find(char)
        break
      end
    end
  end
  return p
end

print(part1(f))
f:seek('set')
print(part2(f))
f:close()
