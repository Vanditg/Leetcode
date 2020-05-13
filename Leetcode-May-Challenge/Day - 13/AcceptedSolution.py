##==================================
## Leetcode May Challenge 
## Username: Vanditg
## Year: 2020
## Problem: 13
## Problem Name: Remove K Digits
##===================================
#
#Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.
#
#Note:
#The length of num is less than 10002 and will be ≥ k.
#The given num does not contain any leading zero.
#Example 1:
#
#Input: num = "1432219", k = 3
#Output: "1219"
#Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
#Example 2:
#
#Input: num = "10200", k = 1
#Output: "200"
#Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
#Example 3:
#
#Input: num = "10", k = 2
#Output: "0"
#Explanation: Remove all the digits from the number and it is left with nothing which is 0.
class Solution:
    def removeKDigits(self, num, k):
        tmp = []	#Initialise tmp stack  
        nRemove = k	#Initialise nRemove which is number to remove
        for curr in num:	#Loop through num 
            while nRemove and tmp and tmp[-1] > curr:	#Loop 
                tmp.pop()	#Pop out the last element in tmp stack 
                nRemove -= 1	#Update the nRemove by decreasing 1 
            tmp.append(curr)	#Append the curr element in tmp stack 
        out = ''.join(tmp[0:len(num)-k]).lstrip('0')	#Initialise out which strips the 0 
        if len(out):	#Condition-check: If len(out) is not empty 
            return out 	#Return out 
        else:	#Condition-check: Else
            return '0'	#Return 0 string 