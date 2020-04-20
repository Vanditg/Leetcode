##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 628
## Problem Name: Maximum Product of Three Numbers  
##===================================
#
#Given an integer array, find three numbers whose product is maximum and output the maximum product.
#
#Example 1:
#
#Input: [1,2,3]
#Output: 6
#
#Example 2:
#
#Input: [1,2,3,4]
#Output: 24
class Solution:
    def maximumProduct(self, nums):
        if len(nums) == 3:	#Condition-check: If nums length is equal to three. 
            return nums[0]*nums[1]*nums[2]	#We return the muliplication of their value. 
        else:	#Condition-check: Otherwise 
            nums.sort()	#We sort the array.
            if nums[0] >= 0 or nums[-1] <= 0:	#Condition-check: If sorted array has all positive numbers or negative numbers
               return nums[-1]*nums[-2]*nums[-3]	#We multiply nums last three numbers to get max 
            return max(nums[-1]*nums[-2]*nums[-3], nums[-1]*nums[0]*nums[1])	#Otherwise, we return max of given numbers 