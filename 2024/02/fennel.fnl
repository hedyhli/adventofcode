(fn is-gradient [row]
  "Either all increasing or all decreasing."
  (local inc (< (. row 1) (. row 2)))
  (faccumulate [ok true
                i 2 (length row)
                &until (not ok)]
    (= inc (< (. row (- i 1)) (. row i)))))

(fn diff-within [lo hi row]
  "Whether all absolute differences are >= lo and <= hi."
  (faccumulate [ok true
                i 2 (length row)
                &until (not ok)]
    (<= lo (math.abs (- (. row i) (. row (- i 1)))) hi)))

(fn is-safe [row]
  "Whether this single report is safe."
  (and (is-gradient row) (diff-within 1 3 row)))

(fn has-removable-level [row]
  "Naively bruteforce whether removing a level makes the report safe."
  (faccumulate [found false
                remove 1 (length row)
                &until found]
    (is-safe (icollect [i level (ipairs row)]
               (if (not= i remove) level)))))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(fn main [f]
  (var total-safe 0)
  (var tolerate-1-bad 0)

  (each [line (f:lines)]
    (local row (icollect [mat (string.gmatch line "%d+")] (tonumber mat)))
    (local safe (is-safe row))
    (if safe
        (set total-safe (+ 1 total-safe))
        ;; else
        (when (has-removable-level row)
          (set tolerate-1-bad (+ 1 tolerate-1-bad)))))

  (print total-safe)
  (print (+ total-safe tolerate-1-bad)))


(local f (io.open "input.txt"))
(main f)
(f:close)
