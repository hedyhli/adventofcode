(fn Point [i j] {: i : j})

(fn mark-1 [i j rows marked]
  (local in-bounds (and (<= 1 i rows) (<= 1 j rows)))
  (if (and
       in-bounds
       (not (. (. marked i) j)))
      (do
        (tset (. marked i) j true)
        (values 1 in-bounds))
      (values 0 in-bounds)))

(fn mark-antinodes [A B rows marked]
  "Determine antinodes, update `marked', and return the increase of unique locations."
  (var [a b c d] [A.i A.j B.i B.j])
  (when (> a c)
    (set [a b c d] [c d a b]))
  (var dx (math.abs (- b d)))
  (local dy (math.abs (- a c)))
  (when (< b d)
    (set dx (- 0 dx)))
  (+ (. [(mark-1 (- a dy) (+ b dx) rows marked)] 1)
     (. [(mark-1 (+ c dy) (- d dx) rows marked)] 1)))

(fn mark-antinodes2 [A B rows marked]
  "Determine antinodes, update `marked', and return the increase of unique locations."
  (var [a b c d] [A.i A.j B.i B.j])
  (when (> a c)
    (set [a b c d] [c d a b]))
  (var dx (math.abs (- b d)))
  (local dy (math.abs (- a c)))
  (when (< b d)
    (set dx (- 0 dx)))

  (var total (+ (. [(mark-1 a b rows marked)] 1)
                (. [(mark-1 c d rows marked)] 1)))

  (var continue true)
  (var inc 0)
  (while continue
    (set [b a] [(+ b dx) (- a dy)])
    (set [inc continue] [(mark-1 a b rows marked)])
    (set total (+ total inc)))

  (set continue true)
  (while continue
    (set [d c] [(- d dx) (+ c dy)])
    (set [inc continue] [(mark-1 c d rows marked)])
    (set total (+ total inc)))

  total)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
(fn prn [num]
  (print (string.format "%.0f" num)))

(fn main [f]
  (local grid (icollect [line (f:lines)]
                (icollect [mat (string.gmatch line ".")] mat)))
  (var marked (icollect [_ row (ipairs grid)]
                (icollect [_ _ (ipairs row)] false)))
  (local rows (length grid))
  (local freqs {})
  (each [i row (ipairs grid)]
    (each [j f (ipairs row)]
      (when (not= f ".")
        (local new-list (or (. freqs f) []))
        (table.insert new-list (Point i j))
        (tset freqs f new-list))))

  (var uniqs 0)
  (each [_ list (pairs freqs)]
    (for [a 1 (length list)]
      (for [b 1 (- a 1)]
        (set uniqs (+ uniqs (mark-antinodes (. list a) (. list b) rows marked))))))
  (print uniqs)

  (set marked (icollect [_ row (ipairs grid)] (icollect [_ _ (ipairs row)] false)))
  (set uniqs 0)
  (each [f list (pairs freqs)]
    (for [a 1 (length list)]
      (for [b 1 (- a 1)]
        (set uniqs (+ uniqs (mark-antinodes2 (. list a) (. list b) rows marked))))))
  (print uniqs)
  )

(local INP "i")
(local f (assert (io.open (if (= INP "s" ) "sample.txt" (= INP "i") "input.txt" INP))))
(main f)
(f:close)
