##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 20
## Problem Name: Valid Parantheses     
##===================================
#Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
#An input string is valid if:
#
#Open brackets must be closed by the same type of brackets.
#Open brackets must be closed in the correct order.
#Note that an empty string is also considered valid.
#
#Example 1:
#
#Input: "()"
#Output: true
#
#Example 2:
#
#Input: "()[]{}"
#Output: true
#
#Example 3:
#
#Input: "(]"
#Output: false
#
#Example 4:
#
#Input: "([)]"
#Output: false
#
#Example 5:
#
#Input: "{[]}"
#Output: true
class Solution:
    def isValid(self, s):
        tmp = []	#Initialize stack
        for i in range(len(s)):	#Loop through string 
            if self.isOpenParentheses(s[i]):	#Condition_check: Using helper method 
                tmp.append(s[i])	#Append the character to stack 
            else:	#Condition_check: else 
                if len(tmp) == 0:	#If string is empty 
                    return False	#Return False
                open = tmp.pop()	#Initialize open and pop the character
                close = s[i]	#Initialize close which will be our character
                isValid = self.parenthesesSame(open, close)	#Initialize isValid and using helper method
                if not isValid:	#Condition_check: If it's not vaild 
                    return False	#Return fasle
        return len(tmp) == 0	#Return true or false if condition do not met
    
    def isOpenParentheses(self, str):	#Define helper method 1
        if str == '(' or str == '[' or str == '{':	#Condition_check: If string character has these type
            return True 	#Return true 
        return False	#Otherwise return false
    
    def parenthesesSame(self, open, close):	#Define helper method 2 
        if open == '(' and close == ')':	#Condition_check: if the brackets are same 
            return True	#Return True
        elif open == '{' and close == '}':	#Condition_check: if the brackets are same
            return True	#Return True
        elif open == '[' and close == ']':	#Condition_check: if the brackets are same
            return True	#Return True
        else:	#Condition_check: else 
            return False	#Return false