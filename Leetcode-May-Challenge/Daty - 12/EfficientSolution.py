##==================================
## Leetcode May Challenge 
## Username: Vanditg
## Year: 2020
## Problem: 12
## Problem Name:  Single Element in a Sorted Array
##===================================
#
#You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.
#
#Example 1:
#
#Input: [1,1,2,3,3,4,4,8,8]
#Output: 2
#Example 2:
#
#Input: [3,3,7,7,10,11,11]
#Output: 10
# 
#Note: Your solution should run in O(log n) time and O(1) space.
from collections import Counter as c	#Import Counter module 
class Solution:
    def singleNonDuplicate(self, nums):	
        return ''.join([str(i) for i, j in c(nums).items() if j == 1])	#Return str(i) where i's occurence is only one-time 