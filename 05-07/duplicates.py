"""
Remove duplicate items from a given sorted list
"""

def removeDuplicates(nums):
    i = 0
    while(i<len(nums)-1):
        if(nums[i]==nums[i+1]):
            nums.pop(i+1)
        else:
            i+=1
    return len(nums)

print(removeDuplicates([1,2,3,4,4,4]))