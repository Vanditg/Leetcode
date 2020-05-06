##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 202
## Problem Name: Happy Number           
##===================================
#
#Write an algorithm to determine if a number n is "happy".
#
#A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.
#
#Return True if n is a happy number, and False if not.
#
#Example: 
#
#Input: 19
#Output: true
#Explanation: 
#12 + 92 = 82
#82 + 22 = 68
#62 + 82 = 100
#12 + 02 + 02 = 1
class Solution: 
    def isHappy(self, n):
        tmp = dict()	#Initialize tmp dictionary
        while n != 1 and n not in tmp:	#Loop till condition met
            tmp[n] = True	#We'll add the number and its digits sqaure and set to True 
            def next(n):	#Define helper method - next
                newNum = 0	#Initialize newNum 
                for i in str(n):	#Loop through n
                    newNum += int(i)**2	#Preform digits sqaure and update the newNum
                return newNum	#Return newNum 
            n = next(n)	#Update the n by using helper method 
        return n == 1	#Return true or false based on the next method's output 