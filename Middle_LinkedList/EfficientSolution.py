##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 876
## Problem Name: Middle of the Linked List 
##===================================
#
#Given a non-empty, singly linked list with head node head, return a middle node of linked list.
#
#If there are two middle nodes, return the second middle node.
#
#Example 1:
#
#Input: [1,2,3,4,5]
#Output: Node 3 from this list (Serialization: [3,4,5])
#The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
#Note that we returned a ListNode object ans, such that:
#ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.
#
#Example 2:
#
#Input: [1,2,3,4,5,6]
#Output: Node 4 from this list (Serialization: [4,5,6])
#Since the list has two middle nodes with values 3 and 4, we return the second one.
class Solution:
    def middleNode(self, head):
        tmp = head    #Referencing head value to tmp
		counter = 0   #Initialize counter
		while tmp:    #While our head is not empty
            counter += 1    #We'll traverse through list and increase our counter by 1.
            tmp = tmp.next   #We'll point to next value
        middle = counter // 2    #Find the middle index of linked list, that return integer value
        newTmp = head    #Referencing head value to newTmp
        for i in range(middle):    #Loop throuh middle in list
            newTmp = newTmp.next   #We'll point till we reach middle index
        return newTmp    #We'll return the newTmp value or serialization. 
#Example:
#tmp = [1, 2, 3, 4, 5, 6]
#counter = 0
#While Loop
#tmp = [1, 2, 3, 4, 5, 6]
#counter = 1
#tmp = [2, 3, 4, 5, 6]
#counter = 2
#tmp = [3, 4, 5, 6]
#counter = 3
#tmp = [4, 5, 6]
#counter = 4
#tmp = [5, 6]
#counter = 5
#tmp = [6]
#counter = 6
#Loop terminates
#Middle = counter // 2 ===>>> 3
#newTmp = [1, 2, 3, 4, 5, 6]
#For loop 
#i = 0
#newTmp = [2, 3, 4, 5, 6]
#i = 1
#newTmp = [3, 4, 5, 6]
#i = 2
#newTmp = [4, 5, 6]
#This newTmp we'll return as we reached the middle.