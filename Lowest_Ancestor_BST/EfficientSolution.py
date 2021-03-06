##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 230
## Problem Name: Kth Smallest Element in a BST    
##===================================
#Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
#
#According to the definition of LCA on Wikipedia: 
#“The lowest common ancestor is defined between two nodes p and q as the 
#lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
#
#Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]
#
#Example 1:
#
#Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
#Output: 6
#Explanation: The LCA of nodes 2 and 8 is 6.
#Example 2:
#
#Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
#Output: 2
#Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if (p.val < root.val and q.val < root.val):	#Condition-check: If the values of p and q is in the left subtree
            return self.lowestCommonAncestor(root.left, p, q)	#Using recursion gives search for the left subtree and return the lowest ancestor
        elif (p.val > root.val and q.val > root.val):	#Condition-check: If the values of p and q is in the right subtree
            return self.lowestCommonAncestor(root.right, p, q)	#Using recursion gives search for the right subtree and return the lowest ancestor
        else:	#Condition-check: Else
            return root	#We simply return root value 