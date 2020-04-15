##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 268
## Problem Name: Missing Number  
##===================================
#
#Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
#
#Example 1:
#
#Input: [3,0,1]
#Output: 2
#
#Example 2:
#
#Input: [9,6,4,2,3,5,7,0,1]
#Output: 8
class Solution:
    def missingNumber(self, nums):
        numsSum = sum(nums)	#Count the sum of numbers
        tmpSum = ((len(nums)) * (len(nums) + 1)) // 2	#Initialize tmpSum which stores the given equation int value
        return tmpSum - numsSum	#return tmpSum - numsSum