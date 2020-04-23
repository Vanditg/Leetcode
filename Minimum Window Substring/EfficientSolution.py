##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 76
## Problem Name: Minimum Window Substring      
##===================================
#
#Given a string S and a string T, 
#find the minimum window in S which will contain all the characters in T in complexity O(n).
#
#Example:
#
#Input: S = "ADOBECODEBANC", T = "ABC"
#Output: "BANC"
import collections 
class Solution:
    def minWindow(self, s, t):
        tmp = collections.Counter(t)	#Initilaize tmp dictionary > key = letter and value = count
        left, right, i, j, minStr = 0, 0, 0, 0, len(t)	#Initilaize left, right, i, j, and minStr
        while right < len(s):	#Loop while right is less than the length of string 
            if tmp[s[right]] > 0:	#Condition-check: If string's right value is greater than zero
                minStr -= 1	#Update minStr by decreasing 1
            tmp[s[right]] -= 1	#Update dictionary value for particular key by decreasing 1
            right += 1	#Update right by increasing 1 
            while minStr == 0:	#Loop while minStr is zero
                if j == 0 or right - left < j - i:	#Condition-check: If j is zero or right - left value is less than j - i value
                    i, j = left, right	#Update i, j by left, right
                tmp[s[left]] += 1	#Update dictionary value for particular key by increasing 1
                if tmp[s[left]] > 0:	#If dictionary value for particular key is greater than 0
                    minStr += 1	#Update minStr by increasing 1
                left += 1	#Update left by increasing 1
        return s[i:j]	#Finally return s from i to j index 				