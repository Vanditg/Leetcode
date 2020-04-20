##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 3
## Problem Name: Longest Substring Without Repeating Characters    
##===================================
#
#Given a string, find the length of the longest substring without repeating characters.
#
#Example 1:
#
#Input: "abcabcbb"
#Output: 3 
#Explanation: The answer is "abc", with the length of 3. 
#
#Example 2:
#
#Input: "bbbbb"
#Output: 1
#Explanation: The answer is "b", with the length of 1.
#
#Example 3:
#
#Input: "pwwkew"
#Output: 3
#Explanation: The answer is "wke", with the length of 3. 
#             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
class Solution:
    def lengthOfLongestSubstring(self, s): 
        if len(s) == 0:	#Condition-check: If length of string s is zero
            return 0	#We'll return zero. 
        tmp = dict()	#Initialize tmp dictionary.
		length = i = 0	#Initialize length and i to zero. 
        for j in range(len(s)):	#Loop through string 
            if s[j] in tmp and i <= tmp[s[j]]:	#Condition-check: If character is in dictionary and i's value is less than or equal to tmp[s[j]]
                i = tmp[s[j]] + 1	#Update i by adding tmp[s[j]] + 1 
            else:	#Condition-check: Else
                length = max(length, j - i + 1)	#Update length value by taking max of these two given values 
            tmp[s[j]] = j	#Update dictionary by adding j character
        return length	#Return length at the end. 