(defn- trick
  [number]
  (let [number* (str number)]
    (str number* (last number*))))

(defn largest-number
  [numbers]
  (->> numbers
       (sort-by trick)
       reverse
       clojure.string/join
       Long.))

;;
;; TESTS
;;

(let [data [10, 68, 75, 7, 21, 12]
      res 77568211210
      res* (largest-number data)]
  (when (not= res res*)
    (throw (Exception. (format "Expected %s got %s" res (doall res*))))))