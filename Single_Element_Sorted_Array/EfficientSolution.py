##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 540
## Problem Name: Single Element in a Sorted Array  
##===================================
#
#You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.
#
#Example 1:
#
#Input: [1,1,2,3,3,4,4,8,8]
#Output: 2
#
#Example 2:
#
#Input: [3,3,7,7,10,11,11]
#Output: 10
import collections as c	#Importing collections module 
class Solution:
    def singleNonDuplicate(self, nums):
        return ("".join(map(str, [item for item, count in c.Counter(nums).items() if count == 1])))	#Returning the element appears exactly once in an array.