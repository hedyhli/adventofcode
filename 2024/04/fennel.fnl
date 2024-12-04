(fn count-matches [word lines]
  (local word-1 (- (length word) 1))
  (accumulate [total 0
               _ line (ipairs lines)]
    (+ total (faccumulate [count 0
                           i 1 (- (length line) word-1)]
               (+ count (if (= word (string.sub line i (+ i word-1)))
                            1
                            0))))))

(fn count-both [lines]
  (+ (count-matches "XMAS" lines) (count-matches "SAMX" lines)))

(fn transpose [lines]
  "Tranposes each column from bottom to top."
  (local transposed [])
  (for [i 1 (length (. lines 1))]
    (var column "")
    (for [j 1 (length lines)]
      (set column (.. (string.sub (. lines j) i i) column)))
    (table.insert transposed column))
  transposed)

(fn diagonal [lines]
  "Top-left to bottom-right."
  (local rows (length lines))
  (local result [])
  (for [i 1 rows]
    (var diag "")
    (var x i)
    (var y 1)
    (while (and (>= x 1) (<= y rows))
      (set diag (.. diag (string.sub (. lines x) y y)))
      (set x (- x 1))
      (set y (+ y 1)))
    (table.insert result diag))
  (for [j 2 rows]
    (var diag "")
    (var x rows)
    (var y j)
    (while (and (>= x 1) (<= y rows))
      (set diag (.. diag (string.sub (. lines x) y y)))
      (set x (- x 1))
      (set y (+ y 1)))
    (table.insert result diag))
  result)

(fn flip [lines]
  (icollect [_ line (ipairs lines)] (string.reverse line)))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; helpers for part 2

(fn count-ms [M S lines]
  (local len-2 (- (length lines) 2))
  (local ms-map (icollect [_ line (ipairs lines)]
                  (do
                    (local map {})
                    (for [i 1 len-2]
                      (local is-match (and
                                       (= M (string.sub line i i))
                                       (= S (string.sub line (+ i 2) (+ i 2)))))
                      (table.insert map is-match))
                    map)))
  (var count 0)
  (for [i 1 len-2]
    (for [j 1 len-2]
      (when (and
             (. (. ms-map i) j)
             (. (. ms-map (+ 2 i)) j))
        (local a-pos (+ 1 j))
        (when (= (string.sub (. lines (+ 1 i)) a-pos a-pos) "A")
          (set count (+ 1 count))))))
  count)

(fn count-ms-both [lines]
  (+ (count-ms "M" "S" lines) (count-ms "S" "M" lines)))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
(fn main [f]
  (local lines (icollect [line (f:lines)] line))
  ;; 1
  (local checks [lines (transpose lines)
                 (diagonal lines) (diagonal (flip lines))])
  (print (accumulate [sum 0
                      _ check (ipairs checks)]
           (+ sum  (count-both check))))
  ;; 2
  (local checks [lines (transpose lines)])
  (print (accumulate [sum 0
                      _ check (ipairs checks)]
           (+ sum (count-ms-both check)))))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
(local INP "i")
(local f (assert (io.open (if (= INP "s" ) "sample2.txt" (= INP "i") "input.txt" INP))))
(main f)
(f:close)
