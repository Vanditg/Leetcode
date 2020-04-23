##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 70
## Problem Name: Climbing Stairs     
##===================================
#You are climbing a stair case. It takes n steps to reach to the top.
#
#Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#
#Note: Given n will be a positive integer.
#
#Example 1:
#
#Input: 2
#Output: 2
#Explanation: There are two ways to climb to the top.
#1. 1 step + 1 step
#2. 2 steps
#Example 2:
#
#Input: 3
#Output: 3
#Explanation: There are three ways to climb to the top.
#1. 1 step + 1 step + 1 step
#2. 1 step + 2 steps
#3. 2 steps + 1 step
class  Solution: 
    def climbStairs(self, n):
        if n == 1:	#Condition-check: If n is 1 
            return 1 	#We returns 1 step
        if n == 2:	#Condition-check: If n is 2 
            return 2	#We returns 2 step
        tmpA = 1	#Initialize tmpA  
        tmpB = 2	#Initialize tmpB
		for i in range(3, n + 1):	#Loop through 3 to n+1
            tmp = tmpA + tmpB	#Initialize tmp and update it 
            tmpA, tmpB = tmpB, tmpA	#Update tmpA and tmpB
        return tmpB	#Return tmpB at the end. 