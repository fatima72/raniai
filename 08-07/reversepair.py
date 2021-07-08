"""
Given an integer array nums, return the number of reverse pairs in the array.
A reverse pair is a pair (i, j) where 

0 <= i < j < nums.length and 
nums[i] > 2 * nums[j].

"""


nums = list(map(int, input().split()))


def reversePairs(nums):
    ans = [0]

    def merge(l):
        if len(l) <= 1:
            return l
        list_A = merge(l[:len(l)//2])
        list_B = merge(l[len(l)//2:])

        left = right = 0

        while(left < len(list_A) and right < len(list_B)):
            if list_A[left] <= 2*list_B[right]:
                left += 1
            else:
                ans[0] += len(list_A)-left
                right += 1

        return sorted(list_A+list_B)
    merge(nums)
    return ans[0]


print(reversePairs(nums))
