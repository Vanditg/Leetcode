##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 104
## Problem Name: Maximum Depth of Binary Tree 
##===================================
#
#Given a binary tree, find its maximum depth.
#
#The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
#
#Note: A leaf is a node with no children.
#
#Example:
#
#Given binary tree [3,9,20,null,null,15,7],
#
#    3
#   / \
#  9  20
#    /  \
#   15   7
#return its depth = 3.
class Solution:
    def maxDepth(self, root):
        if root is None:	#Condition-check:If root is empty
            return 0	#We return zero, as depth is zero for base case
        else:	#Condition-check:Else
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))	#We return total depth of tree by using recursion