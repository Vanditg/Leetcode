##==================================
## Leetcode May Challenge 
## Username: Vanditg
## Year: 2020
## Problem: 1
## Problem Name: First Bad Version       
##===================================
#
#You are a product manager and currently leading a team to develop a new product. 
#Unfortunately, the latest version of your product fails the quality check. 
#Since each version is developed based on the previous version, all the versions after a bad version are also bad.
#
#Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, 
#which causes all the following ones to be bad.
#
#You are given an API bool isBadVersion(version) which will return whether version is bad. 
#Implement a function to find the first bad version. You should minimize the number of calls to the API.
#
#Example:
#
#Given n = 5, and version = 4 is the first bad version.
#
#call isBadVersion(3) -> false
#call isBadVersion(5) -> true
#call isBadVersion(4) -> true
#
#Then 4 is the first bad version. 

class Solution:
    def firstBadVersion(self, n):
        first = 0	#Initialize first
        while first < n:	#Loop till the condition met
            middle = (first + n) // 2	#Initialize middle which is int from sum of first + n // 2
            if isBadVersion(middle):	#Condition-check:If middle is bad version
                n = middle	#We'll update n to middle int
            else:	#Condition-check: Else
                first = middle + 1	#We'll update first to middle + 1
        return first	#We'll return first, which will be first bad version
		