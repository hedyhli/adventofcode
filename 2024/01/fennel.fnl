(local f (io.open "input.txt"))

(local left [])
(local right [])
(local counter {})
(each [line (f:lines)]
  (local l (line:match "^%d+"))
  (local r (line:match "%d+$"))
  (table.insert left l)
  (table.insert right r)
  (local has (. counter r))
  (tset counter r
        (if (= has nil)
            1
            (+ 1 has))))

(table.sort left)
(table.sort right)

(var total 0)
(for [i 1 (length left)]
  (set total (+ total (math.abs (- (. left i) (. right i))))))

(print total)

;;;;;

(set total 0)
(each [_ num (ipairs left)]
  (local has (. counter num))
  (set total (+ total (* (tonumber num) (if (= has nil) 0 has)))))
(print total)
