import sys  
import sys  
"""
sort them in-place so that objects of the same color are adjacent,
You must solve this problem without using the library's sort function.
Do not return anything, modify nums in-place instead.
"""
from collections import Counter


nums = [2,1,0,2,0]
counts = Counter(nums)
nums[:] = [0] * counts[0] + [1] * counts[1] + [2] * counts[2]
print(nums)

