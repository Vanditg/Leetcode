##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 415
## Problem Name: Add Strings           
##===================================
#
#Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
#
#Note:
#
#The length of both num1 and num2 is < 5100.
#Both num1 and num2 contains only digits 0-9.
#Both num1 and num2 does not contain any leading zero.
#You must not use any built-in BigInteger library or convert the inputs to integer directly.
class Solution:
    def addStrings(self, num1, num2):
        tmp = int(num1) + int(num2)	#Initialize tmp and convert the numbers to int
        return str(tmp)	#We return str of tmp 