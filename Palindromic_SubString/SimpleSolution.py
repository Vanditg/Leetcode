##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 647
## Problem Name: Palindromic Substrings       
##===================================
#
#Given a string, your task is to count how many palindromic substrings in this string.
#
#The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.
#
#Example 1:
#
#Input: "abc"
#Output: 3
#Explanation: Three palindromic strings: "a", "b", "c".
#
#Example 2:
#
#Input: "aaa"
#Output: 6
#Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
class Solution:
    def countSubstrings(self, s): 
        tmp = 0	#Initialize tmp
        for i in range(2*len(s) + 1):	#Loop through string with given range
            l = r = i // 2	#Initialize left and right which is i // 2 int value 
            if i % 2 == 1:	#Condition-check:	If i is not even 
                r += 1	#Update r by increasing 1
            while l >= 0 and r < len(s) and s[l] == s[r]:	#Loop till the condition met
                tmp += 1	#Update tmp by increasing 1
                l -= 1	#Update l by decreasing 1
                r += 1	#Update r by increasing 1
        return tmp	#We return tmp which is count