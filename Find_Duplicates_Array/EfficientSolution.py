##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 442
## Problem Name: Find All Duplicates in an Array  
##===================================
#
#Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
#
#Find all the elements that appear twice in this array.
#
#Could you do it without extra space and in O(n) runtime?
#
#Example:
#Input:
#[4,3,2,7,8,2,3,1]
#
#Output:
#[2,3]
import collections	#Importing collections module 
class Solution:
    def findDuplicates(self, nums):
        return ([item for item, count in collections.Counter(nums).items() if count > 1])	#Returning elements list appearing more than one time.  