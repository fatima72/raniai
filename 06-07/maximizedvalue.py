"""
You are given a function f(X)=X^2.
You are also given K lists. 
The ith list consists of Ni elements.
You have to pick one element from each list so that the value from the equation below is maximized
Find the maximized value  obtained.
"""

from itertools import product
K, M = map(int,input().split())
def Sq(n):
    return int(n)**2
List = []
for i in range(K):
    List.append(list(map(Sq,input().split()[1:])))
Max=0    
for T in product(*List):
    Sum=sum(T)%M
    if Sum>Max:   #finding maximum sum out of all tuples
        Max=Sum
print(Max)