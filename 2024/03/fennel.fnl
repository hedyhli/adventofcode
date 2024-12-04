(fn main [f]
  (var sum 0)
  (var sum2 0)
  (var enable true)
  (each [line (f:lines)]
    (each [func i (string.gmatch line "([muldon't]+)%(()")]
      (local empty (= ")" (string.sub line i i)))
      (if (and (= (string.match func "do$") "do") empty)
          (set enable true)

          (and (= (string.match func "don't$") "don't") empty)
          (set enable false)

          (and (= (string.match func "mul$") "mul") (not empty))
          (do
            (local nums [(string.match line "^(%d+),(%d+)%)" i)])
            (when (= 2 (length nums))
              (local product (* (. nums 1) (. nums 2)))
              (set sum (+ sum product))
              (when enable
                (set sum2 (+ sum2 product))))))))
  (print sum)
  (print sum2))

(local INP "i")
(local f (assert (io.open (if (= INP "s" ) "sample.txt" (= INP "i") "input.txt" INP))))
(main f)
(f:close)
