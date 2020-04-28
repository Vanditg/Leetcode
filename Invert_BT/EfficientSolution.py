##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 226
## Problem Name: Invert Binary Tree   
##===================================
#Invert a binary tree.
#
#Example:
#
#Input:
#
#     4
#   /   \
#  2     7
# / \   / \
#1   3 6   9
#Output:
#
#     4
#   /   \
#  7     2
# / \   / \
#9   6 3   1
class Solution:
    def invertTree(self, root):
        if root is None:	#Condition-check:If root is empty 
            return root	#We return root
        else:	#Condition-check: Else
            left = self.invertTree(root.right)	#Use recursion to invert left values
            right = self.invertTree(root.left)	#Use recursion to invert right values
            root.left = left	#Update root.left tree to left
            root.right = right	#Update root.right tree to right
            return root	#We return root 