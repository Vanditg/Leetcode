##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 561
## Problem Name: Array Partition I  
##===================================
#
#Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.
#
#Example 1:
#Input: [1,4,3,2]
#
#Output: 4
#Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).
class Solution:
    def arrayPairSum(self, nums):
        nums.sort()	#Sort the nums list
        count = 0	#Initialize count 
        for i in range(0, len(tmp), 2):	#Loop through tmp, starts from 0th index to len(tmp) taking 2 steps
            count += nums[i]	#Update count by taking sum of the elements 
        return count	#We return count 