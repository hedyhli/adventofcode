(fn serialize [i j]
  (string.format "%d,%d" i j))

(fn explore [init-i init-j grid rows]
  (var score 0)
  (var total 0)
  (local visited {}) ;; ["i,j"]: true
  (local stack [{ :i init-i :j init-j }])  ;; points
  (while (> (length stack) 0)
    (local {: i : j} (table.remove stack))
    (local height (. (. grid i) j))
    (when (= height 9)
      (set total (+ 1 total))
      (when (not (. visited (serialize i j)))
        (set score (+ 1 score))
        (tset visited (serialize i j) true)))

    (when (not= height 9)
      (each [_ dxy (ipairs [{:i 1 :j 0} {:i -1 :j 0} {:i 0 :j 1} {:i 0 :j -1}])]
        (local {:i di :j dj} dxy)
        (local [newi newj] [(+ i di) (+ j dj)])
        (when (and
               (<= 1 newi rows)
               (<= 1 newj rows)
               (= (+ 1 height) (. (. grid newi) newj)))
          (table.insert stack {:i newi :j newj})))))
  (values score total))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
(fn main [f]
  (local grid (icollect [line (f:lines)]
                (icollect [mat (string.gmatch line ".")]
                  (tonumber mat))))
  (local rows (length grid))
  (var total 0)
  (var total2 0)
  (each [i row (ipairs grid)]
    (each [j c (ipairs row)]
      (when (= 0 c)
        (local (a b) (explore i j grid rows))
        (set total (+ total a))
        (set total2 (+ total2 b)))))
  (print total)
  (print total2))

(local INP :i)
(with-open [f (io.open (if (= INP :s) "sample.txt" (= INP :i) "input.txt" INP))]
  (main f))
