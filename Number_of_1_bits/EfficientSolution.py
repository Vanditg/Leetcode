##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 191
## Problem Name: Number of 1 Bits           
##===================================
#
#Write a function that takes an unsigned integer and return the number of '1' bits it has 
#(also known as the Hamming weight).
#
#Example 1:
#
#Input: 00000000000000000000000000001011
#Output: 3
#Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
#Example 2:
#
#Input: 00000000000000000000000010000000
#Output: 1
#Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.
#Example 3:
#
#Input: 11111111111111111111111111111101
#Output: 31
#Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.
from collections import Counter as c	#Import Counter module 
class Solution:
    def hammingWeight(self, n): 
        tmp = "{:032b}".format(n)	#Initialize tmp and find binary representation
        tmpCount = c(tmp)	#Initialize tmpCount and use Counter for tmp
        for key, val in tmpCount.items():	#Loop through tmpCount
            if key == '1':	#Condition-check: If we find '1' bit 
                return val	#Return value for key == '1'
        return 0	#Otherwise return 0
   