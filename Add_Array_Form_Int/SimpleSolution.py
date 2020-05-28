##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 989
## Problem Name: Add to Array-Form of Integer          
##===================================
#
#For a non-negative integer X, the array-form of X is an array of its digits in left to right order.  
#For example, if X = 1231, then the array form is [1,2,3,1].
#
#Given the array-form A of a non-negative integer X, return the array-form of the integer X+K.
#
#Example 1:
#
#Input: A = [1,2,0,0], K = 34
#Output: [1,2,3,4]
#Explanation: 1200 + 34 = 1234
#Example 2:
#
#Input: A = [2,7,4], K = 181
#Output: [4,5,5]
#Explanation: 274 + 181 = 455
#Example 3:
#
#Input: A = [2,1,5], K = 806
#Output: [1,0,2,1]
#Explanation: 215 + 806 = 1021
#Example 4:
#
#Input: A = [9,9,9,9,9,9,9,9,9,9], K = 1
#Output: [1,0,0,0,0,0,0,0,0,0,0]
#Explanation: 9999999999 + 1 = 10000000000
class Solution:
    def addToArrayForm(self, A, K):
        if A is None:	#Condition-check: If A is empty list 
            return [int(i) for i in str(K)]	#We return K 
        if K is None:	#Condition-check: If K is None
            return A	#We return A list 
        tmp = ''.join(str(A[i]) for i in range(len(A)))	#Initialize tmp and convert the list to number 
        SUM = int(tmp) + K	#Initialize SUM and add tmp and K 
        return [int(i) for i in str(SUM)]	#We return the SUM's list 