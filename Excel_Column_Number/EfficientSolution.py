##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 171
## Problem Name: Excel Sheet Column Number        
##===================================
#
#Given a column title as appear in an Excel sheet, return its corresponding column number.
#
#For example:
#
#    A -> 1
#    B -> 2
#    C -> 3
#    ...
#    Z -> 26
#    AA -> 27
#    AB -> 28 
#    ...
#Example 1:
#
#Input: "A"
#Output: 1
#Example 2:
#
#Input: "AB"
#Output: 28
#Example 3:
#
#Input: "ZY"
#Output: 701
class Solution:
    def titleToNumber(self, s): 
        tmp = 0	#Initialize tmp
        for i in range(len(s)):	#Loop through string 
            tmp *= 26	#Update tmp by multiplying with 26(A to Z)
            tmp += ord(s[i]) - ord('A') + 1	#Update tmp by finding unicode value for given s[i] and subtact from A and add 1
        return tmp	#Return tmp 