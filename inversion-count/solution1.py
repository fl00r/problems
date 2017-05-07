#!/bin/python3

#
# O(nlogn)
#

def merge(left, right):
  res = []
  inversions = []
  i = j = 0
  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      res.append(left[i])
      i += 1
    else:
      inversions.append((left[i], right[j]))
      res.append(right[j])
      j += 1
  return res + left[i:] + right[j:], inversions

def split(data):
  mid = int(len(data)/2)
  return data[:mid], data[mid:]

def merge_sort(data):
  if len(data) == 1:
    return data, []

  left, right = split(data)
  left_sort, left_inversions = merge_sort(left)
  right_sort, right_inversions = merge_sort(right)
  data, inversions = merge(left_sort, right_sort)
  return data, left_inversions + right_inversions + inversions

def inversion_count(data):
  _, inversions = merge_sort(data)
  return len(inversions)

#
# TESTS
#

data = [1, 9, 6, 4, 5]
res = 5
res_ = inversion_count(data)
if res_ != res:
  raise(Exception("Expected %s, got %s" % (res, res_)))