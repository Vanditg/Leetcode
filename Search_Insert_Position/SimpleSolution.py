##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 35
## Problem Name: Search Insert Position 
##===================================
#
#Given a sorted array and a target value, return the index if the target is found. 
#If not, return the index where it would be if it were inserted in order.
#
#You may assume no duplicates in the array.
#
#Example 1:
#
#Input: [1,3,5,6], 5
#Output: 2
#Example 2:
#
#Input: [1,3,5,6], 2
#Output: 1
#Example 3:
#
#Input: [1,3,5,6], 7
#Output: 4
#Example 4:
#
#Input: [1,3,5,6], 0
#Output: 0
class Solution:
    def searchInsert(self, nums, target): 
        tmp = 0	#Initialize tmp
        for i in range(len(nums)):	#Loop through nums 
            if nums[i] == target:	#Condition-check:	If target is in the nums list 
                tmp = nums.index(target)	#Update the tmp by the target index in the nums list 
            else:	#Condition-check: Else
                nums.append(target)	#Append the target value in the nums list 
                tmp = sorted(nums).index(target)	#Update the tmp by sorting nums list and return the index 
        return tmp	#Return tmp