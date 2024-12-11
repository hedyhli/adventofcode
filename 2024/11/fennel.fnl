(fn split [stone]
  (local s (tostring stone))
  (local l (math.floor (/ (length s) 2)))
  (values (tonumber (string.sub s 1 l))
          (tonumber (string.sub s (+ 1 l) (length s)))))

(local cache {})

(fn blink-1 [stone times]
  (local key (string.format "%d,%d" stone times))
  (fn save [x] (tset cache key x) x)
  (local hit (. cache key))
  (if (not= nil hit)
      hit
      (= times 0)
      (save 1)
      (= stone 0)
      (save (blink-1 1 (- times 1)))
      (= 0 (% (length (tostring stone)) 2))
      (do
        (local (a b) (split stone))
        (save (+ (blink-1 a (- times 1))
                 (blink-1 b (- times 1)))))
      ;; else
      (save (blink-1 (* 2024 stone) (- times 1)))))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
(fn prn [num]
  (print (string.format "%.0f" num)))

(fn main [f]
  (local stones (icollect [mat (string.gmatch (f:read) "%d+")]
                  (tonumber mat)))
  (local total (accumulate [t 0
                            _ stone (ipairs stones)]
                 (+ t (blink-1 stone 25))))
  (local total2 (accumulate [t 0
                            _ stone (ipairs stones)]
                  (+ t (blink-1 stone 75))))
  (print total)
  (prn total2))

(local INP :i)
(with-open [f (io.open (if (= INP :s) "sample.txt" (= INP :i) "input.txt" INP))]
  (main f))
