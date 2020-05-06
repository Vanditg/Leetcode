##==================================
## Leetcode May Challenge 
## Username: Vanditg
## Year: 2020
## Problem: 6
## Problem Name: Majority Element   
##===================================
#
#Given an array of size n, find the majority element. 
#The majority element is the element that appears more than ⌊ n/2 ⌋ times.
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
from collections import Counter as c	#Import Counter 
class Solution: 
    def majorityElement(self, nums):
        tmp = c(nums)	#Initialize tmp and count the numbers occurence 
        tmpListVal = [val for key, val in tmp.items()]	#Initialize tmpListVal, which will be list of all the values from different keys 
        tmpList = "".join([str(key) for key, val in tmp.items() if val == max(tmpListVal)])	#Initialize tmpList which will be the str of the key whose value is majority in tmpListVal
        return int(tmpList)	#Return int of tmpList which is majority element
#Example:
#nums = [3, 2, 3]
#tmp = {'3':2, '2':1}
#tmpListVal = [2, 1]
#tmpList = '3'
#return 3