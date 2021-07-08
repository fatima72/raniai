"""
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution,
and you may not use the same element twice.
You can return the answer in any order.

"""


nums = list(map(int, input().split()))

target = int(input())


def sumoftwo(nums, target):
    s = 0
    for num in range(len(nums)):
        if(nums[num] < target):
            s = target - nums[num]

            for j in range(num+1, len(nums[num:])):

                if nums[j] == s:
                    return (num, j)
    return


print(sumoftwo(nums, target))
