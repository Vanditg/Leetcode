##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 169
## Problem Name: Majority Element        
##===================================
#
#Given an array of size n, find the majority element. 
#The majority element is the element that appears more than n/2 times.
#
#You may assume that the array is non-empty and the majority element always exist in the array.
#
#Example 1:
#
#Input: [3,2,3]
#Output: 3
#Example 2:
#
#Input: [2,2,1,1,1,2,2]
#Output: 2
from collections import Counter as c	#Import Counter module
class Solution:
    def majorityElement(self, nums):
        tmp = c(nums)	#Initialize tmp which counts the number of elements and store in dictionary number : occurrence manner
        for key, val in tmp.items():	#Loop through tmp 
            if val > (len(nums) / 2):	#Condition-check: If value is greater than length of array / 2 
                return key	#We return key for that value 
#Example:
#nums = [3, 2, 3]
#tmp = Counter({3:2, 2:1})
#key, val = (3, 2)
#key, val = (2, 1)
#Condition-check: 2 > (3 / 2): return key Here value is 2, and for that value key is 3, so we'll return 3 which is majority element