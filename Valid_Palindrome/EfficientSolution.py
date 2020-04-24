##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 125
## Problem Name: Valid Palindrome
##===================================
#
#Given a string, determine if it is a palindrome, 
#considering only alphanumeric characters and ignoring cases.
#
#Note: For the purpose of this problem, we define empty string as valid palindrome.
#
#Example 1:
#
#Input: "A man, a plan, a canal: Panama"
#Output: true
#Example 2:
#
#Input: "race a car"
#Output: false
class Solution:
    def isPalindrome(self, s):
        s = ''.join(i for i in s if i.isalnum().lower)	#Initialize s where we join every word in one string and check for alphanumeric cases 
        return s == s[::-1]	#Return true or false if our main s and reverse of s is same or not respectively