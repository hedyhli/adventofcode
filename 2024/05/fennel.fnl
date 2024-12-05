(fn clone [list]
  (icollect [_ item (ipairs list)] item))

(fn contains [item list]
  (var found false)
  (when (not= nil list)
    (each [_ cmp (ipairs list) &until found]
      (set found (= cmp item))))
  found)

(fn get-middle [list]
  (. list (math.ceil (/ (length list) 2))))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
(fn main [f]
  ;; [number]: [these must be before key]
  ;; each key must be before each val
  (local rules {})
  (each [line (f:lines) &until (= line "")]
    (local [a b] [((string.gmatch line "(%d+)%|(%d+)"))])
    (local before (. rules (tonumber a)))
    (local new-before (if (not= nil before) before []))
    (table.insert new-before (tonumber b))
    (tset rules (tonumber a) new-before))

  (local pagelist (icollect [line (f:lines)]
                    (icollect [mat (string.gmatch line "%d+")] (tonumber mat))))

  (var result 0)
  (var result2 0)

  (each [_ pages (ipairs pagelist)]
    (var ok true)
    (each [i page (ipairs pages) &until (not ok)]
      (each [j bef (ipairs pages) &until (or (= j i) (not ok))]
        (set ok (not (contains bef (. rules page))))))

    (when ok
      (local middle (get-middle pages))
      (set result (+ result middle)))
    (when (not ok)
      (local sorted (clone pages))
      ;; whether a should be before b
      (table.sort sorted (fn [a b] (contains b (. rules a))))
      (local middle (get-middle sorted))
      (set result2 (+ result2 middle))))

  (print result)
  (print result2))

(local INP "i")
(local f (assert (io.open (if (= INP "s" ) "sample.txt" (= INP "i") "input.txt" INP))))
(main f)
(f:close)
