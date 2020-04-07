##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 1342
## Problem Name: Number of Steps to Reduce a Number to Zero
##===================================
#Given a non-negative integer num, return the number of steps to reduce it to zero. 
#
#If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.
#Example 1:
#
#Input: num = 14
#Output: 6
#Explanation: 
#Step 1) 14 is even; divide by 2 and obtain 7. 
#Step 2) 7 is odd; subtract 1 and obtain 6.
#Step 3) 6 is even; divide by 2 and obtain 3. 
#Step 4) 3 is odd; subtract 1 and obtain 2. 
#Step 5) 2 is even; divide by 2 and obtain 1. 
#Step 6) 1 is odd; subtract 1 and obtain 0.
#
#Example 2:
#
#Input: num = 8
#Output: 4
#Explanation: 
#Step 1) 8 is even; divide by 2 and obtain 4. 
#Step 2) 4 is even; divide by 2 and obtain 2. 
#Step 3) 2 is even; divide by 2 and obtain 1. 
#Step 4) 1 is odd; subtract 1 and obtain 0.
#
#Example 3:
#
#Input: num = 123
#Output: 12
#
#The solution for this problem is fairly starightforward by following the problem statement. 

class Solution:

    def numberOfSteps (self, number):

        step = 0  #Initialize our step counter. 

        while number != 0:   #While the number is not zero (Following the condition of non-negative integer)

            if number % 2 == 0:   #Condition Check - If number is divided by zero and gives no remainder

                number = number // 2    #We'll divide the number by 2 again. Here (//) will give you integer as in 2.0, 3.0 etc. In python (/) will give you floating numbers.

            else:    #If condition fails then

                number = number - 1   #We'll subtract the number by 1. 

            step = step + 1      #Corresponding, we'll update our step counter. 

        return step     #We'll return the step number at the end. 
		
#For example: number = 3
# 3 % 2 = 1 (If condition failed.)
# 3 - 1 = 2 (Enters the else condition.) [step = 1]
# Now number = 2. 
# 2 % 2 = 0 (If condition pass.)
# 2 // 2 = 1.0 (Enters the if condition.) [step = 2]
# number = 1.0
# 1 % 2 = -1 (if condition failed.)
# 1 - 1 = 0 (Enters the else condition.) (Goal state reached.) [step = 3] 
# Total number of step = 3.