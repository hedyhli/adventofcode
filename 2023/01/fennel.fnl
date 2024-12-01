(local f (io.open "input.txt"))

(when (= f nil)
  (print "Unable to open input file.")
  (os.exit 1))

;; p1
(var total 0)
(each [line (f:lines)]
  (var first "")
  (var last "")
  (each [digit (string.gmatch line "%d")]
    (when (= first "")
        (set first digit))
    (set last digit))
  (local calib (tonumber (.. first last)))
  (set total (+ total calib)))

(print total)

;; p2
(f:seek "set")

(local words ["one" "two" "three" "four" "five" "six" "seven" "eight" "nine"])
(local lookup {})
(each [i word (ipairs words)]
  (tset lookup word (tostring i)))
(for [i 1 9]
  (tset lookup (tostring i) (tostring i)))

(var total 0)

(each [line (f:lines)]
  (var first "")
  (var last "")
  (for [i 1 (length line)]
    (each [check num (pairs lookup)]
      (local have
             (string.sub line i (- (+ i (length check)) 1)))
      (when (= have check)
        (when (= first "")
          (set first num))
        (set last num))))

  (set total (+ total (tonumber (.. first last)))))

(print total)
