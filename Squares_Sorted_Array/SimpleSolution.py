##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 977
## Problem Name: Squares of a Sorted Array  
##===================================
#
#Given an array of integers A sorted in non-decreasing order, 
#return an array of the squares of each number, also in sorted non-decreasing order.
#
#Example 1:
#
#Input: [-4,-1,0,3,10]
#Output: [0,1,9,16,100]
#Example 2:
#
#Input: [-7,-3,2,3,11]
#Output: [4,9,9,49,121]
class Solution:
    def sortedSquares(self, A):
        tmp = [abs(i) for i in A]	#Initialize tmp and convert all negatives to positive using absolute function  
        tmp.sort()	#Sort tmp list 
        tmpSquare = [0]*len(A)	#Initialize tmpSquare same length as A
        for i in range(len(tmp)):	#Loop through tmp 
            tmpSquare[i] = tmp[i]*tmp[i]	#Update the tmpSquare by adding squares of number 
        return tmpSquare	#Return tmpSquare