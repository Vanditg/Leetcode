##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 905
## Problem Name: Sort Array by Parity  
##===================================
#
#Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.
#
#You may return any answer array that satisfies this condition.
#
#Example 1:
#
#Input: [3,1,2,4]
#Output: [2,4,3,1]
#The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
class Solution:
    def sortArrayByParity(self, A): 
        tmp = []	#Initialize tmp list
        for i in range(len(A)):	#Loop through A
            if A[i] % 2 != 1:	#Condition-check: If element is even 
                tmp.append(A[i])	#Append the element in tmp
        for j in range(len(A)):	#Loop through A 
            if A[j] % 2 == 1:	#Condition-check: If element is odd
                tmp.append(A[j])	#Append the element in tmp 
        return tmp	#Return tmp at the end.