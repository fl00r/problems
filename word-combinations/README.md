# Combinations of words formed by replacing given numbers with corresponding alphabets

Given a set of positive numbers, find all possible combinations of words formed by replacing the continuous digits with corresponding character of English alphabet. i.e. subset {1} can be replaced by A, {2} can be replaced by B, {1, 0} can be replaced J, {2, 1} can be replaced U, etc..

For example,

Input:  digits[] = { 1, 2, 2 }
Output: ABB, AV, LB

{1, 2, 2} = ABB
{1, 22} = AV
{12, 2} = LB

Input:  digits[] = { 1, 2, 2, 1 }
Output: ABBA, ABU, AVA, LBA, LU

{1, 2, 2, 1} = ABBA
{1, 2, 21} = ABU
{1, 22, 1} = AVA
{12, 2, 1} = LBA
{12, 21} = LU

http://www.techiedelight.com/combinations-of-words-formed-replacing-given-numbers-corresponding-english-alphabet/