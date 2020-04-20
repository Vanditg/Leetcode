##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 137
## Problem Name: Single Number II   
##===================================
#Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.
#
#Note:
#
#Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
#
#Example 1:
#
#Input: [2,2,3,2]
#Output: 3
#
#Example 2:
#
#Input: [0,1,0,1,0,1,99]
#Output: 99
import collections as c	#Importing collections module 
class Solution:
    def singleNumber(self, nums):
        return "".join(map(str, [item for item, count in c.Counter(nums) if count == 1]))	#Returning element that appears exactly one times. 