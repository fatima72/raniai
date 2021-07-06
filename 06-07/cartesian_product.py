"""
You are given a two lists A and B. 
Your task is to compute their cartesian product X.
"""

from itertools import product


A = list(map(int,input("Enter Values for A: ").split()))

B = list(map(int,input("Enter Values for B: ").split()))


print(*product(A,B))