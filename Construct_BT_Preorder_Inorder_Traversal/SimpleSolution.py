##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 105
## Problem Name: Construct Binary Tree from Preorder and Inorder Traversal
##===================================
#
#Given preorder and inorder traversal of a tree, construct the binary tree.
#
#Note:
#You may assume that duplicates do not exist in the tree.
#
#For example, given
#
#preorder = [3,9,20,15,7]
#inorder = [9,3,15,20,7]
#Return the following binary tree:
#
#    3
#   / \
#  9  20
#    /  \
#   15   7
class Solution:
    def buildTree(self, preorder, inorder):
        l_preorder = len(preorder)	#Initialize l_preorder by finding length of preorder
        l_inorder = len(inorder)	#Initialize l_inorder by finding length of inorder
        if l_preorder != l_inorder:	#Condition-check:	If l_preorder and l_inorder are not the same 
            return None	#We return none as the tree is different 
        if preorder is None:	#Condition-check: If preorder is empty
            return None	#We return none as preorder is different
        if inorder is None:	#Condition-check: If inorder is empty
            return None	#We return none as inorder is different
        if l_preorder == 0:	#If length of preorder is zero
            return None	#We return none as preorder is different
        root = TreeNode(preorder[0])	#Initialize root by taking first value from preorder
        root_index = inorder.index(root.val)	#Initialize root_index by taking index from inorder's root
        root.left = self.buildTree(preorder[1:root_index + 1], inorder[:root_index])	#Initialize root.left by using recursion
        root.right = self.buildTree(preorder[root_index + 1:], inorder[root_index + 1:])	#Initialize root.right by using recursion 
        return root	#We return root after no value is present in preorder or inorder		
        