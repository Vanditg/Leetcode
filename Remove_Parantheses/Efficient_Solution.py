##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 1021
## Problem Name: Remove Outermost Parantheses 
##===================================
#
#A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.  For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
#
#A valid parentheses string S is primitive if it is nonempty, and there does not exist a way to split it into S = A+B, with A and B nonempty valid parentheses strings.
#
#Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.
#
#Return S after removing the outermost parentheses of every primitive string in the primitive decomposition of S.
#
#Example 1:
#
#Input: "(()())(())"
#Output: "()()()"
#Explanation: 
#The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
#After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
#
#Example 2:
#
#Input: "(()())(())(()(()))"
#Output: "()()()()(())"
#Explanation: 
#The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
#After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".
#
#Example 3:
#
#Input: "()()"
#Output: ""
#Explanation: 
#The input string is "()()", with primitive decomposition "()" + "()".
#After removing outer parentheses of each part, this is "" + "" = "".
class Solution:
    def removeOuterParantheses(self, S):
        tmp = ""	#Initialize tmp empty string 
        final_S = ""	#Initialize final_S empty string which we'll return at the end.
        count = 0	#Initialize count
        for i in range(len(S)):	#Loop through our string 
            tmp += S[i]	#tmp string will be tmp + S[i]. i.e: "" + "(" = "("
            if S[i] == '(':	#Condition-check: If S[i] == '('
                count += 1	#We'll increase our count by 1
            else:	#Condition-check: else then
                count -= 1	#We'll decrease count by 1
            if count == 0:	#Condition-check: Now, if we reach count to zero. 
                final_S += tmp[1:-1]	#final_S will be final_S + tmp[1:-1]. i.e. = "" + "(()())" = "" + "()()" = "()()"
                tmp = ""	#Then we'll change previous tmp string to empty string
        return final_S	#Finally we'll return final_S. 