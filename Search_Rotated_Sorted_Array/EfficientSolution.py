##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 33
## Problem Name: Search in Rotated Sorted Array    
##===================================
#
#Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
#
#(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
#
#You are given a target value to search. If found in the array return its index, otherwise return -1.
#
#You may assume no duplicate exists in the array.
#
#Your algorithm's runtime complexity must be in the order of O(log n).
#
#Example 1:
#
#Input: nums = [4,5,6,7,0,1,2], target = 0
#Output: 4
#
#Example 2:
#
#Input: nums = [4,5,6,7,0,1,2], target = 3
#Output: -1
class Solution:
    def search(self, nums, target):
        if not in nums:	#Condition-check: If nums is empty
            return -1	#Return -1 
        low = 0	#Initialize low 
        high = len(nums) - 1	#Initialize high 
        while low < high:	#Loop 
            mid = (low + high) // 2	#Initialize mid point
            if target == nums[mid]:	#Condition-check: If target is mid 
                return mid 	#We return mid 
            if nums[low] <= nums[mid]:	#Condition-check: If nums[low] <= nums[mid]
                if nums[low] <= target <= nums[mid]:	#Condition-check: If target is in the range 
                    high = mid - 1	#Update high by mid - 1
                else:	#Condition-check: Else
                    low = mid + 1	#Update low by mid + 1
            else:
                if nums[mid] <= target <= nums[high]	#Condition-check: If target is in the range
                    low = mid + 1	#Update low by mid + 1
                else:	#Condition-check: Else
                    high = mid - 1	#Update high by mid - 1
		return -1	#Otherwise we'll return -1