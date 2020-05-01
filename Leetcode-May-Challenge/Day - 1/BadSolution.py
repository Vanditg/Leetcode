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
        for i in range(1, n+1, 1):	#Loop through 1 to n + 1 by step 1  
            if isBadVersion(i):	#Condition-check: If i is bad version
                return i	#We'll return that i which is the first bad version

#Explanation:
#The time complexity will be o(n). 
#For small inputs this will work, but for larger input such as n = 1857686865656 if the bad version is at 185268686565, this will impose time limit error as the algorithm is checking from 1 to 185268686565.  
#Thus in the case binary Search will be optimal to use, and has time complexity is o(log(n)). 