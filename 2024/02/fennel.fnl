(fn is-safe [row]
  (local inc (< (. row 1) (. row 2)))
  (var return false)
  (var i 2)
  (while (and (not return) (<= i (length row)))
    (local diff (- (. row i) (. row (- i 1))))
    (local this-inc (> diff 0))
    (when (or (not= this-inc inc) (not (<= 1 (math.abs diff) 3)))
      (set return true))
    (set i (+ 1 i)))
  (not return))

(local f (io.open "input.txt"))
(var total-safe 0)
(var tolerate-1-bad 0)

(each [line (f:lines)]
  (local row (icollect [mat (string.gmatch line "%d+")] (tonumber mat)))
  (local safe (is-safe row))
  (when safe
    (set total-safe (+ 1 total-safe)))
  (when (not safe)
    (var passed false)
    ;; Naively bruteforce which level to remove
    (var remove 1)
    (while (and (not passed) (<= remove (length row)))
      (local check (icollect [_ level (ipairs row)] level))
      (table.remove check remove)
      (when (is-safe check)
        (set passed true)
        (set tolerate-1-bad (+ 1 tolerate-1-bad)))
      (set remove (+ 1 remove)))))

(print total-safe)
(print (+ total-safe tolerate-1-bad))
(f:close)
