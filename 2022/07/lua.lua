
path = {}
dirs = {}

for line in io.lines("input.txt") do
    d = line:match("^$ cd (.+)")
    if d == ".." then
        table.remove(path)
    elseif d then
        table.insert(path, d)
    end
    size = line:match("^%d+")
    if size then
        size = tonumber(size)
        for i = 1, #path do
            p = table.concat(path, "/", 1, i)
            -- print(p)
            dirs[p] = (dirs[p] or 0) + size
        end
    end
end

sum = 0 -- for Part One
should_free = 30000000 - 70000000 + dirs["/"]
candidates = {} -- for Part Two
for _, size in pairs(dirs) do
    if size <= 100000 then
        sum = sum + size
    end
    if size >= should_free then
        table.insert(candidates, size)
    end
end
print("Total size of all dirs <= 100,000")
print(sum)

table.sort(candidates)
print("Smallest dir size to be deleted to have 30,000,000 free space")
print(candidates[1])
