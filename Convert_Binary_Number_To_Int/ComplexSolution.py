##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 1290
## Problem Name: Convert Binary Number in a Linked List to Integer
##===================================
#
#Given head which is a reference node to a singly-linked list. 
#The value of each node in the linked list is either 0 or 1. 
#The linked list holds the binary representation of a number.
#
#Return the decimal value of the number in the linked list.
#
#Example 1:
#
#Input: head = [1,0,1]
#Output: 5
#Explanation: (101) in base 2 = (5) in base 10
#
#Example 2:
#
#Input: head = [0]
#Output: 0
#
#Example 3:
#
#Input: head = [1]
#Output: 1
#
#Example 4:
#
#Input: head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
#Output: 18880
#
#Example 5:
#
#Input: head = [0,0]
#Output: 0
class Solution:
    def getDecimalValue(self, head):
        tmp = head
        count = 0
        while tmp:
            count += 1
            tmp = tmp.next
        tmpList = []
        for i in range(count - 1, -1, -1):
            j = 2**i
            tmpList.append(j)
        tmp = head
        emptyList = []
        while tmp:
            val = tmp.val
            emptyList.append(val)
            tmp = tmp.next 
        for i in range(len(emptyList)):
            for j in range(len(tmpList)):
                ab = [emptyList[i]*tmpList[i] for i in range(len(emptyList))]
        sum = 0
        for i in range(len(ab)):
            sum = sum + ab[i]
        return sum 