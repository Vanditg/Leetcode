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
        num = {}	#Initialize num dictionary
        for i in nums:	#Loop through nums
            num[i] = 1	#Assign key-values to static 1 
        for i in range(len(nums) + 1): 	#Loop through len(nums) + 1
            if i not in d:	#Condition-check: if i is not in dictionary
                return i	#We'll return i. 