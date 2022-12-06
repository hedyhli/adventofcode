f = io.open("input.txt")
input = f:read("*a")
f:close()

a = input:gsub("\n\n(.*)", "")
b = input:gsub("(.*)\n\n", "")
-- crateslen = math.floor((a:find(".\n")+1) / 4)
crates = {}
for line in a:gmatch("([^\n]-)\n") do
    startindex = 1
    for match in line:gmatch("%a") do
        index = line:find(match, startindex, true)
        startindex = index + 1
        n = math.floor((index + 2) / 4)
        crates[n] = match..(crates[n] or "")
    end
end
-- Lazy copy
crates2 = {table.unpack(crates)}

-- -- These only gets the first line match?
-- for a, b, c in b:gmatch("(%d+).+(%d+).+(%d+)") do
--     print(a, b, c)
-- end
-- -- hmm
-- b:gsub("(%d+).+(%d+).+(%d+)\n", function (a, b, c) print(a, b, c) end )
for line in b:gmatch("([^\n]-)\n") do
    n, f, t = line:match("(%d+).+(%d+).+(%d+)")
    f = f - 0
    t = t - 0
    n = n - 0
    l = #crates[f]
    crates[t] = crates[t]..crates[f]:sub(l-n+1):reverse()
    crates[f] = crates[f]:sub(1, l-n)
    crates2[t] = crates2[t]..crates2[f]:sub(l-n+1)
    crates2[f] = crates2[f]:sub(1, l-n)
end

ends = ""
ends2 = ""
for i = 1, #crates do
    ends = ends..crates[i]:sub(-1)
    ends2 = ends2..crates2[i]:sub(-1)
end
print(ends, ends2)
