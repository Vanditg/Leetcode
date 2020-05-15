##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 1351
## Problem Name: Count Negative Numbers in a Sorted Matrix
##===================================
#
#Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise. 
#
#Return the number of negative numbers in grid.
#
#Example 1:
#
#Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
#Output: 8
#Explanation: There are 8 negatives number in the matrix.
#Example 2:
#
#Input: grid = [[3,2],[1,0]]
#Output: 0
#Example 3:
#
#Input: grid = [[1,-1],[-1,-1]]
#Output: 3
#Example 4:
#
#Input: grid = [[-1]]
#Output: 1
class Solution:
    def countNegatives(self, grid):
        count = 0	#Initialize count 
        for i in range(len(grid)):	#Loop through grid
            for j in range(len(grid[0]))	#Loop through grid[0]
                if grid[i][j] < 0:	#Condition-check: If the value in the array matrix is negative
                    count += 1	#Update count by increasing 1 
        return count	#Return count