##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 118
## Problem Name: Pascal's Triangle         
##===================================
#
#Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
#
#In Pascal's triangle, each number is the sum of the two numbers directly above it.
#
#Example:
#
#Input: 5
#Output:
#[
#     [1],
#    [1,1],
#   [1,2,1],
#  [1,3,3,1],
# [1,4,6,4,1]
#]
class Solution:
    def generate(self, numRows):	
        if numRows is None:	#Condition-check: If numRows is empty 
            return []	#Return empty list
        tmp = []	#Initialize tmp list 
        for i in range(numRows):	#Loop through numRows
            tmp.append([0]*(i+1))	#Append the list i + 1 in tmp 
        for i in range(numRows):	#Loop through numRows 
            for j in range(i+1):	#Loop through i + 1
                if j == 0 or j == i:	#Condition-check: If j is zero or j is equal to i 
                    tmp[i][j] = 1	#Update the tmp i row, j column by 1 
                else:	#Condition-check: Else
                    tmp[i][j] = tmp[i-1][j-1] + tmp[i-1][j]	#Update tmp i row, j column by the equation
        return tmp	#Return tmp 