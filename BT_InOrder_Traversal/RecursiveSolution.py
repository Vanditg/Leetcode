##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 94
## Problem Name: Binary Tree Inorder Traversal          
##===================================
#
#Given a binary tree, return the inorder traversal of its nodes' values.
#
#Example:
#
#Input: [1,null,2,3]
#   1
#    \
#     2
#    /
#   3
#
#Output: [1,3,2]
#Follow up: Recursive solution is trivial, could you do it iteratively?
class Solution:
    def inorderTraversal(self, root): 
        if root is None:	#If root is empty
            return []	#Return empty list
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)	#Return inorder traversal