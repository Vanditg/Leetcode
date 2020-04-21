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
        if not lists:	#Condition-check: If list is empty
            return	#Return Empty 
		if len(lists) == 1:	#Condition-check: If list has length of 1 
            return lists[0]	#Return that element 
        mid = len(lists) // 2	#Initialize mid point 
        left = self.mergeKLists(lists[:mid])	#Initialize left by 0 to mid point 
        right = self.mergeKLists(lists[mid:])	#Initialize right by mid point to last
        return	self.merge(left, right)	#Return sorted list by using helper method 
    def merge(self, list1, list2):	#Defining method merge that takes two list
        tmp = dummy = ListNode(0)	#Initialize tmp and dummy which are empty linkedlist
        while list1 and list2:	#Loop: List 1 and List 2 are not empty 
            if list1.val <= list2.val:	#Condition-check: If list1.val is less than or equal to list2.val
                tmp.next = ListNode(list1.val)	#Update the linkedlist by adding value of list1 
                tmp = tmp.next	#Traverse through tmp 
                list1 = list1.next	#Traverse through list1			 
            else:	#Condition-check: Else
                tmp.next = ListNode(list2.val)	#Update the linkedlist by adding value of list2
                tmp = tmp.next	#Traverse through tmp 
                list2 = list2.next	#Traverse through list2
        if list1:	#Condition-check: If list1 is empty 
            tmp.next = list1	#Change the point to list1
        else:	#Condition-check: Else
            tmp.next = list2	#Change the point to list2
        return dummy.next	#Return the dummy linkedlist