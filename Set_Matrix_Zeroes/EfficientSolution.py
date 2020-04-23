##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 73
## Problem Name: Set Matrix Zeroes      
##===================================
#Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.
#Example 1:
#
#Input: 
#[
#  [1,1,1],
#  [1,0,1],
#  [1,1,1]
#]
#Output: 
#[
#  [1,0,1],
#  [0,0,0],
#  [1,0,1]
#]
#Example 2:
#
#Input: 
#[
#  [0,1,2,0],
#  [3,4,5,2],
#  [1,3,1,5]
#]
#Output: 
#[
#  [0,0,0,0],
#  [0,4,5,0],
#  [0,3,1,0]
#]
class Solution:
    def setZeroes(self, matrix): 
        i, j = len(matrix), len(matrix[0])	#Initialize i, j 
        c = False	#Initialize bool c 
        for row in range(i):	#Loop through rows 
            if matrix[row][0] == 0:	#Condition-check: If row contains any zero element
                c = True 	#Update c to True 
            for column in range(1, j):	#Loop through column
                if matrix[row][column] == 0:	#Condition-check: If row and column has zero element
                    matrix[row][0] = 0	#Set row to zero 
                    matrix[column][0] = 0 	#Set column to zero
        for row in range(1, i):	#Loop through row
            for column in range(1, j):	#Loop through column
                if not matrix[row][0] or not matrix[0][column]:	#Condition-check: If row and matrix is empty 
                    matrix[row][column] = 0 	#Set row and column to zero
		if matrix[0][0] == 0:	#Condition-check: If 0th element row and column wise found 
            for column in range(j):	#Loop through column    
				matrix[0][column] = 0:	#set column to zero
        if c:	#Condition-check: If False
            for row in range(i):	#Loop through row
                matrix[row][0] = 0	#Set row to zero     