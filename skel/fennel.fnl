

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
(fn main [f]
  (each [line (f:lines)]
    ;; (each [mat (string.gmatch line "%d+")])
    ))

(local INP "s")
(local f (assert (io.open (if (= INP "s" ) "sample.txt" (= INP "s") "input.txt" INP))))
(main f)
(f:close)
