

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
(fn prn [num]
  (print (string.format "%.0f" num)))

(fn print-table [grid repr]
  "(print-table table (fn [m] (tostring m)))"
  (each [_ row (ipairs grid)]
    (print (accumulate [s ""
                        _ m (ipairs row)]
             (.. s (repr m))))))

(fn clone-table [tab init]
  "(clone table (fn [it] it))"
  (icollect [_ row (ipairs tab)]
    (icollect [_ item (ipairs row)]
      (init item))))

(fn main [f]
  (each [line (f:lines)]
    ;; (each [mat (string.gmatch line "%d+")])
    ))

(local INP "s")
(local f (assert (io.open (if (= INP "s" ) "sample.txt" (= INP "i") "input.txt" INP))))
(main f)
(f:close)
