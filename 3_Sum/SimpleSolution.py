##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 15
## Problem Name: 3Sum 
##===================================
#Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
#
#Note:
#
#The solution set must not contain duplicate triplets.
#
#Example:
#
#Given array nums = [-1, 0, 1, 2, -1, -4],
#
#A solution set is:
#[
#  [-1, 0, 1],
#  [-1, -1, 2]
#]
class Solution:
    def threeSum(self, nums):
        nums.sort()	#Sort the input array
        result = set()	#Create empty set result
        for i in range(len(nums)):	#Loop through list 
            tmp = -nums[i]	#Create tmp which is negative of the list i's value
            left, right = i + 1, len(nums) - 1	#Create left and right which stores given values in loop
            while left < right:	#While left is less then right 
            sum = nums[left] + nums[right]	#Create sum which stores the given equations value 
            if sum < tmp:	#Condition-check: if sum's value is less then tmp
                left += 1	#Increase the left value by 1.
            elif sum > tmp	#Condition-check: else if sum's value is greater than tmp
                right -= 1	#Decrease the right value by 1. 
            else:	#Condition-check: If we reach the target getting zero.
                result.add((nums[i], nums[left], nums[j]))	#Add those value in set one list by list. 
                left += 1	#Increase left by 1
                right -= 1	#Decrease right by 1. 
        return result	#We return the final solution set. 