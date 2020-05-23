##==================================
## Leetcode May Challenge 
## Username: Vanditg
## Year: 2020
## Problem: 965
## Problem Name: Univalued Binary Tree
##===================================
#
#A binary tree is univalued if every node in the tree has the same value.
#
Return true if and only if the given tree is univalued.
#
#Example 1:
#
#Input: [1,1,1,1,1,null,1]
#Output: true
#Example 2:
#
#Input: [2,2,2,5,2]
#Output: false
class Solution:
    def isUnivalTree(self, root): 
        if root is None:	#Condition-check: If root is empty 
            return True 
        def inOrder(root):	#Defining helper method - inOrder
            if root is None:	#Condition-check: If root is empty
                return []	#We return empty list 
            inLeft = inOrder(root.left)	#Initialize inLeft, using recursion for left sub-tree
            rootVal = [root.val]	#Initialize rootVal 
            inRight = inOrder(root.right)	#Initialize inRight, using recursion for right sub-tree
        tmp = inOrder(root)	#Using helper method to create a list of our root  
        return len(set(tmp)) == 1	#Return true or false based on the length of the list 