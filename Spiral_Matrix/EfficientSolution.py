##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 54
## Problem Name: Spiral Matrix    
##===================================
#
#Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
#
#Example 1:
#
#Input:
#[
# [ 1, 2, 3 ],
# [ 4, 5, 6 ],
# [ 7, 8, 9 ]
#]
#Output: [1,2,3,6,9,8,7,4,5]
#
#Example 2:
#
#Input:
#[
#  [1, 2, 3, 4],
#  [5, 6, 7, 8],
#  [9,10,11,12]
#]
#Output: [1,2,3,4,8,12,11,10,9,5,6,7]
class Solution:
    def spiralOrder(self, matrix):
        if not matrix:	#Condition-check: If matrix is empty
            return []	#Return empty array
        tmp = []	#Initialize tmp empty list
        r_b, r_e, c_b, c_e = 0, len(matrix), 0, len(matrix[0])	#Initialize row_begin, row_end, column_begin, column_end
        while r_e > r_b and c_e > c_b:	#Loop while the condition meets 
            for i in range(c_b, c_e):	#Loop through c_b to c_e
                tmp.append(matrix[r_b][i])	#Append the given value in list 
            for i in range(r_b + 1, r_e - 1):	#Loop through the given start and end point 
                tmp.append(matrix[i][c_e - 1])	#Append the given value in list
            if r_e != r_b + 1:	#Condition-check: If r_e's value is not equal to r_b + 1 
                for j in range(c_e - 1, c_b -1, -1):	#Loop through the given start and end point by decreasing j by 1
                    tmp.append(matrix[r_e - 1][j]	#Append the given value in list
            if c_b != c_e - 1:	#Condition-check: If c_b's value is not equal to c_e - 1
                for j in range(r_e - 2, r_b, -1):	#Loop through the given start and end point by decreasing j by 1
                    tmp.append(matrix[j][c_b])	#Append the given value in list
            r_b, r_e, c_b, c_e = r_b + 1, r_e - 1, c_b + 1, c_e - 1	#Update the values 
        return tmp	#Return tmp list at the end 