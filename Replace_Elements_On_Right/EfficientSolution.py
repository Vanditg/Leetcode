##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 1299
## Problem Name: Replace Elements with Greatest Element on Right Side
##===================================
#
#Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.
#
#After doing so, return the array.
#
#Example 1:
#
#Input: arr = [17,18,5,4,6,1]
#Output: [18,6,6,6,1,-1]
class Solution:
    def replaceElements(self, array):
        maxValue = -1   #Define maxValue variable -1.
        for i in range(len(array)) - 1, -1, -1):   #Loop through array in reverse order
            maxValue, array[i] = max(maxValue, array[i]), maxValue    #Interchange the maxValue and array[i] 
        return array    #Return final array