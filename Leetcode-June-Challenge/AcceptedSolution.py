##==================================
## Leetcode May Challenge 
## Username: Vanditg
## Year: 2020
## Problem: 1
## Problem Name: nvert Binary Tree
##===================================
#
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
        if root is None:	#Condition-check: If root is empty 
            return root	#We return root 
        else:	#Condition-check: Else
            left = self.invertTree(root.right)
            right = self.invertTree(root.left)
            root.left, root.right = left, right
            return root