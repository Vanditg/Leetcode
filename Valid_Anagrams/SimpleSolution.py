##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 242
## Problem Name: Valid Anagram     
##===================================
#
#Given two strings s and t , write a function to determine if t is an anagram of s.
#
#Example 1:
#
#Input: s = "anagram", t = "nagaram"
#Output: true
#Example 2:
#
#Input: s = "rat", t = "car"
#Output: false
class Solution:
    def isAnagram(self, s, t): 
        return sorted(s) == sorted(t)	#Return True if the condition satisfied otherwise false 

#Linewise Example
#s = 'rat'
#t = 'cat'
#sorted(s) = [a, r, t]
#sorted(t) = [a, c, t]
#Return False as both are different 