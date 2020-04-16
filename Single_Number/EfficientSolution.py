##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 268
## Problem Name: Single Number  
##===================================
#
#Given a non-empty array of integers, every element appears twice except for one. Find that single one.
#
#Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
#
#Example 1:
#
#Input: [2,2,1]
#Output: 1
#
#Example 2:
#
#Input: [4,1,2,1,2]
#Output: 4
class Solution:
    def singleNumber(self, nums):
        number =  0	#Initilaize number 
        for i in nums:	#Loop through number 
            number ^= i	#using XOR between two number - number and i
        return number	#Return number at the end. 