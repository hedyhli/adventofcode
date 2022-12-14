path = {}
dirs = {}

for line in io.lines("input.txt") do
    local d = line:match("^$ cd (.+)")
    if d == ".." then
        table.remove(path)
    elseif d then
        table.insert(path, d)
    end
    local size = line:match("^%d+")
    if size then
        size = tonumber(size)
        for i = 1, #path do
            local p = table.concat(path, "/", 1, i)
            dirs[p] = (dirs[p] or 0) + size
        end
    end
end

sum = 0 -- for Part One
should_free = 30000000 - 70000000 + dirs["/"]
min_del = 70000000 -- for Part Two
for _, size in pairs(dirs) do
    if size <= 100000 then
        sum = sum + size
    end
    if size >= should_free and size < min_del then
        min_del = size
    end
end
print("Total size of all dirs <= 100,000")
print(sum)

print("Smallest dir size to be deleted to have 30,000,000 free space")
print(min_del)
