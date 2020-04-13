##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 21
## Problem Name: Merge Two Sorted Lists
##===================================
#Merge two sorted linked lists and return it as a new list. 
#The new list should be made by splicing together the nodes of the first two lists.
#
#Example:
#
#Input: 1->2->4, 1->3->4
#Output: 1->1->2->3->4->4
class Solution:
    def mergeTwoLists(self, l1, l2):
        head = ListNode(0)	#Creating dummy linkedList which we'll return
        point = head	#Pointer for reference
        
        while l1 or l2:    #While either of the list is empty or not.
            if l1 is None and l2 is None:    #Condition-check: if l1 is empty and l2 is empty
                break	#We enter the condition and break the loop.
            elif l1 is None:	#Condition-check: if l1 is empty.
                point.next = l2		#We enter the condition and point it to l2 
                break	#Then we break the loop. 
            elif l2 is None:	#Condition-check: if l2 is empty
                point.next = l1		#We enter the condition and point it to l1
                break	#Then we break the loop. 
            else:
                val = 0		#Initialize val
                if l1.val < l2.val:		#Condition-check: if l1's element value is less than l2's element
                    val = l1.value	#We assign this l1's element to val
                    l1 = l1.next   #We then traverse through l1. 
                else:
                    val = l2.val	#We assign this l2's element to val
                    l2 = l2.next	#We then traverse through l2. 
                tmpNode = ListNode(val)		#We create a tmpNode, which will add the val
                point.next = tmpNode	#We point this to tmpNode
                point = point.next	#We point this to point.next  
		return head.next #Lastly, we return our dummy head. 