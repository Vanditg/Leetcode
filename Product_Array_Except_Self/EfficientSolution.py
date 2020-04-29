##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 230
## Problem Name: Kth Smallest Element in a BST    
##===================================
#
#Given an array nums of n integers where n > 1,  
#return an array output such that output[i] is equal to
#the product of all the elements of nums except nums[i].
#
#Example:
#
#Input:  [1,2,3,4]
#Output: [24,12,8,6]
#Constraint: It's guaranteed that the product of the elements of 
#any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.
class Solution: 
    def productExceptSelf(self, nums):
        l = [1]*len(nums)	#Initialize l list which contains 1, total of len(nums)
        r = [1]*len(nums)	#Initialize r list which contains r, total of len(nums)
        for i in range(1, len(nums)):	#Loop through nums 
            l[i] = l[i-1]*nums[i-1]	#Update l[i] by multiplying previous values from l and nums 
        for j in range(len(nums) - 2, -1, -1):	#Loop through nums in reverse order 
            r[j] = r[j+1]*nums[j+1]	#Update r[j] by multiplying previous values from r and nums 
        for k in range(len(l)):	#Loop through left 
            l[k] = l[k]*r[k]	#Update l by multiplying l and r's index's values 
        return l	#Return modified l 