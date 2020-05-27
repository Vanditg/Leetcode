##==================================
## Leetcode May Challenge 
## Username: Vanditg
## Year: 2020
## Problem: 26
## Problem Name: Contiguous Array
##===================================
#
#Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.
#
#Example 1:
#Input: [0,1]
#Output: 2
#Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
#
#Example 2:
#Input: [0,1,0]
#Output: 2
#Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
class Solution:
    def findMaxLength(self, nums):
        res, count = 0, 0	#Initialize res and count 
        tmp = {}	#Initialize dictionary 
        for i in range(len(nums)):	#Loop through nums 
            if nums[i] == 1:	#Condition-check: If number is 1 
                count += 1	#Update the count 
            else:	#Condition-check: Else
                count -= 1	#Decrease the count
            if count == 0:	#Condition-check: If count is zero  
                res = i + 1	#Update the res 
            if count in tmp:	#Condition-check: If count is in the tmp dictionary
                res = max(res, i - tmp[count])	#Then we take the max between res and i - tmp[dictionary]
            else:	#Condition-check: Else
                tmp[count] = i	#Update the dictionary
        return res	#We return res 