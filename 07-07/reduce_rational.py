"""
Demontraring the use of reduce function and lambda function
Given a list of rational numbers,find their product.
Reduce the fraction to its lowest form

Input: First line contains , the number of rational numbers. The  of next  lines contain two integers each, the numerator(  ) and denominator(  ) of the  rational number in the list.
Output: Print only one line containing the numerator and denominator of the product of the numbers in the list in its simplest form
"""
from functools import reduce
from math import gcd

numerator = 1
denominator = 1
n = int(input())
for i in range(n):
    nr,d = list(map(int,input().split()))
    numerator*=nr
    denominator*=d


d = gcd(numerator,denominator)

print(numerator//d,denominator//d)
