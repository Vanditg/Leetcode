##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 102
## Problem Name: Binary Tree Level Order Traversal 
##===================================
#
#Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
#
#For example:
#Given binary tree [3,9,20,null,null,15,7],
#    3
#   / \
#  9  20
#    /  \
#   15   7
#return its level order traversal as:
#[
#  [3],
#  [9,20],
#  [15,7]
#]
import queue
class Solution:
    def levelOrder(self, root):
        tmp = []	#Initialize tmp empty list
        q = queue.Queue()	#Initialize queue
        if root is None:	#Condition-check: If root is empty
            return None	#Return nothing 
        q.put(root)	#Put root in our queue
        while not q.empty():	#While queue is not empty
            array = []	#Initialize an empty array for levelorder nodes 
            size = q.qsize()	#Get the size of queue
            while size != 0:	#Loop till size gets zero
                curr = q.get()	#Initialize curr which takes the value we have put 
                array.append(curr.val)	#Append that curr's value in array
                if curr.left is not None:	#Condition-check: If we have left subtree or child 
                    q.put(curr.left)	#We simply add that curr's left in queue
                if curr.right is not None:	#Condition-check: If we have right subtree or child
                    q.put(curr.right)	#We simply add that curr's right in queue                  
                size -= 1	#Reduce size by 1 
            if len(array) != 0:	#Condition-check: If the array's length is not equal to zero 
                tmp.append(array)	#We append that array in our tmp array, which we'll return 
        return tmp	#Finally we'll return tmp
            