##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 108
## Problem Name: Convert Sorted Array to Binary Search Tree         
##===================================
#
#Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
#
#For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the 
#two subtrees of every node never differ by more than 1.
#
#Example:
#
#Given the sorted array: [-10,-3,0,5,9],
#
#One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:
#
#      0
#     / \
#   -3   9
#   /   /
# -10  5
class Solution:
    def sortedArrayToBST(self, nums):
        if nums is None:	#Condition-check: If nums is empty list
            return None	#Return none
        return self.BST(nums, 0, len(nums) - 1)	#We return helper method's output 
    def BST(self, nums, l, r)	#Defining helper method - BST
        if l > r:	#Condition-check: If left is greater than right 
            return None	#We return None 
        mid = (l + r) // 2	#Initialize mid which is the middle point of the list  
        tree = TreeNode(nums[mid])	#Initialize tree and set the root to mid point of nums 
        tree.left = self.BST(nums, l, mid - 1)	#Use recursion to build the left subtree
        tree.right = self.BST(nums, mid + 1, r)	#Use recursion to build the right subtree
        return tree	#We return tree 