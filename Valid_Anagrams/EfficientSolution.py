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
from collections import Counter as c	#Importing Counter module 
class Solution:
    def isAnagram(self, s, t): 
        return c(s) == c(t) #Return True if the condition satisfied otherwise false 

#Linewise Example:
#s = 'rat'
#t = 'car'
#c(s) = {'a':1, 'r':1, 't':1}
#c(t) = {'a':1, 'c':1, 't':1}
#False 