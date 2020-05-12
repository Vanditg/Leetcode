##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 66
## Problem Name: Plus One 
##===================================
#
#Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
#
#The digits are stored such that the most significant digit is at the head of the list, 
#and each element in the array contain a single digit.
#
#You may assume the integer does not contain any leading zero, except the number 0 itself.
#
#Example 1:
#
#Input: [1,2,3]
#Output: [1,2,4]
#Explanation: The array represents the integer 123.
#Example 2:
#
#Input: [4,3,2,1]
#Output: [4,3,2,2]
#Explanation: The array represents the integer 4321.
class Solution:
    def plusOne(self, digits):
        tmpList = [str(i) for i in digits]	#Initialize tmpList and converting number to string 
        tmp = int(''.join(tmpList))	#Initialize tmp and join the list and converting back to int 
        tmp += 1	#Update tmp by adding 1 
        return [int(i) for i in str(tmp)]	#Return a list of numbers gained from tmp		