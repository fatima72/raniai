"""
You are given a string S.
1)Your task is to print all possible combinations of the string
2)Your task is to print all possible permutations of size k of the string in lexicographic sorted order
3)Your task is to print all possible size k replacement combinations of the string in lexicographic sorted order.
"""
from itertools import permutations,combinations,combinations_with_replacement


S,k = input("Enter a string").split()

k = int(k)



print("Combinations: ",list(combinations(S,k)))
print("Permutations: ",list(permutations(S,k)))
print("Combinations with replacement: ",list(combinations_with_replacement(S,k)))