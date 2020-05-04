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
        tmp = bin(nums)	#Initialize tmp and set to binary of nums 
        result = "".join(['0' if i == '1' else '1' for i in tmp[2:]])	#Initialize result and set 0 to 1 and 1 to 0
        return int(result, 2)	#Return decimal representation of the result 