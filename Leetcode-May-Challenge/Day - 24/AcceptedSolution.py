##==================================
## Leetcode May Challenge 
## Username: Vanditg
## Year: 2020
## Problem: 24
## Problem Name:  Construct Binary Search Tree from Preorder Traversal
##===================================
#
#Return the root node of a binary search tree that matches the given preorder traversal.
#
#(Recall that a binary search tree is a binary tree where for every node, 
#any descendant of node.left has a value < node.val, 
#and any descendant of node.right has a value > node.val.  
#Also recall that a preorder traversal displays the value of the node first, 
#then traverses node.left, then traverses node.right.)
#
#It's guaranteed that for the given test cases there is always possible to 
#find a binary search tree with the given requirements.
#
#Example 1:
#
#Input: [8,5,1,7,10,12]
#Output: [8,5,10,1,7,null,12]
class Solution:
    def bstFromPreorder(self, preorder): 
        inorder = sorted(preorder)	#Initialize inorder which is sorted of preorder
        def helper(preorder, inorder):	#Defining helper method  
            lenP, lenI = len(preorder), len(inorder)	#Initialize lenP and lenI which is the length of the preorder and inorder
            if lenP != lenI or preorder == None or inorder == None or lenP == 0:	#Condition-check: If length are not the same or either of the order is null or length of preorder is zero 
                return None	#We return none 
            root = TreeNode(preorder[0])	#Initialize root by constructing tree node 
            rootIndex = inorder.index(root.val)	#Initialize rootIndex by finding the index from inorder of root's value
            root.left = helper(preorder[1:rootIndex+1], inorder[:rootIndex])	#Using recursion for left subtree to construct left subtree
            root.right = helper(preorder[rootIndex+1:], inorder[rootIndex+1])	#Using recursion for right subtree to construct right subtree
            return root	#We return root from the helper method  
        return helper(preorder, inorder)	#We return the root by using helper method 