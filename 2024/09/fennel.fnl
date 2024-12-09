

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
(fn prn [num]
  (print (string.format "%.0f" num)))

(fn print-table [grid repr]
  "(print-table table (fn [m] (tostring m)))"
  (each [_ row (ipairs grid)]
    (print (accumulate [s ""
                        _ m (ipairs row)]
             (.. s (repr m))))))

(fn clone-table [tab init]
  "(clone table (fn [it] it))"
  (icollect [_ row (ipairs tab)]
    (icollect [_ item (ipairs row)]
      (init item))))

(fn s-index [string i]
  (tonumber (string.sub string i i)))

(fn part1 [line]
  (var checksum 0)
  (var j (length line))
  (var idx 0)      ; block id
  (var disk-idx 0)
  (var back-idx (math.floor (/ (- j 1) 2))) ; block id
  (var back-count (s-index line j)) ; count down
  (var is-gap false)
  (for [i 1 (length line) &until (= i j)]
    (local len (s-index line i))

    (when (not is-gap)
      (for [_ 1 len]
        (set checksum (+ checksum (* idx disk-idx)))
        (set disk-idx (+ 1 disk-idx)))
      (set idx (+ 1 idx)))

    (when is-gap
      (for [_ 1 len &until (= i j)]
        (when (not= 0 back-count)
          (set checksum (+ checksum (* back-idx disk-idx)))
          (set disk-idx (+ 1 disk-idx))
          (set back-count (- back-count 1)))
        (when (= 0 back-count)
          (set j (- j 2)) ; is the last number always not gap??
          (set back-count (s-index line j))
          (set back-idx (- back-idx 1)))
        ))

    (set is-gap (not is-gap)))

  (when (not is-gap)
    (for [_ 1 back-count]
      (set checksum (+ checksum (* back-idx disk-idx)))
      (set disk-idx (+ 1 disk-idx))))
  checksum)

(fn main [f]
  (local line (f:read))
  (print (part1 line)))

(local INP "i")
(local f (assert (io.open (if (= INP "s" ) "sample.txt" (= INP "i") "input.txt" INP))))
(main f)
(f:close)
