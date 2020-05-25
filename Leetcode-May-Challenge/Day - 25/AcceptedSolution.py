##==================================
## Leetcode May Challenge 
## Username: Vanditg
## Year: 2020
## Problem: 25
## Problem Name: Uncrossed Lines
##===================================
#
#We write the integers of A and B (in the order they are given) on two separate horizontal lines.
#
#Now, we may draw connecting lines: a straight line connecting two numbers A[i] and B[j] such that:
#
#A[i] == B[j];
#The line we draw does not intersect any other connecting (non-horizontal) line.
#Note that a connecting lines cannot intersect even at the endpoints: 
#each number can only belong to one connecting line.
#
#Return the maximum number of connecting lines we can draw in this way.
#
#Example 1:
#
#Input: A = [1,4,2], B = [1,2,4]
#Output: 2
#Explanation: We can draw 2 uncrossed lines as in the diagram.
#We cannot draw 3 uncrossed lines, because the line from A[1]=4 to B[2]=4 will intersect the line from A[2]=2 to B[1]=2.
#Example 2:
#
#Input: A = [2,5,1,2,5], B = [10,5,2,1,5,2]
#Output: 3
#Example 3:
#
#Input: A = [1,3,7,1,7,5], B = [1,9,2,5,1]
#Output: 2
class Solution:
    def maxUncrossedLines(self, A, B):
        lenA, lenB = len(A), len(B)	#Initialize lenA and lenB which is length of the list 
        dp = [[0 for i in range(lenB + 1] for j in range(lenA + 1)]	#Initialize dp and create a matrix with 0 value 
        for i in range(lenA):	#Loop through A 
            for j in range(lenB):	#Loop through B 
                if A[i] == B[j]:	#Condition-check: if the matching points found 
                    dp[i+1][j+1] = dp[i][j] + 1	#Update the value by increasing 1 
                else:	#Condition-check: Else
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])	#We take the max value from previous row and column 
        return dp[lenA][lenB]	#Return the last value in the matrix 