##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 1323
## Problem Name: Maximum 69 Number
##===================================
#
#Given a positive integer num consisting only of digits 6 and 9.
#
#Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).
#
#Example 1:
#
#Input: num = 9669
#Output: 9969
#Explanation: 
#Changing the first digit results in 6669.
#Changing the second digit results in 9969.
#Changing the third digit results in 9699.
#Changing the fourth digit results in 9666. 
#The maximum number is 9969.
#
#Example 2:
#
#Input: num = 9996
#Output: 9999
#Explanation: Changing the last digit 6 to 9 results in the maximum number.

#Example 3:
#
#Input: num = 9999
#Output: 9999
#Explanation: It is better not to apply any change.
class Solution:
    def maximum69Number(self, number):
        tmpNumber = [int(j) for j in str(number)]    #Converting number to list
        count = 0    #Initialize counter
        for i in range(len(tmpNumber))    #loop through the list
            if tmpNumber[i] == 6:    #Condition-check: If tmpNumber[i] == 6 then we enter the if condition
                tmpNumber[i] = 9    #We'll replace that integer with '9'
                count += 1    #Increase our count by 1.
                if count == 1:   #Condition-check: If count == 1 then we enter the if condition
                    finalNumber = int("".join(map(str, tmpNumber)))    #We'll map our list to int number - finalNumber
                    break    #We'll break then.
            else:    #Condition-check: if tmpNumber[i] != 6 then we enter the else condition
                finalNumber = int("".join(map(str, tmpNumber)))    #We'll map our list to int number - finalNumber
        return finalNumber   #We'll return finalNumber

#Example
#Number = 9669
#tmpNumber = [9, 6, 6, 9]
#count = 0
#i = 0 
#Condition-check for if - it fails 
#finalNumber = 9
#i = 1
#Condition-check for if - it passed
#tmpNumber[1] = 9
#count = 1
#Condition-check for if - it passed
#finalNumber = 99
#i = 2 
#Condition-check for if - it fails 
#finalNumber = 996
#i = 3
#Condition-check for if - it fails 
#finalNumber = 9969