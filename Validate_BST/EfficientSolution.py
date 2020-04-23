##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 98
## Problem Name: Validate Binary Search Tree   
##===================================
#
#Given a binary tree, determine if it is a valid binary search tree (BST).
#
#Assume a BST is defined as follows:
#
#The left subtree of a node contains only nodes with keys less than the node's key.
#The right subtree of a node contains only nodes with keys greater than the node's key.
#Both the left and right subtrees must also be binary search trees.
#
#Example 1:
#
#    2
#   / \
#  1   3
#
#Input: [2,1,3]
#Output: true
#Example 2:
#
#    5
#   / \
#  1   4
#     / \
#    3   6
#
#Input: [5,1,4,null,null,3,6]
#Output: false
#Explanation: The root node's value is 5 but its right child's value is 4.
class Solution:
    def isValid(self, root):
        return self.BST(root, float("-inf"), float("inf"))	#Return True or False based on Helper method BST
    def BST(self, root, minVal, maxVal):	#Defining helper method BST
        if root is None:	#Condition-check:If root is empty
            return True	#We return True 
        if root.val <= minVal or root.val >= maxVal:	#Condition-check:If root's value is less than or equal to min value or greater than equal to max value
            return False	#We return False
        validLeft = self.BST(root.left, minVal, root.val)	#Initialize validLeft by using helper method 
        validRight = self.BST(root.right, root.val, maxVal)	#Initialize validRight by using helper method
        return validLeft and validRight	#If niether of is False, we return False or True for both True values 