##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 260
## Problem Name: Single Number III  
##===================================
#
#Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.
#
#Example:
#
#Input:  [1,2,1,3,2,5]
#Output: [3,5]
import collections as c	#Importing collections module 
class Solution:
    def singleNumber(self, nums):
        return [item for item, count in c.Counter(nums).items() if count == 1]	#Return the list containing excatly once element appearing in the array