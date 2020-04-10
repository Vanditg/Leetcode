##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 709
## Problem Name: To Lower Case
##===================================
#
#Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.
#
#Example 1:
#
#Input: "Hello"
#Output: "hello"
#
#Example 2:
#
#Input: "here"
#Output: "here"
#
#Example 3:
#
#Input: "LOVELY"
#Output: "lovely"
class Solution:
    def toLowerCase(self, str):
        return str.lower() #Using string in-built method - lower() in python 