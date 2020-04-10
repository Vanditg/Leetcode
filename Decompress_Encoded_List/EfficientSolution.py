##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 1313
## Problem Name: Decompress Run-Length Encoded List
##===================================
#
#We are given a list nums of integers representing a list compressed with run-length encoding.
#
#Consider each adjacent pair of elements [freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0).  
#For each such pair, there are freq elements with value val concatenated in a sublist. 
#Concatenate all the sublists from left to right to generate the decompressed list.
#
#Return the decompressed list.
#
#Example 1:
#
#Input: nums = [1,2,3,4]
#Output: [2,4,4,4]
#Explanation: The first pair [1,2] means we have freq = 1 and val = 2 so we generate the array [2].
#The second pair [3,4] means we have freq = 3 and val = 4 so we generate [4,4,4].
#At the end the concatenation [2] + [4,4,4] is [2,4,4,4].
#
#Example 2:
#
#Input: nums = [1,1,2,3]
#Output: [1,3,3]
class Solution:
    def decompressRLElist(self, number):
        tmpArray = []    #Intialize temporary array - tmpArray
        for i in range(len(number)):    #Loop through number
            if i % 2 == 0:    #Condition-check: if i is even, we enters the if condition
                freq = nums[i]    #Here we assign freq = nums[i], so freq will be even places from the list. 
            else:    #Condition-check: Else block for i is odd
                value = nums[i]   #Here we assign value = nums[i], so value will be odd places from the list. 
                tmpValue = [value]*freq   #We create tmpArray by adding [value]*freq
                new_tmpValue = str(tmpValue).replace('[','').replace(']','')    #Some operations to modify our array - replacing brackets with nothing i.e a = [1, 2, 3] output = 1, 2, 3
                final_tmpValue = str(new_tmpValue).replace(" ", "")    #Some operations to modify our array - replacing whitespaces with no spacing i.e a = 1, 2, 3 output = 1,2,3
                #print(final_tmpValue)
                tmpArray.append(final_tmpValue)   #Finally we append the array in our final tmpArray.
		return tmpArray    #We return the tmpArray
#Example:
#nums = [1,1,2,3]
#tmpArray = []
#i = 0
#freq = 1
#i = 1
#value = 1
#tmpValue = [1]*1 = [1]
#new_tmpValue = 1
#final_tmpValue = 1
#tmpArray after append = [] + [1] = [1]
#i = 2
#freq = 2
#i = 3
#value = 3
#tmpValue = [3]*2 = [3, 3]
#new_tmpValue = 3, 3
#final_tmpValue = 3,3
#tmpArray after append = [1] + [3,3] = [1,3,3]
#return tmpArray = [1,3,3] which is output