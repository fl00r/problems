#!/bin/python3

ALPHABET = {i+1: c for i, c in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}

def get_combinations(word):
  res = []
  if len(word) < 2:
    return [word]
  l = word[0]
  for w in get_combinations(word[1:]):
    res.append([l] + w)
  ll = word[0] * 10 + word[1]
  if ALPHABET.get(ll):
    for w in get_combinations(word[2:]):
      res.append([ll] + w)
  return res

def get_words(word):
  res = []
  for w in get_combinations(word):
    letters = "".join(ALPHABET[c] for c in w)
    res.append(letters)
  return res


print(get_words([1, 2, 2, 3, 1]))
print(get_words([2, 2, 2, 2, 2]))
print(get_words([1, 2, 2, 1]))