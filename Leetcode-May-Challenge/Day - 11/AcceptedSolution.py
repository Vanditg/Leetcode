##==================================
## Leetcode May Challenge 
## Username: Vanditg
## Year: 2020
## Problem: 11
## Problem Name: Flood Fill
##===================================
#
#An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).
#
#Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.
#
#To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.
#
#At the end, return the modified image.
#
#Example 1:
#Input: 
#image = [[1,1,1],[1,1,0],[1,0,1]]
#sr = 1, sc = 1, newColor = 2
#Output: [[2,2,2],[2,2,0],[2,0,1]]
#Explanation: 
#From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
#by a path of the same color as the starting pixel are colored with the new color.
#Note the bottom corner is not colored 2, because it is not 4-directionally connected
#to the starting pixel.
class Solution: 
    def floodFill(self, image, sr, sc, newColor):
        r, c = len(image), len(image[0])	#Initialize r and c 
        clr = image[sr][sc]	#Initialize clr which is the location of the color
        if clr == newColor:	#Condition-check: If clr is same as newColor
            return image	#Then we'll not change the color and return that image
        def dfs(row, column):	#Defining dfs accepts row, and column 
            if image[row][column] == clr:	#Condition-check: If location of that point is same as color 
                image[row][column] = newColor	#Then we change that to newColor
                if row >= 1:	#Condition-check: If row is greater or equal to 1
                    dfs(row - 1, column)	#Using DFS
                if row + 1 < r:	#Condition-check: If row + 1 is less than r 
                    dfs(row + 1, column)	#Using DFS
                if column >= 1:	Condition-check: If column is greater or equal to 1
                    dfs(row, column - 1)	#Using DFS
                if column + 1 < c:	#Condition-check: If column + 1 is less than c 
                    dfs(row, column + 1)	#Using DFS
        dfs(sr, sc)	#Using DFS to change the value to newColor for 4-connected point     
        return image