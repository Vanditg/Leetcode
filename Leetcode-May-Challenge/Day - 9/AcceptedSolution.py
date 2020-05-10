##==================================
## Leetcode May Challenge 
## Username: Vanditg
## Year: 2020
## Problem: 9
## Problem Name: Valid Perfect Square 
##===================================
#Given a positive integer num, write a function which returns True if num is a perfect square else False.
#
#Note: Do not use any built-in library function such as sqrt.
#
#Example 1:
#
#Input: 16
#Output: true
#Example 2:
#
#Input: 14
#Output: false
class Solution:
    def isPerfectSquare(self, num):
        product = 1	#Initialize product
        while True:	#Loop while
            if product*product == num:	#Condition-check: If product^2 is equal to number 
                return True	#We return true
            elif product*product > num:	#Condition-check: Elif product^2 is greater than number
                return False	#We return false
            product += 1	#Update the product