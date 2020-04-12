##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 206
## Problem Name: Reverse Linked List
##===================================
#
#Reverse a singly linked list.
#
#Example:
#
#Input: 1->2->3->4->5->NULL
#Output: 5->4->3->2->1->NULL
class Solution:
    def reverseList(self, head):
        previous = None    #Set previous to None
        current = head     #Set current to head 
        while current:     #While our head is not empty
            following = current.next    #Our following points to current.next
            current.next = previous     #Current.next will be previous 
            previous = current          #Our previous points to current
            current = following    #Current points to following
        head = previous     #Set head to previous
        return head     #We'll return head at the end.
#Example 
#Input: head = [1, 2]
#previous = None
#current = [1, 2]
#While Loop:
#current = [1, 2]
#following = [2]
#current next = None (Null)
#previous =  [1]
#current = [2]
#--------------
#current = [2]
#following = None (Null)
#current next = [1]
#previous =  [2, 1]
#current = None (Null)
---------------
#head = [2, 1]