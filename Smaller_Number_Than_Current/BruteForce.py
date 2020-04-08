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

class Solution:
    def smallerNumbersThanCurrent(self, number):
        output = []    #Intialize output list. 
        for i in range(len(number)):    #Loop through Number
            counter = 0    #Intialize our counter 
			for j in range(len(number)):    #Loop through NUmber 
                if (number[j] < number[i]) and (j != i):    #Condition-check - Number[j] < Number[i] and J and  are not equal. 
                    counter += 1    #If passed the condition, we'll update the counter by one. 
            output.append(counter)    #We'll append counter in output list. 
        return counter    #Finally we'll return counter after loop completes.
#Example
#Number = [6, 5]
#Output = [1, 0]
#Code iteration: 
#output = []
#len(number) = 2; so for i = 0
#We enters the loop and Intialize counter = 0. 
#len(number) = 2; so for j = 0. 
#We enters the loop and condition check: condition fails as j == i, so for then j = 1, we'll have if (5 < 6) and (1 != 0), 
#So condition passses and we update our counter. 
#Counter = 1 and we'll append it to output list, so output = [1]. 
#So on we'll get output = [1, 0]