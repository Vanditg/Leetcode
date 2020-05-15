##==================================
## Leetcode May Challenge 
## Username: Vanditg
## Year: 2020
## Problem: 15
## Problem Name: Maximum Sum Circular Subarray
##===================================
#
#Given a circular array C of integers represented by A, find the maximum possible sum of a non-empty subarray of C.
#
#Here, a circular array means the end of the array connects to the beginning of the array.  (Formally, C[i] = A[i] when 0 <= i < A.length, and C[i+A.length] = C[i] when i >= 0.)
#
#Also, a subarray may only include each element of the fixed buffer A at most once.  (Formally, for a subarray C[i], C[i+1], ..., C[j], there does not exist i <= k1, k2 <= j with k1 % A.length = k2 % A.length.)
#
#Example 1:
#
#Input: [1,-2,3,-2]
#Output: 3
#Explanation: Subarray [3] has maximum sum 3
#Example 2:
#
#Input: [5,-3,5]
#Output: 10
#Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10
#Example 3:
#
#Input: [3,-1,2,-1]
#Output: 4
#Explanation: Subarray [2,-1,3] has maximum sum 2 + (-1) + 3 = 4
#Example 4:
#
#Input: [3,-2,2,-3]
#Output: 3
#Explanation: Subarray [3] and [3,-2,2] both have maximum sum 3
#Example 5:
#
#Input: [-2,-3,-1]
#Output: -1
#Explanation: Subarray [-1] has maximum sum -1
class Solution:
    def maxSubarraySumCircular(self, A):
        def kadane(num):	#Defining KADANE helper method 
            curr, maxSum = num[0], num[0]	#Initialize curr and maxSum
            for i in num[1:]:	#Loop through num 
                curr = max(i, curr + i)	#Update curr by taking max of i and curr+i
                maxSum = max(curr, maxSum)	#Update maxSum by taking curr and maxSum
            return maxSum	#Return maxSum
        tmp = kadane(A)	#Initialize tmp using helper method 
        currSum = 0	#Initialize currSum
        for i in range(len(A)):	#Loop through list 
            currSum += A[i]	#Update currSum
            A[i] = -A[i]	#Change the value to negative or positive
            currSum = currSum + kadane(A)	#Update currSum
        if currSum > tmp and currSum != 0:	#Condition-check: If currSum is greater than tmp and currSum is not 0
            return currSum 		#Return currSum
        else:	#Condition-check: Else
            return tmp	#Return tmp