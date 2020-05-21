##==================================
## Leetcode May Challenge 
## Username: Vanditg
## Year: 2020
## Problem: 21
## Problem Name: Count Square Submatrices with All Ones
##===================================
#
#Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.
#
#Example 1:
#
#Input: matrix =
#[
#  [0,1,1,1],
#  [1,1,1,1],
#  [0,1,1,1]
#]
#Output: 15
#Explanation: 
#There are 10 squares of side 1.
#There are 4 squares of side 2.
#There is  1 square of side 3.
#Total number of squares = 10 + 4 + 1 = 15.
#Example 2:
#
#Input: matrix = 
#[
#  [1,0,1],
#  [1,1,0],
#  [1,1,0]
#]
#Output: 7
#Explanation: 
#There are 6 squares of side 1.  
#There is 1 square of side 2. 
#Total number of squares = 6 + 1 = 7.
class Solution:
    def countSquares(self, matrix):
        r, c = len(matrix), len(matrix[0])	#Initialize r and c which is lenght of row and column of matrix 
        tmp = [[0]*(c+1) for _ in range(r+1)]	#We create a dummy matrix filled with 0 having r+1 and c+1 row and column respectively 
        res = 0	#Initialize res which we'll return
        for row in range(1, r+1):	#Loop through row + 1
            for column in range(1, c+1):	#Loop through column + 1
                if matrix[row - 1][column - 1] == 1:	#If the matrix has 1 
                    tmp[row][column] = 1 + min(tmp[row][column -1], tmp[row - 1][column], tmp[row - 1][column - 1])	#Update 1 in the tmp matrix if we encounter 1 in the previous row, column or in the previous line 
                    res += tmp[row][column]	#Add all the values of tmp matrix and update in res 
        return res	#We return res 