##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 1295
## Problem Name: Find Numbers with Even Number of Digits
##===================================
#
#Given an array nums of integers, return how many of them contain an even number of digits.
#
#Example 1:
#
#Input: nums = [12,345,2,6,7896]
#Output: 2
#Explanation: 
#12 contains 2 digits (even number of digits). 
#345 contains 3 digits (odd number of digits). 
#2 contains 1 digit (odd number of digits). 
#6 contains 1 digit (odd number of digits). 
#7896 contains 4 digits (even number of digits). 
#Therefore only 12 and 7896 contain an even number of digits.
#
#Example 2:
#
#Input: nums = [555,901,482,1771]
#Output: 1 
#Explanation: 
#Only 1771 contains an even number of digits.
class Solution:
    def findNumbers(self, array):
        count = 0    #Intialize count 
        for i in range(len(array)):    #Loop through array
            #print(array[i])
            splitArrayDigit = [int(j) for j in str(array[i])]    #Split the array's number into each digit.
            #print(splitArrayDigit)
            if len(splitArrayDigit) % 2 == 0:     #Condition-check: If array's digits are even we'll enter the if condition
                count += 1     #Update the counter by 1
        return count    #We'll return the counter at the end of loop. 

#Example:
#array = [555, 901, 482, 1771]
#Count = 0
#i = 0
#splitArrayDigit = [5, 5, 5]
#If condition-check is false for i = 0. 
#Count = 0
#i = 1
#splitArrayDigit = [9, 0, 1]
#If condition-check is false for i = 1.
#Count = 0
#i = 2
#splitArrayDigit = [4, 8, 2]
#If condition-check is false for i = 2.
#Count = 0
#i = 3
#splitArrayDigit = [1, 7, 7, 1]
#If condition-check is true for i = 3.
#Count = 1
#So for this array we'll get count = 1. So even number of digits are for this example is 1.  