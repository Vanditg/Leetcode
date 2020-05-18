##==================================
## Leetcode May Challenge 
## Username: Vanditg
## Year: 2020
## Problem: 18
## Problem Name: Permutation in String
##===================================
#
#Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. 
#In other words, one of the first string's permutations is the substring of the second string.
#
#Example 1:
#
#Input: s1 = "ab" s2 = "eidbaooo"
#Output: True
#Explanation: s2 contains one permutation of s1 ("ba").
#Example 2:
#
#Input:s1= "ab" s2 = "eidboaoo"
#Output: False
from collections import Counter as c	#Import Counter module 
class Solution:
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):	#Condition-check: If s1 is bigger than s2
            return False	#We return false
        lenS1, countS1, windowCount = len(s1), c(s1), c()	#Initialize lenS1, countS1, and windowCount
        for i, count in enumerate(s2):	#Loop through s2 
            windowCount[count] += 1	#Update windowCount set the count key and update the value of the count 
            if i >= lenS1:	#Condition-check: If i is greater or equal to lenS1
                left = s2[i - lenS1]	#Initialize left 
                if windowCount[left] == 1:	#Condition-check: If windowCount of left key is equal to 1 
                    del windowCount[left]	#We remove the windowCount of left key 
                else:	#Condition-check: Else
                    windowCount[left] -= 1	#Update windowCount of left key by decreasing 1 
            if windowCount == countS1:	#Condition-check: If windowCount and countS1 is same 
                return True	#We return True  
        return False	#We return False 