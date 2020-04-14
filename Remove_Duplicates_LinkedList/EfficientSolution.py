##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 83
## Problem Name: Remove Duplicates from Sorted List
##===================================
#
#Given a sorted linked list, delete all duplicates such that each element appear only once.
#
#Example 1:
#
#Input: 1->1->2
#Output: 1->2
#
#Example 2:
#
#Input: 1->1->2->3->3
#Output: 1->2->3
class Solution:
    def deleteDuplicates(self, head): 
        tmp = head	#Referencing head value to tmp

        while tmp and tmp.next:	#Loop till tmp and tmp.next is not empty
            if tmp.val == tmp.next.val:	#Condition-check: if tmp.val and tmp.next.val is same 
                tmp.next = tmp.next.next	#We point to tmp.next.next 
            else:	#Condition-check: else condition
                tmp = tmp.next	#We point to tmp.next
        return head	#We'll return the head at the end. 
#Example:
#head = [1, 1, 2]
#tmp = head = [1, 1, 2]
#While loop:
#----------
#tmp.val = 1 and tmp.next.val = 1
#tmp.next = tmp.next.next = 1
#----------
#tmp.val = 1 and tmp.next.next = 2
#----------
#head = [1, 2]