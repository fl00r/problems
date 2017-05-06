(defn sort-binary
  [data]
  (let [data* (group-by identity data)]
    (concat (get data* 0) (get data* 1))))

;;
;; TESTS
;;

(let [data [1, 0, 1, 0, 1, 0, 0, 1]
      res [0, 0, 0, 0, 1, 1, 1, 1]
      res* (sort-binary data)]
  (when (not= res res*)
    (throw (Exception. (format "Expected %s got %s" res (doall res*))))))