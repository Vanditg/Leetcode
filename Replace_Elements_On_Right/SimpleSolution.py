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
        tmpArray = [-1 for _ in range(len(array))]   #Creating tmpArray and fill it up with -1 for len(array)
        for i in range(len(array)) - 2, -1, -1):    #Loop through array in reverse manner.
            tmpArray[i] = max(tmpArray[i + 1], array[i + 1])    #Update the tmpArray[i] by using max function between actual and tmpArray.
        return tmpArray    #Returning tmpArray at the end.

#Example
#array = [17, 18, 5, 4, 6, 1]
#tmpArray = [-1, -1, -1, -1, -1, -1]
#Now range will be range(4, -1, -1)
#array =    [17, 18,  5,  4,  6,  1]
#tmpArray = [-1, -1, -1, -1, -1, -1]
#Index =    [0,   1,  2,  3,  4,  5]
#i = 4
#tmpArray[4] = max(tmpArray[5], array[5]) = max(-1, 1) = 1
#tmpArray = [-1, -1, -1, -1,  1,  -1]
#array =    [17, 18,  5,  4,  6,  1]
#i = 3
#tmpArray[3] =max(tmpArray[4], array[4]) = max(1, 6) = 6
#tmpArray = [-1, -1, -1,  6,  1,  -1]
#array =    [17, 18,  5,  4,  6,  1]
# and so on we'll get tmpArray = [18, 6, 6, 6, 1, -1]
