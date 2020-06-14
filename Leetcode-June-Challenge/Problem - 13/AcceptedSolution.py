##==================================
## Leetcode June Challenge 
## Username: Vanditg
## Year: 2020
## Problem: 13
## Problem Name: Largest Divisible Subset
##===================================
#
#Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of 
#elements in this subset satisfies:
#
#Si % Sj = 0 or Sj % Si = 0.
#
#If there are multiple solutions, return any subset is fine.
#
#Example 1:
#
#Input: [1,2,3]
#Output: [1,2] (of course, [1,3] will also be ok)
#Example 2:
#
#Input: [1,2,4,8]
#Output: [1,2,4,8]
class Solution:
    def largestDivisibleSubset(self, nums):
        if len(nums) == 0:
            return []
        nums.sort()
        tmp = [[num] for num in nums]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(tmp[i]) < len(tmp[j]) + 1:
                    tmp[i] = tmp[j] + [nums[i]]
        return max(tmp, key = len)