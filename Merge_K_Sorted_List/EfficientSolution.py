##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 23
## Problem Name: Merge k Sorted Lists  
##===================================
#
#Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
#
#Example:
#
#Input:
#[
#  1->4->5,
#  1->3->4,
#  2->6
#]
#Output: 1->1->2->3->4->4->5->6
class Solution:
    def mergeKLists(self, lists):
        tmp = []	#Initialize tmp empty list
        dummy = head = ListNode(0)	#Initialize dummy linkedlist
        for i in lists:	#Loop through lists
            while i:	#Loop 
                tmp.append(i.val)	#Append values in tmp list
                i = i.next	#Traverse through list
        for i in sorted(tmp):	#Loop through sorted tmp list
            dummy.next = ListNode(i)	#Add the values in dummy linkedlist
            dummy = dummy.next	#Point reference to next node 
        return head.next	#Return our sorted dummy list