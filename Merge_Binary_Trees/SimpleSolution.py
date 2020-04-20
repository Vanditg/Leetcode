##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 617
## Problem Name: Merge Two Binary Tress   
##===================================
#
#Given two binary trees and imagine that when you put one of them to cover the other, 
#some nodes of the two trees are overlapped while the others are not.

#You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, 
#then sum node values up as the new value of the merged node. 
#Otherwise, the NOT null node will be used as the node of new tree.

class Solution:
    def mergeTrees(self, t1, t2):
        if t1 is None:	#Condition-check: If tree 1 is null, we simply merge/add tree 2.
            return t2
        if t2 is None:	#Condition-check: If tree 2 is null, we simply merge/add tree 1. 
            return t1
        t1.val = t1.val + t2.val	#Now, we add root values and stores in tree 1's root. 'We'll return tree 1 at the end.'
        t1.left = self.mergeTrees(t1.left, t2.left)	#Recursive call for left child 
        t1.right = self.mergeTrees(t1.right, t2.right)	#Recursive call for right child
        return t1	#Finally, we'll return t1. 