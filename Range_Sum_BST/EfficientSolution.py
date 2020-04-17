##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 938
## Problem Name:  Range Sum of BST   
##===================================
#
#Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

#The binary search tree is guaranteed to have unique values.
#
#Example 1:
#
#Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
#Output: 32
#
#Example 2:
#
#Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
#Output: 23
class Solution;
    def rangeSumBST(self, root, L, R):
        return self._rangeSumBST(root, L, R, 0)	#Calling our helper method 
    def _rangeSumBST(self, curr_node, L, R, Sum):	#Defining our helper method
        if curr_node is None:	#Condition-check: If curr_node is empty
            return Sum	#We return Sum 
        if L <= curr_node.val <= R: #Condition-check: If our curr_node.val is in the range of [L, R]
            Sum += curr_node.val	#Sum is Sum + curr_node.val 
            Sum = self._rangeSumBST(curr_node.left, L, R, Sum)	#Calling helper method 
            Sum = self._rangeSumBST(curr_node.right, L, R, Sum)	#Calling helper method
        if curr_node.val < L:	#Condition-check: if curr_node.val is less than L
            Sum = self._rangeSumBST(curr_node.right, L, R, Sum)	#Calling helper method 
        if curr_node.val > R:	#Condition-check: if curr_node.val is greater than R
            Sum = self._rangeSumBST(curr_node.left, L, R, Sum)	#Calling helper method
    return Sum	#Return total Sum at the end. 