##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 217
## Problem Name: Contains Duplicate  
##===================================
#
#Given an array of integers, find if the array contains any duplicates.
#
#Your function should return true if any value appears at least twice in the array, 
#and it should return false if every element is distinct.
#
#Example 1:
#
#Input: [1,2,3,1]
#Output: true
#Example 2:
#
#Input: [1,2,3,4]
#Output: false
#Example 3:
#
#Input: [1,1,1,3,3,4,3,2,4,2]
#Output: true
class Solution:
    def containsDuplicate(self, nums):
        return [i for i, count in collections.Counter(nums).items() if count != 1]	#If the value is not 1 in count value than it will be true otherwise false 