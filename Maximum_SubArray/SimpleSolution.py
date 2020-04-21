##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 49
## Problem Name: Group Anagrams    
##===================================
#Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
#
#Example:
#
#Input: [-2,1,-3,4,-1,2,1,-5,4],
#Output: 6
#Explanation: [4,-1,2,1] has the largest sum = 6.
class Solution:
    def maxSubArray(self, nums):
        sum = max_sum = nums[0]	#Initialize sum and max_sum equals to 0th index value from nums 
        for i in nums[1:]:	#Loop through nums start index from 1 
            sum = max(i, sum + i)	#Update sum by finding max of i and sum + i. 
            max_sum = max(max_sum, sum)	#Update max_sum by finding max of max_sum and sum 
        return max_sum	#We'll return max_sum at the end. 