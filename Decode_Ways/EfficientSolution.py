##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 91
## Problem Name: Decode Ways   
##===================================
#
#A message containing letters from A-Z is being encoded to numbers using the following mapping:
#
#'A' -> 1
#'B' -> 2
#...
#'Z' -> 26
#Given a non-empty string containing only digits, determine the total number of ways to decode it.
#
#Example 1:
#
#Input: "12"
#Output: 2
#Explanation: It could be decoded as "AB" (1 2) or "L" (12).
#
#Example 2:
#
#Input: "226"
#Output: 3
#Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
class Solution:
    def numDecodings(self, s): 
        if len(s) == 0 or s[0] == '0':	#Condition-check: If str is empty or 1st digit is zero
            return 0	#We return zero
        tmpA, tmpB = 1, 0	#Initialize tmpA, tmpB counter 
        for i in range(len(s)):	#Loop through string 
            tmp = 0	#Initialize final counter tmp
            if s[i] != '0':	#Condition-check: If str's 1st digit is not zero
                tmp = tmpA	#Update tmp by assigining tmpA
            if i > 0 and (s[i - 1] == '1' or (s[i - 1] == '2' and s[i] <= '6')):	#Condition-check: If i is greater than zero and previous digit is one or previous and current digit is between 2 and 6
                tmp += tmpB	#Update tmp  by adding tmpB into it 
            tmpA, tmpB = tmp, tmpA	#Update tmpA, and tmpB by assigining tmp and tmpA
        return tmpA	#Return tmpA