##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 100
## Problem Name: Same Tree
##===================================
#Given two binary trees, write a function to check if they are the same or not.
#
#Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
#
#Example 1:
#
#Input:     1         1
#          / \       / \
#         2   3     2   3
#
#        [1,2,3],   [1,2,3]
#
#Output: true
#Example 2:
#
#Input:     1         1
#          /           \
#         2             2
#
#        [1,2],     [1,null,2]
#
#Output: false
#Example 3:
#
#Input:     1         1
#          / \       / \
#         2   1     1   2
#
#        [1,2,1],   [1,1,2]
#
#Output: false
class Solution:
    def isSameTree(self, p, q): 
        if p is None and q is None:	#Condition-check: If p and q both are empty
            return True	#We return true
        if p is not None and q is None:	#Condition-check: If q is empty, while p is not
            return False	#We return false
        if p is None and q is not None:	#Condition-check: If p is empty, while q is not
            return False	#We return false
        if p.val != q.val:	#Condition-check: If p's val and q's val is not same 
            return False	#We return false
        sameLeft = self.isSameTree(p.left, q.left)	#Initialize sameLeft by using helper method to check True or False for left subtree
        sameRight = self.isSameTree(p.right, q.right)	#Initialize sameRight by using helper method to check Tree or False for right subtree
        return sameLeft and sameRight	#We return True or False if neither of is same or not the same respectively 