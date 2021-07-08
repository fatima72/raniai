"""
Pascal Triangle
"""

from itertools import combinations

n = int(input("enter value of row for pascal triangle: "))-1
m = int(input("enter value of column for pascal triangle: "))-1

print(len(list(combinations(list(range(n)), m))))
