##==================================
## Leetcode May Challenge 
## Username: Vanditg
## Year: 2020
## Problem: 8
## Problem Name: Check If It Is a Straight Line
##===================================
#
#You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. 
#Check if these points make a straight line in the XY plane.
#
#Example 1:
#
#Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
#Output: true
#Example 2:
#
#Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
#Output: false
class Solution:
    def checkStraightLine(self, coordinates):
        x, y = coordinates[:2]	#Initialize tuple x, y which is first two coordinates
        return all(x[0] * y[1] - y[0] * x[1] + y[0] * k[1] - k[0] * y[1] + k[0] * x[1] - x[0] * k[1] == 0 for k in coordinates)	#Return True or False based on the condition - cross product for colinearity. 