##==================================
## Leetcode May Challenge 
## Username: Vanditg
## Year: 2020
## Problem: 5
## Problem Name: First Unique Character in a String    
##===================================
#
#Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
#
#Examples:
#
#s = "leetcode"
#return 0.
#
#s = "loveleetcode",
#return 2.
#Note: You may assume the string contain only lowercase letters.
from collections import Counter as c	#Import Counter module 
class Solution:
    def firstUniqChar(self, s):
        tmp = c(s)	#Initialize tmp and use counter to count the char and values 
        tmpChar = [key for key, val in tmp.items() if val == 1]	#Initialize tmpChar list and store the char whose occurence is only one time 
        if s == "":	#Condition-check: If s is empty string 
            return -1	#Return -1
        else:	#Condition-check: Else
            if tmpChar == []:	#Condition-check: If tmpChar is empty
                return -1	#Return -1
            else:	#Condition-check: Else
                return s.find(tmpChar[0])	#Find the index of first character of tmpChar in string and return it  