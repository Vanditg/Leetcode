##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 101
## Problem Name: Symmetric Tree            
##===================================
#
#Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
#
#For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
#
#    1
#   / \
#  2   2
# / \ / \
#3  4 4  3
# 
#But the following [1,2,2,null,3,null,3] is not:
#
#    1
#   / \
#  2   2
#   \   \
#   3    3
Class Solution:
    def isSymmetric(self, root):
        if root is None:	#Condition-check: If root is empty
            return True	#Return True 
        def symmetric(left, right):	#Defining helper function symmetric
            if left and right:	#Condition-check: If left and right is not None
                return left.val == right.val and symmetric(left.left, right.right) and symmetric(left.right, right.left)	#We return True or false based on the conditions 
                #(i)  If left and right values are same 
                #(ii) If left.left and right.right values are same 
                #(iii)If left.right and right.left values are same 
            return left == right	#Return True or False based on conditions
        return symmetric(root.left, root.right)	#Return true or false using helper function