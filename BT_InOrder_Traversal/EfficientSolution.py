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
        out, tmp = [], root	#Initialize out empty list and tmp to root
        while tmp:	#Loop till tmp is empty
            if tmp.left is None:	#Condition-check: If left is none
                out.append(tmp.val)	#Append the val in out 
                tmp = tmp.right	#Point to tmp.right
            else:	#Condition-check: Else
                node = tmp.left	#Initialize node and set to tmp.left
                while node.right and node.right != tmp:	#Loop
                    node = node.right	#Update node to node.right 
                if node.right is None:	#Condition-check: If node.right is empty
                    node.right = tmp	#Update node.right to tmp 
                    tmp = tmp.left	#Point to tmp.left 
                else:	#Condition-check: Else
                    out.append(tmp.val)	#Append the val in out 
                    node.right = None	#Set node.right to None
                    tmp = tmp.right	#Point tmp to tmp.right
        return out	#Return out 