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
        self.tmp = 0	#Initialize tmp = 0
        length = self.dfs(root)	#Initialize length, which is after running dfs, we'll get the count 
        return tmp	#We'll return tmp 
    def dfs(self, node):	#Define DFS
        if node is None:	#Condition-check: If node is empty	 
            return 0	#We return 0
        l, r = self.dfs(node.left), self.dfs(node.right)	#Initialize l and r 
        self.tmp = max(self.tmp, l + r)	#Update tmp by finding max between tmp and l + r
        return 1 + max(l, r)	#Return 1 + max between l and r