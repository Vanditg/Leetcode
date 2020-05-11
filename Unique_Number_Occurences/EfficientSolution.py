##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 1207
## Problem Name:  Unique Number of Occurrences 
##===================================
#
#Given an array of integers arr, write a function that returns true 
#if and only if the number of occurrences of each value in the array is unique.
#
#Example 1:
#
#Input: arr = [1,2,2,1,1,3]
#Output: true
#Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
#Example 2:
#
#Input: arr = [1,2]
#Output: false
#Example 3:
#
#Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
#Output: true
from collections import Counter as c	#Import Counter module 
class Solution:
    def uniqueOccurences(self, arr):
        tmp = c(arr)	#Initialize tmp which count the occurrences 
        tmpVal = []	#Initialize tmpVal empty list
        for key, val in tmp.items():	#Loop through dictionary 
            tmpVal.append(val)	#Append the val in tmpVal list 
        count = c(tmpVal)	#Initialize count which count the occurrences of values
        for key, val in count.items():	#Loop through dictionary
            if val != 1:	#Condition-check: If val is not equal to 1 such that any value occurrence twice or more than that 
                return False	#We return false 
        return True	#Return true otherwise 