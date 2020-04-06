##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 1
## Problem Name: Two Sum
##===================================
#
#Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
#Example:
#
#Given nums = [2, 7, 11, 15], target = 9,
#
#Because nums[0] + nums[1] = 2 + 7 = 9,
#
#return [0, 1].

class Solution:
	def twoSum(self, array, target):
		complementDictionary = dict() #Initializing Dictionary. Before first iteration it is empty {}
		
		for i in range(len(array)):   #Loop through array
			arr = array[i]            #For every element of array
			complement = target - arr #Find complement i.e i = 0, arr = array[0] = 2. So complement = 9 - 2 = 7
			
			if arr in complementDictionary:    #Condition check if array value is in dictionary
				return [complementDictionary[arr], i]   #We'll return indices >> [complementDictionary[arr] = empty, i = 0]
			else:
				complementDictionary[complement] = i    #Otherwise we'll add that in our dictionary. So it will be {7 : 0}

# First Iteration:
# complementDictionary is empty. 
# i = 0 
# arr = array[0] = 2
# complement = 9 - 2 = 7
# if 2 is in dictionary (Which is not), we'll return [dictionary value for array, i]
# else we'll add complement is our dictionary which will now {7 : 0}

# Second Iteration:
# Dictionary is {7 : 0}
# i = 1
# arr = array[1] = 7
# if 7 is in dictionary (Which is), we'll return [dictionary[7] = 0, i = 1]
#This indices will be [0, 1]