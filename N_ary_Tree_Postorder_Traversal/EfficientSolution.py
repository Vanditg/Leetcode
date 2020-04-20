##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 590
## Problem Name: N-ary Tree Postorder Traversal    
##===================================
#
#Given an n-ary tree, return the postorder traversal of its nodes' values.
#
#Nary-Tree input serialization is represented in their level order traversal, 
#each group of children is separated by the null value (See examples).
#
#Follow up:
#
#Recursive solution is trivial, could you do it iteratively?
class Solution:
    def postorder(self, root):
        if not root:	#Condition-check: If root is empty
            return []	#Return empty list
        stack = [root]	#Initialize stack by adding root
        tmp = []	#Initialize tmp empty list
        while stack:	#Loop through stack
            node = stack.pop()	#Initialize node value by pop out element from stack 
            tmp.append(node.val)	#Append that element's value in tmp list
            for child in node.children:	#Loop through children
                stack.append(child)	#Append child value to stack
        return tmp[::-1]	#Return reverse of the list 