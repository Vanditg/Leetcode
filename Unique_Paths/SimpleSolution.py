##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 62
## Problem Name: Unique Paths    
##===================================
#A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
#
#The robot can only move either down or right at any point in time. 
#
#The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
#
#How many possible unique paths are there?
#
#Above is a 7 x 3 grid. How many possible unique paths are there?
#
#Example 1:
#
#Input: m = 3, n = 2
#Output: 3
#Explanation:
#From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
#1. Right -> Right -> Down
#2. Right -> Down -> Right
#3. Down -> Right -> Right
#
#Example 2:
#
#Input: m = 7, n = 3
#Output: 28
class Solution:
    def uniquePaths(self, m, n):
        if m == 0 or n == 0:	#Condition-check: If m and n is zero
            return 0	#Return zero unique paths. 
        tmp = [[1 for j in range(m)] for i in range(n)]	#Create a 2d matrix of m column and n row, also filling row and column value by 1 
        for i in range(1, n):	#Loop through n 
            for j in range(1, m):	#Loop through m 
                tmp[i][j] = tmp[i][j-1] + tmp[i-1][j]	#Update tmp [i][j] by adding previous row's and column's value respectively 
        return tmp[n-1][m-1]	#Return tmp value which will be output of total unique Paths. 