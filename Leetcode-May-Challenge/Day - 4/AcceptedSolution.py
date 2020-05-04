##==================================
## Leetcode May Challenge 
## Username: Vanditg
## Year: 2020
## Problem: 4
## Problem Name: Number Complement
##===================================
#
#Given a positive integer, output its complement number. 
#The complement strategy is to flip the bits of its binary representation.
#
#Example 1:
#
#Input: 5
#Output: 2
#Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. 
#So you need to output 2.
# 
#Example 2:
#
#Input: 1
#Output: 0
#Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. 
#So you need to output 0.
class Solution:
    def findComplement(self, nums):
        tmp = nums	#Initialize tmp to nums 
        bit = 1	#Initialize bit to 1  		
        while tmp:	#Loop 
            num = num ^ bit	#Update num by taking XOR of num and bit 
            bit = bit << 1	#Taking left shift by 1 for bit 
            tmp = tmp >> 1	#taking right shift by 1 for tmp
        return num	#We'll return our number 