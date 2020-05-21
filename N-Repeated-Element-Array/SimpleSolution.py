##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 961
## Problem Name: N-Repeated Element in Size 2N Array  
##===================================
#In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.
#
#Return the element repeated N times.
#
#Example 1:
#
#Input: [1,2,3,3]
#Output: 3
#Example 2:
#
#Input: [2,1,2,5,3,2]
#Output: 2
#Example 3:
#
#Input: [5,1,5,2,5,3,5,4]
#Output: 5
from collections import Counter as c	#Import Counter module 
class Solution:
    def repeatedNTimes(self, A):
        tmp = c(A)	#Initialize tmp which count the occurance of number 
        return (''.join(str(key) for key, val in tmp.items() if val > 1))	#Return the key whose val is greater than 1 