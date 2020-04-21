##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 19
## Problem Name: Remove Nth Node From End of List   
##===================================
#
#Given a linked list, remove the n-th node from the end of list and return its head.
#
#Example:
#
#Given linked list: 1->2->3->4->5, and n = 2.
#
#After removing the second node from the end, the linked list becomes 1->2->3->5.
class Solution:
    def removeNthFromEnd(self, head, n):
        tmp = head	#Initialize tmp 
        count = 0	#Initialize count
        while tmp:	#Loop: tmp is not empty, we traverse the list 
            tmp = tmp.next	#point to next node 
            count += 1	#Increment count by 1
        index = count - n	#Initialize index which is given equation's result value 
        previous = None	#Initialize previous
		point = head	#Initialize point 
        while index != 0:	#Loop: index is not zero
            previous = point	#Assign point to previous
            point = point.next	#point to next node 
            index -= 1	#Decrease the index value by 1 
        if previous is None:	#Condition-check: If previous is empty
            return head.next 	#Return head.next
        else: 	#Condition-check: Else 
            previous.next = point.next		#Point point.next to previous.next
            point.next = None	#Point point.next to none 
            return head	#Return head at the end. 