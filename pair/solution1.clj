(defn- by-pair
  [numbers sum n]
  (let [m (- sum n)
        mcnt (get numbers m)]
    (when (or (and mcnt (= m n) (> mcnt 1))
              (and mcnt (not= m n) (> mcnt 0)))
      [n m])))

(defn find-pair
  [data sum]
  (let [numbers (frequencies data)]
    (->> data
         (keep (partial by-pair numbers sum))
         first)))

;;
;; TESTS
;;

(let [data [5, 8, 1, 5, 6, 3, 4]
      tests [[10 [5 5]]
             [11 [5 6]]
             [100 nil]]]
  (doseq [[sum res] tests
          :let [res* (find-pair data sum)]
          :when (not= res* res)]
    (throw (Exception. (format "Expected %s got %s" res res*)))))