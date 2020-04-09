##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 1221
## Problem Name: Split a String in Balanced Strings
##===================================
#
#Balanced strings are those who have equal quantity of 'L' and 'R' characters.
#
#Given a balanced string s split it in the maximum amount of balanced strings.
#
#Return the maximum amount of splitted balanced strings.
#
#Example 1:
#
#Input: s = "RLRRLLRLRL"
#Output: 4
#Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
#
#Example 2:
#
#Input: s = "RLLLLRRRLR"
#Output: 3
#Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.
#
#Example 3:
#
#Input: s = "LLLLRRRR"
#Output: 1
#Explanation: s can be split into "LLLLRRRR".
#
#Example 4:
#
#Input: s = "RLRRRLLRLL"
#Output: 2
#Explanation: s can be split into "RL", "RRRLLRLL", since each substring contains an equal number of 'L' and 'R'

class Solution:
    def balanceStringSplit(self, string):
        counter = 0    #Intialize counter 
        finalCounter = 0     #Intialize finalCounter which will return the max amount of splitted balanced strings. 
        for s in string:    #Loop through the string for extracting a character. 
            #print(s)
            if s == 'R':    #Condition-check: If the character is R. 
                counter += 1    #We pass the If Condition-check and increase the counter by 1. 
            elif s == 'L':    #Condition-check: Elif the character is L. 
                counter -= 1    #We pass the Elif Condition-check and decrease the counter by 1. 
            
			if counter == 0:    #Condition-check: If the counter will be zero.
                finalCounter += 1     #We pass the If Condition-check and increase the finalCounter by 1 because now counter is zero that means we have all substring in matching R and L form. 
        return finalCounter
#
#Example:
#Input string = "LLLLRRRR"
#counter = 0
#finalCounter = 0
#s = 'L'
#If Condition-check failed enter elif so counter = -1
#s = 'L'
#If Condition-check failed enter elif so counter = -1
#s = 'L'
#If Condition-check failed enter elif so counter = -1
#s = 'L'
#If Condition-check failed enter elif so counter = -1
#s = 'R'
#If Condition-check failed enter elif so counter = +1
#s = 'R'
#If Condition-check failed enter elif so counter = +1
#s = 'R'
#If Condition-check failed enter elif so counter = +1
#s = 'R'
#If Condition-check failed enter elif so counter = +1
#Now our finalCounter is -1 -1 -1 -1 +1 +1 +1 +1 = 0, so we increase this finalCounter by +1. 
#As we have completed the string, we simply return finalCounter. 
#So finalCounter = 1 for this input. 