##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 1365
## Problem Name: How Many Numbers Are Smaller Than the Current Number
##===================================
#
#Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. 
#That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
#Return the answer in an array.
#Example 1:
#
#Input: nums = [8,1,2,2,3]
#Output: [4,0,1,1,3]
#Explanation: 
#For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
#For nums[1]=1 does not exist any smaller number than it.
#For nums[2]=2 there exist one smaller number than it (1). 
#For nums[3]=2 there exist one smaller number than it (1). 
#For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).
#
#Example 2:
#
#Input: nums = [6,5,4,8]
#Output: [2,1,0,3]
#
#Example 3:
#
#Input: nums = [7,7,7,7]
#Output: [0,0,0,0]
import bisect as b    #Importing bisect search module 
class Solution:
    def smallerNumbersThanCurrent(self, number):
        count = 0    #Initialize counter count 
        output = []   #Initialize output list
        sortNumber = sorted(number)    #Sorting the number 
 
        for i in range(len(number)):    #loop through number 
            count = b.bisect_left(sortNumber, number[i])     #Where count is equal to bisect search of left - sortNumber and number[i]
            output.append(count)     #We'll append in our output list. 
        return output   #We'll return output list at the end. 
		
#Iteration:
#number = [6, 5]
#Count = 0
#output = []
#sortNumber = [5, 6]
#For loop i = 0
#count = b.bisect_left([5, 6], 5), count = 0
#output = [0]
#For loop i = 1
#count = b.bisect_left([5, 6], 6) count = 1
#output = [0, 1]