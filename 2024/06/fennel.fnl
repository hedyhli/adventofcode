;;
;; All coordinates are 1-indexed
;;
;; Guard pos:
;; { :x 0 :y 0 :dir :up/:down/:left/:right }
;;
;; Grid is a list of rows
;; top right is 10,10, top left is 1,1
;; coord (x, y) is at:
;; (. (. grid y) x)
;;
;; Possible approach for faster solution:
;; - Patrolling:
;;   Use a x-y and y-x map to get a list of y coordinates for a give x
;;   coordinate and vice-versa, to quickly find the next obstacle.
;;   See find-> and find-<
;;   Find intersections of path segments (see) to compute the updated
;;   visit-count value. This can be trivial because there can never be
;;   two colinear segments without looping.
;; - Brute-force search can be restricted to the visited path.

(fn exiting? [guard rows]
  (or (and (= guard.x 0)    (= guard.dir :left))
      (and (= guard.x rows) (= guard.dir :right))
      (and (= guard.y 0)    (= guard.dir :down))
      (and (= guard.y rows) (= guard.dir :up))))

;; (fn find-> [item list]
;;   ;; XXX: Not a binary search yet
;;   (local default (length list))
;;   (accumulate [result default
;;                _ check (ipairs list)
;;                &until (not= default result)]
;;     (if (> check item) (- check 1) default)))

;; (fn find-< [item list]
;;   (local default 1)
;;   (accumulate [result default
;;                _ check (ipairs list)
;;                &until (not= default result)]
;;     (if (< check item) (+ check 1) default)))

(fn set-new-direction [guard]
  (tset guard :dir (if (= guard.dir :up)
                       :right
                       (= guard.dir :right)
                       :down
                       (= guard.dir :down)
                       :left
                       (= guard.dir :left)
                       :up)))

(fn get-cell [x y grid]
  (. (. grid y) x))

(fn visit [x y grid dir]
  "Update grid and return increase in visits and whether we're looping"
  (local cell (get-cell x y grid))
  (if cell.visited
      (values 0 (= cell.dir dir))
      ;; else
      (do
        (tset cell :visited true)
        (tset cell :dir dir)
        (values 1 false))))

(fn patrol [guard grid]
  "Update `grid' and return the increase in visits and whether we're exiting."
  (var inc 0)
  (var x guard.x)
  (var y guard.y)
  (var exited false)
  (var stop false)
  (var looping false)
  (while (not stop)
    (tset guard :x x)
    (tset guard :y y)
    (local [new-inc new-looping] [(visit x y grid guard.dir)])
    (when new-looping
      (set looping true)
      (set stop true))
    (when (not new-looping)
      (set inc (+ inc new-inc))
      (set x (+ x (if (= guard.dir :right) 1
                      (= guard.dir :left) -1
                      0)))
      (set y (+ y (if (= guard.dir :up) 1
                      (= guard.dir :down) -1
                      0)))
      (if (or
           (not (<= 1 x (length grid)))
           (not (<= 1 y (length grid))))
          ;;then
          (do
            (set stop true)
            (set exited true))
          ;;else
          (when (. (get-cell x y grid) :ob)
            (set stop true))))
    )
  (values inc exited looping))

(fn patrol-all [guard grid]
  (var visits 0)
  (var stop false)
  (var loops false)
  (while (not stop)
    (local [inc exited looped] [(patrol guard grid)])
    (set stop (or exited looped))
    (set loops looped)
    (set visits (+ visits inc))
    (when (not exited)
      (set-new-direction guard)))
  (values visits loops))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
(fn main [f]
  (local grid (icollect [line (f:lines)]
                (icollect [_ (string.gmatch line ".")] {})))
  (f:seek "set")
  (var guard {})
  (local rows (length grid))
  (var y rows)
  (each [line (f:lines)]
    (var x 1)
    (each [ch (string.gmatch line ".")]
      (if (= ch "#")
          (tset (get-cell x y grid) :ob true))
      (if (= ch "^")
          (set guard {:x x :y y :dir :up})
          (= ch ">")
          (set guard {:x x :y y :dir :right})
          (= ch "<")
          (set guard {:x x :y y :dir :left})
          (= ch "v")
          (set guard {:x x :y y :dir :down}))
      (set x (+ 1 x)))
    (set y (- y 1)))

  ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

  (local initial {:x guard.x :y guard.y :dir guard.dir})
  (local [visits _] [(patrol-all guard grid)])
  (print visits)

  ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
  (var options 0)
  (for [j rows 1 -1]
    (print j)
    (for [i 1 rows]
      (when (and
             (not (. (get-cell i j grid) :ob))
             (or (not= j initial.y) (not= i initial.x)))
        (for [k 1 rows]
          (for [l 1 rows]
            (tset (get-cell k l grid) :visited false)
            (tset (get-cell k l grid) :dir nil)))
        (tset (get-cell i j grid) :ob true)
        (local g {:x initial.x :y initial.y :dir initial.dir})
        (local [_ loops] [(patrol-all g grid)])
        (when loops
          (set options (+ 1 options)))
        (tset (get-cell i j grid) :ob false))))
  (print "")
  (print options)

  )

(local INP "i")
(local f (assert (io.open (if (= INP "s" ) "sample.txt" (= INP "i") "input.txt" INP))))
(main f)
(f:close)
