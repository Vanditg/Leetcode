##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 387
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
from collections import Counter as c	#Import Counter 
class Solution:
    def firstUniqChar(self, s):
        tmp = c(s)	#Initialize tmp 
        tmpChar = [key for key, val in tmp.items() if val == 1]	#Initialize tmpChar which will strore the key's in which the value will be one for each character
	    if s == "":	#Condition-check: If string is empty
            return -1	#We'll return -1
        else:	#Condition-check: Else
            if tmpChar == []:	#Condition-check: if tmpChar is empty
                return -1	#We'll return -1 
            else:	#Condition-check: Else 
                return s.find(tmpChar[0])	#We'll return the index of the first tmpChar in string s 