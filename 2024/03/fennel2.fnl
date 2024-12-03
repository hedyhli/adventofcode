(fn product-sum [code]
  (accumulate [sum 0
               a b (string.gmatch code "mul%((%d+),(%d+)%)")]
    (+ sum (* a b))))

(fn get-enabled [code]
  (var enabled "")
  (var start 1)
  (var found true)
  (each [i j (string.gmatch code "()don't%(%)()" start)]
    (when found
      (set enabled (.. enabled (string.sub code start (- i 1)))))
    (set found false)
    (local next-start (string.match code "do%(%)()" j))
    (when (not= nil next-start)
      (set found true)
      (set start next-start)))
  enabled)

(fn main [f]
  (local code (accumulate [joined "" line (f:lines)] (.. joined line)))
  (print (product-sum code))
  (print (product-sum (get-enabled (.. code "don't()")))))
  

(local INP "i")
(local f (assert (io.open (if (= INP "s" ) "sample.txt" (= INP "i") "input.txt" INP))))
(main f)
(f:close)
