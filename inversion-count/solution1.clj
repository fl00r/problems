(defn- merge
  [[left-data left-inversions] [right-data right-inversions]]
  (loop [[l & left :as left-data*] left-data
         [r & right :as right-data*] right-data
         res []
         inversions []]
   (cond 
     (or (and l r (< l r)) (and l (nil? r)))
     (recur left right-data* (conj res l) inversions)
     (or (and l r (> l r)))
     (recur left-data* right (conj res r) (conj inversions [l r]))
     (and r (nil? l))
     (recur left-data* right (conj res r) inversions)
     :else [res (concat left-inversions right-inversions inversions)])))

(defn- split
  [data]
  (-> data count (/ 2) int (split-at data)))

(defn- merge-sort
  [data]
  (if (> (count data) 1)
    (->> data
         split
         (map merge-sort)
         (apply merge))
    [data []]))

(defn inversions-count
  [data]
  (let [[data* inversions] (merge-sort data)]
    (count inversions)))

;;
;; TESTS
;;

(let [data [1, 9, 6, 4, 5]
      res 5
      res* (inversions-count data)]
  (when (not= res res*)
    (throw (Exception. (format "Expected %s got %s" res (doall res*))))))