##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 1389
## Problem Name:  Create Target Array in the Given Order
##===================================
#
#Given two arrays of integers nums and index. Your task is to create target array under the following rules:
#
#Initially target array is empty.
#From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
#Repeat the previous step until there are no elements to read in nums and index.
#Return the target array.
#
#It is guaranteed that the insertion operations will be valid.
#
#Example 1:
#
#Input: nums = [0,1,2,3,4], index = [0,1,2,2,1]
#Output: [0,4,1,3,2]
#Explanation:
#nums       index     target
#0            0        [0]
#1            1        [0,1]
#2            2        [0,1,2]
#3            2        [0,1,3,2]
#4            1        [0,4,1,3,2]
#
#Example 2:
#
#Input: nums = [1,2,3,4,0], index = [0,1,2,3,0]
#Output: [0,1,2,3,4]
#Explanation:
#nums       index     target
#1            0        [1]
#2            1        [1,2]
#3            2        [1,2,3]
#4            3        [1,2,3,4]
#0            0        [0,1,2,3,4]
#
#Example 3:
#
#Input: nums = [1], index = [0]
#Output: [1]

class Solution:
    def createTargetArray(self, nums, index):
        for i in range(len(nums)):    #Loop through nums. 
            for j in range(i):    #Loop through previous i. 
                if index[j] >= index[i]:    #Condition-check for left-right index allocation. 
                    index[j] += 1    Increment value by +1. 
        output = [0]*(len(nums))    #Creating an empty array Output. 
        
        for i in range(len(nums)):    #Loop through nums. 
            output[index[i]] = nums[i]    #Adding target value to output list.
     return output    #return output. 
#
#Example
#nums = [1] and index = [0]
#output = [1]