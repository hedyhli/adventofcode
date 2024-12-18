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

(fn part2 [line]
  (local start {}) ;; not a real node
  (var ptr start)
  (var idx 0)
  (var is-gap false)
  (local list []) ;; non-gaps
  (for [i 1 (length line)]
    (local len (s-index line i))
    (local this {: len : idx : is-gap})
    (when is-gap
      (set idx (+ 1 idx)))
    (tset ptr :next this)
    (set ptr this)
    (when (not is-gap)
      (table.insert list this))
    (set is-gap (not is-gap)))

  (var qtr (. list (length list))) ;; to be moved
  (set ptr start) ;; to find the first adequate gap

  (for [q (length list) 2 -1]
    (local qtr (. list q))
    (set ptr start)
    (var prev-ptr ptr)
    (var found false)
    (while (and (not found) (not= qtr ptr.next))
      (set prev-ptr ptr)
      (set ptr ptr.next)
      (when ptr.is-gap
        (when (<= qtr.len ptr.len)
          (set found true)
          (tset qtr :is-gap true)
          (local new-qtr {:len qtr.len :is-gap false :idx qtr.idx :next ptr})
          (tset prev-ptr :next new-qtr)
          (tset ptr :len (- ptr.len qtr.len))
          ;; TODO: Why doesn't the below work?
          ;; (when (< qtr.len ptr.len)  ;; update self
          ;;   (tset ptr :len (- ptr.len qtr.len)))
          ;; (when (= qtr.len ptr.len)  ;; detach self
          ;;   (tset new-qtr :next ptr.next))
          ))))

  (var checksum 0)
  (var disk-idx 0)
  (set ptr start)
  (while (not= nil ptr.next)
    (set ptr ptr.next)
    (when (not ptr.is-gap)
      (for [i 0 (- ptr.len 1)]
        (set checksum (+ checksum (* ptr.idx (+ disk-idx i))))))
    (set disk-idx (+ disk-idx ptr.len)))

  (when (not= checksum 6431472344710)
    (print "incorrect!"))
  checksum)

(fn main [f]
  (local line (f:read))
  (print (part1 line))
  (print (part2 line)))

(local INP "i")
(local f (assert (io.open (if (= INP "s" ) "sample.txt" (= INP "i") "input.txt" INP))))
(main f)
(f:close)
