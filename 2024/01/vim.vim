let lines = readfile("input.txt")
let left = []
let right = []
let counter = {}

for line in lines
  let nums = split(line, "   ")
  let left = add(left, nums[0])
  let right = add(right, nums[1])
  let counter[nums[1]] = get(counter, nums[1], 0) + 1
endfor

let left = sort(left)
let right = sort(right)

let i = 0
let t = 0
let t2 = 0
while i < len(left)
  let t = t + abs(left[i] - right[i])
  let t2 = t2 + left[i] * get(counter, left[i], 0)
  let i = i + 1
endwhile
echo t
echo t2
