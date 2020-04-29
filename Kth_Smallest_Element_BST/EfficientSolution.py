##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 230
## Problem Name: Kth Smallest Element in a BST    
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
        if root is None or k is None:	#Condition-check: If root is null and k is null
            return None	#We return None.
        tmp = []	#Initialize tmp empty list
        while True:	#Loop while True
            while root:	#Loop while root is not empty
                tmp.append(root)	#Appned the root to tmp list
                root = root.left	#Point reference to left sub-tree
            node = tmp.pop()	#Initialize a node which will be last element of tmp list 
            k = -1	#Update k by decreasing 1 
            if not k:	#Condition-check: If k's value is different 
                return node.val	#Return node's value 
            root = root.right	#Otherwise update root to root.right subtree for finding the smallest element 