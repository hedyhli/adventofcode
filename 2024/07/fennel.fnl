
(fn try [want start have i]
  (if (> i (length have))
      (= want start)
      (or (try want (* start (. have i)) have (+ i 1))
          (try want (+ start (. have i)) have (+ i 1)))))

(fn concat [a b]
  (tonumber (.. (tostring a) (tostring b))))

(fn try2 [want start have i]
  (if (> i (length have))
      (= want start)
      (or (try2 want (* start (. have i)) have (+ i 1))
          (try2 want (+ start (. have i)) have (+ i 1))
          (try2 want (concat start (. have i)) have (+ 1 i)))))


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
(fn prn [num] (print (string.format "%.0f" num)))
(fn main [f]
  (var total 0)
  (var extra 0)
  (var i 0)
  (each [line (f:lines)]
    (set i (+ 1 i))
    (local [need rest] [((string.gmatch line "(%d+): (.*)"))])
    (local numbers (icollect [mat (string.gmatch rest "%d+")] (tonumber mat)))
    (if (try (tonumber need) (. numbers 1) numbers 2)
        (set total (+ need total))
        (try2 (tonumber need) (. numbers 1) numbers 2)
        (set extra (+ need extra))
        ))
  (prn total)
  (prn (+ total extra)))

(local INP "i")
(local f (assert (io.open (if (= INP "s" ) "sample.txt" (= INP "i") "input.txt" INP))))
(main f)
(f:close)
