##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 287
## Problem Name: Find the Duplicate Number          
##===================================
#
#Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), 
#prove that at least one duplicate number must exist. Assume that there is only one duplicate number, 
#find the duplicate one.
#
#Example 1:
#
#Input: [1,3,4,2,2]
#Output: 2
#Example 2:
#
#Input: [3,1,3,4,2]
#Output: 3
class Solution:
    def findDuplicate(self, nums):
        return "".join([str(key) for key, val in collections.Counter(nums).items() if val != 1])	#Return the duplicate number 