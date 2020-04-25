##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 152
## Problem Name: Maximum Product Subarray
##===================================
#
#Given an integer array nums, find the contiguous subarray within an array 
#(containing at least one number) which has the largest product.
#
#Example 1:
#
#Input: [2,3,-2,4]
#Output: 6
#Explanation: [2,3] has the largest product 6.
#
#Example 2:
#
#Input: [-2,0,-1]
#Output: 0
#Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
class Solution:
    def maxProduct(self, nums):
        tmp, maxProduct, minProduct = float('-inf'), 1, 1	#Initialize tmp, maxProduct, minProduct
        for i in nums:	#Loop through numbers 
            if i < 0:	#Condition-check: If number is negative
                minProduct, maxProduct = maxProduct, minProduct	#Swap the minProduct and maxProduct
            maxProduct = max(maxProduct*i, i)	#Update maxProduct by taking max of number and maxProduct*i
            minProduct = min(minProduct*i, i)	#Update maxProduct by taking min of number and minProduct*i
            tmp = max(tmp, maxProduct)	#Update tmp by taking max of tmp and maxProduct
        return tmp	#We return tmp at the end 