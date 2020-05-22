##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 263
## Problem Name: Ugly Number   
##===================================
#
#Write a program to check whether a given number is an ugly number.
#
#Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
#
#Example 1:
#
#Input: 6
#Output: true
#Explanation: 6 = 2 × 3
#Example 2:
#
#Input: 8
#Output: true
#Explanation: 8 = 2 × 2 × 2
#Example 3:
#
#Input: 14
#Output: false 
#Explanation: 14 is not ugly since it includes another prime factor 7.
class Solution:
    def isUgly(self, num):
        if num == 0:	#Condition-check: If num is zero 
            return False	#We return false 
        for i in [2, 3, 5]:	#Loop through 2, 3, 5     
            while num % i == 0:	#Loop till condition met 
                num /= i	#Update number by dividing by i 
        return num == 1	#Return true or false if the number will be 1 