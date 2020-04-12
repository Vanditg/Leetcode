##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 1394
## Problem Name: Find Lucky Integer in an Array
##===================================
#
#Given an array of integers arr, a lucky integer is an integer which has a frequency in the array equal to its value.
#
#Return a lucky integer in the array. If there are multiple lucky integers return the largest of them. If there is no lucky integer return -1.
#
#Example 1:
#
#Input: arr = [2,2,3,4]
#Output: 2
#Explanation: The only lucky number in the array is 2 because frequency[2] == 2.
#
#Example 2:
#
#Input: arr = [1,2,2,3,3,3]
#Output: 3
#Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.
#
#Example 3:
#
#Input: arr = [2,2,2,3,3]
#Output: -1
#Explanation: There are no lucky numbers in the array.
#
#Example 4:
#
#Input: arr = [5]
#Output: -1
#
#Example 5:
#
#Input: arr = [7,7,7,7,7,7,7]
#Output: 7
import collections as c    #Importing collections module
class Solution:
    def findLucky(self, array):
        counter = c.Counter(array)    #Creating counter dictionary, inserting key (array integer) : value (count of integer). 
        lucky_number = -1    #Initiating lucky_number = -1
        for key, value in counter.items():    #Loop through counter for keys and value 
            if key == value:    #Condition-check: if key == value then we enter the condition
                lucky_number = max(lucky_number, key)   #We update lucky_number by max of (lucky_number, key)
        return lucky_number   #We return the lucky_number
		
#Example:
#array = [2, 2, 3, 4]
#counter = ({2 : 2, 3 : 1, 4 : 1})
#lucky_number = -1
#key = 2, value = 2
#Condition-check: key == value pass
#Lucky_number = max(-1, 2) = 2
#lucky_number = 2
 