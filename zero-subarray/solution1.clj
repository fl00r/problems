(defn- get-subarrays
  [data]
  (loop [[head & tail] data
         intermediate-vec []
         intermediate-sum 0
         res []]
    (if head
      (let [intermediate-sum (+ intermediate-sum head)
            intermediate-vec (conj intermediate-vec head)]
        (if (= intermediate-sum 0)
          (recur tail intermediate-vec intermediate-sum (conj res intermediate-vec))
          (recur tail intermediate-vec intermediate-sum res)))
      res)))

(defn subarray
  [numbers]
  (->> numbers
       (iterate rest)
       (take-while seq)
       (mapcat get-subarrays)
       (filter seq)
       (into #{})))

;;
;; TESTS
;;

(let [data [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]
      res #{[3, 4, -7],
            [4, -7, 3],
            [-7, 3, 1, 3],
            [3, 1, -4],
            [3, 1, 3, 1, -4, -2, -2],
            [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]}
      res* (subarray data)]
  (when (not= res res*)
    (throw (Exception. (format "Expected %s got %s" res res*)))))