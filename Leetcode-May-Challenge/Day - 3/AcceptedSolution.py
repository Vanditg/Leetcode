##==================================
## Leetcode May Challenge 
## Username: Vanditg
## Year: 2020
## Problem: 3
## Problem Name: Ransom Note
##===================================
#
#Given an arbitrary ransom note string and another string containing letters from all the magazines, 
#write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.
#
#Each letter in the magazine string can only be used once in your ransom note.
#
#Note:
#You may assume that both strings contain only lowercase letters.
#
#canConstruct("a", "b") -> false
#canConstruct("aa", "ab") -> false
#canConstruct("aa", "aab") -> true
from collections import Counter as c	#Importing Counter module 
class Solution:
    def canConstruct(self, ransomNote, magazine):
        return not c(ransomNote) - c(magazine)	#Return True if ransom note constructed from magazine otherwise false