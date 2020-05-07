##==================================
## Leetcode May Challenge 
## Username: Vanditg
## Year: 2020
## Problem: 7
## Problem Name: Cousins in Binary Tree 
##===================================
#
#In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.
#
#Two nodes of a binary tree are cousins if they have the same depth, but have different parents.
#
#We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.
#
#Return true if and only if the nodes corresponding to the values x and y are cousins.
#
#Example 1:
#
#Input: root = [1,2,3,4], x = 4, y = 3
#Output: false
#Example 2:
#
#Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
#Output: true
#Example 3:
#
#Input: root = [1,2,3,null,4], x = 2, y = 3
#Output: false
class Solution:
    def isCousins(self, root, x, y):
        tmpX, tmpY, lvl = [], [], 0	#Initialize tmpX, tmpY, and lvl
        parent = None	#Initialize parent
        if root is None:	#Condition-check: If root is None
            return False	#We return False 
        def DFS(root, x, y, lvl, parent, tmpX, tmpY):	#Defining DFS Helper method 
            if root is None:	#Condition-check: If root is None
				return None		#Condition-check: Return none 
            if root.val == x:	#Condition-check: If root's val is x then 
                tmpX.append((lvl, parent))	#We append the lvl and parent in tmpX
            if root.val == y:	#Condition-check: If root's val is y then 
                tmpY.append((lvl, parent))	#We append the lvl and parent in tmpY
            DFS(root.left, x, y, lvl + 1, root, tmpX, tmpY)	#We use recursion for the left subtree and increase the lvl by 1
            DFS(root.right, x, y, lvl + 1, root, tmpX, tmpY)	#We use recursion for the right subtree and increase the lvl by 1 
        DFS(root, x, y, 0, None, tmpX, tmpY)	#We use helper method DFS in our root 
        return tmpX[0][0] == tmpY[0][0] and tmpX[0][1] != tmpY[0][1]	#We return True or False based on the conditions if the depth is same and parent should different