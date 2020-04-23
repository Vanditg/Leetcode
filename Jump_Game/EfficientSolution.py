##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 55
## Problem Name: Jump Game  
##===================================
#
#Given an array of non-negative integers, you are initially positioned at the first index of the array.
#
#Each element in the array represents your maximum jump length at that position.
#
#Determine if you are able to reach the last index.
#
#Example 1:
#
#Input: [2,3,1,1,4]
#Output: true
#Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
#
#Example 2:
#
#Input: [3,2,1,0,4]
#Output: false
#Explanation: You will always arrive at index 3 no matter what. Its maximum
#             jump length is 0, which makes it impossible to reach the last index.
class Solution:
    def canJump(self, arr):
        curr = 0	#Initialize curr  
        for i in range(len(arr)):	#Loop through array
            if i > curr:	#Condition-check: If index > curr
	            return False 	#We return false 
            curr = max(curr, i + arr[i])	#Update curr by taking max of curr and i + arr[i]
        return True	#Otherwise return True 