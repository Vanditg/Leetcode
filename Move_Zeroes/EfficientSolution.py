##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 283
## Problem Name:  Move Zeroes      
##===================================
#Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#
#Example:
#
#Input: [0,1,0,3,12]
#Output: [1,3,12,0,0]
class Solution:
    def moveZeroes(self, nums):
        index = 0	#Initialize index 
        for i in range(len(nums)):	#Loop through nums 
            if nums[i] != 0:	#Condition-check: if nums[i] is not equal to zero.
                nums[index], nums[i] = nums[i], nums[index]	#Swap the values so that zero will go at the end of list. 
                index += 1	#Increase index by one 