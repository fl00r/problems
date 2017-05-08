(defn- permutations*
  [data r]
  (when (> r 0)
    (mapcat 
      (fn [d] 
        (map
          (partial concat [d])
          (permutations* (remove (partial = d) data) (dec r))))
      data)))

(defn permutations
  ([data] (permutations data (count data)))
  ([data r] (permutations* (concat data data))))

(prn (permutations* [1 2 3] 3))