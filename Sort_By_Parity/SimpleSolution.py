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
        if A == []:	#Condition-check: If A is empty
            return None	#Return None
        A.sort()	#Sort the Array
        tmpEven = []	#Initialize tmpEven list
        for i in range(len(A)):	#Loop through A 
            if A[i] % 2 != 1:	#Condition-check: If element is not odd 
                tmpEven.append(A[i])	#Append that element in tmpEven
        tmpOdd = []	#Initialize tmpOdd list
        for j in range(len(A)):	#Loop through A
            if A[j] % 2 == 1:	#Condition-check: If element is odd
                tmpOdd.append(A[j])	#Append that element in tmpOdd
        tmp = tmpEven + tmpOdd	#Initialize tmp and add both even-odd list 
        return tmp	#Finally return tmp which is sorted array 