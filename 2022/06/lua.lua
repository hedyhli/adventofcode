f = io.open("input.txt")
stream = f:read()
f:close()

function marker_index(l)
    l = l-1
    for i = 1, #stream do
        window = stream:sub(i, i+l)
        unique = true

        for j in window:gmatch(".") do
            if window:gsub(j, "", 1):find(j) then
                unique = false
            end
        end

        if unique then return i+l end
    end
end

-- 1 2 3 4

print(marker_index(4))
print(marker_index(14))
