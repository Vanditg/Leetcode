##==================================
## Leetcode May Challenge 
## Username: Vanditg
## Year: 2020
## Problem: 20
## Problem Name: Kth Smallest Element in BST
##===================================
#
#Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
#
#Note:
#You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
#
#Example 1:
#
#Input: root = [3,1,4,null,2], k = 1
#   3
#  / \
# 1   4
#  \
#   2
#Output: 1
#Example 2:
#
#Input: root = [5,3,6,2,4,null,null,1], k = 3
#       5
#      / \
#     3   6
#    / \
#   2   4
#  /
# 1
#Output: 3
class Solution:
    def kthSmallest(self, root, k):
        return self.inOrder(root)[k - 1]	#Use our helper method to find the element
    def inOrder(self, root):	#Defining helper method 
        if root is None:	#Condition-check: If root is Null
            return []	#We return empty list
        inLeft = self.inOrder(root.left)	#Initialize InLeft, uses recursion for left subtree 
        rootVal = [root.val]	#Initialize rootVal, which is the element of root
        inRight = self.inOrder(root.right)	#Initialize InRight, uses recursion for right subtree
        return inLeft + rootVal + inRight	#We return the list comprising of inLeft, rootVal, and inRight
   