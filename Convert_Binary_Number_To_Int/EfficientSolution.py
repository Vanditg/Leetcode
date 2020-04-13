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
        value = 0   #Initialize value 
        while head:    #While head is not empty
            value = (value)*(2) + head.value    #Counting value based on given equation
            head = head.next    #Traversing
		return value   #Return the value
#Example:
#head = [1, 0, 1]
#value = 0
#While Loop start:
#--------
#head = [1, 0, 1]
#value = (0)*2 + 1 = 1
#--------
#head = [0, 1]
#value = (1)*2 + 0 = 2
#--------
#head = [1]
#value = (2)*2 + 1 = 5
#--------
#head = None
#value = 5