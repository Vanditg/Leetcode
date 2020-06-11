##==================================
## Leetcode June Challenge 
## Username: Vanditg
## Year: 2020
## Problem:11
## Problem Name: Sort Colors 
##===================================
#
#Given an array with n objects colored red, white or blue, 
#sort them in-place so that objects of the same color are adjacent, 
#with the colors in the order red, white and blue.
#
#Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
#
#Example:
#
#Input: [2,0,2,1,1,0]
#Output: [0,0,1,1,2,2]
class Solution:
    def sortColors(self, nums):
        left, right, curr = 0, len(nums) - 1, 0
        while curr <= right:
            if nums[curr] == 0:
                nums[left], nums[curr] = nums[curr], nums[left]
                left, curr = left + 1, curr + 1
            elif nums[curr] == 2:
                nums[curr], nums[right] = nums[right], nums[curr]
                right = right - 1
            else:
                curr = curr + 1