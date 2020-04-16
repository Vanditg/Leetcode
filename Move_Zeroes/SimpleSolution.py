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
        zero = nums.count(0)	#Count the number of zero in given array.
        for i in range(zero):
            nums.remove(0)	#This will remove zero.  
            nums.append(0)	#This will append zero at the end of list. 