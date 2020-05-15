##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 1287
## Problem Name: Element Appearing More Than 25% In Sorted Array
##===================================
#
#Given an integer array sorted in non-decreasing order, 
#there is exactly one integer in the array that occurs more than 25% of the time.
#
#Return that integer.
#
#Example 1:
#
#Input: arr = [1,2,2,6,6,6,6,7,10]
#Output: 6
from collections import Counter as c 
class Solution:
    def finaSpecialInteger(self, arr):
        tmp = c(arr)	#Initialize tmp and count the occurance of numbers 
        return (''.join([str(key) for key, val in tmp.items() if val/len(arr) > 1/4]))	#Return the number whose occurance is more tha 25% times