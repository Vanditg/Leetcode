##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 543
## Problem Name: Diameter of Binary Tree         
##===================================
#
#Given a binary tree, you need to compute the length of the diameter of the tree. 
#The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
#This path may or may not pass through the root.
#
#Example:
#Given a binary tree
#          1
#         / \
#        2   3
#       / \     
#      4   5    
#Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
class Solution:
    def diameterOfBinaryTree(self, root):
        if root is None:	#Condition-check: If root is empty
            return 0	#We return zero
        left = self.length(root.left)	#Initialize left and count the length of left sub-tree
        right = self.length(root.right)	#Initialize right and count the length of right sub-tree
        leftDiameter = self.diameterOfBinaryTree(root.left)	#Initialize leftDiameter 
        rightDiameter = self.diameterOfBinaryTree(root.right)	#Initialize rightDiameter
        return max(left + right, max(leftDiameter, rightDiameter))	#We return max between these two parameters
    
    def length(self, root):	#Define length function 
        if root is None:	#Condition-check: If root is empty
            return 0	#We return zero
        else:	#Condition-check: Else
            return 1 + max(self.length(root.left), self.length(root.right))	#We return total length for the tree