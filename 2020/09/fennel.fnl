(local f (io.open "input.txt"))
(local prem 25)

(var has {})
(local lines (icollect [line (f:lines)] (tonumber line)))
(f:close)

(for [i 2 prem]
  (tset has (. lines i) true))

(var found false)
(var i (+ 1 prem))
(while (and (not found) (<= i (length lines)))
  (tset has (. lines (- i prem)) nil)
  (var j (- i prem))
  (var has-match false)
  (while (and (not has-match) (not= j i))
    (when (. has (- (. lines i) (. lines j)))
      (set has-match true))
    (set j (+ 1 j)))
  (when (not has-match)
    (set found (. lines i)))
  (tset has (. lines i) true)
  (set i (+ 1 i)))

(print found)

(var start 0)
(var end 0)

(for [i 1 (- (length lines) 1)]
  (var sum (. lines i))
  (for [j (+ 1 i) (length lines)]
    (set sum (+ sum (. lines j)))
    (when (and (= start 0) (= end 0) (= sum found))
      (set start i)
      (set end j))))

(var min math.huge)
(var max 0)
(for [i start end]
  (when (> (. lines i) max)
    (set max (. lines i)))
  (when (< (. lines i) min)
    (set min (. lines i))))

(print (+ min max))
