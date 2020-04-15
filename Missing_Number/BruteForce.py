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
        list = []	#Initialize empty list
        for i in range(1, len(nums) + 1):	#Loop through nums 
            list.append(i)	#Append the value to our empty list.
        result = 0	#Initialize result which we'll return 
        for i in range(len(nums)):	#Loop through nums
            if list[i] not in nums:	#Condition-check: If list element is not in the nums list, then		
                result = list[i]	#The result will be that element
        return result	#We'll return result 