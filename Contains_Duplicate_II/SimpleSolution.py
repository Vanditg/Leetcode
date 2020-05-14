##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 219
## Problem Name: Contains Duplicate II  
##===================================
#
#Given an array of integers and an integer k, 
#find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and 
#the absolute difference between i and j is at most k.
#
#Example 1:
#
#Input: nums = [1,2,3,1], k = 3
#Output: true
#Example 2:
#
#Input: nums = [1,0,1,1], k = 1
#Output: true
#Example 3:
#
#Input: nums = [1,2,3,1,2,3], k = 2
#Output: false
class Solution:
    def containsNearbyDuplicate(self, nums, k): 
        tmp = {}	#Initialize tmp dictionary 
        for i in range(len(nums)):	#Loop through numbers 
            if nums[i] in tmp and i - tmp[nums[i]] <= k:	#Condition-check: If number in dictionary and absolute difference is at most k 
                return True	#We return true 
            tmp[nums[i]] = i	#Update dictionary 
        return False	#Return False 