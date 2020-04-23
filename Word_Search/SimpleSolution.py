##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 79
## Problem Name: Word Search      
##===================================
#
#Given a 2D board and a word, find if the word exists in the grid.
#
#The word can be constructed from letters of sequentially adjacent cell, 
#where "adjacent" cells are those horizontally or vertically neighboring. 
#The same letter cell may not be used more than once.
#
#Example:
#
#board =
#[
#  ['A','B','C','E'],
#  ['S','F','C','S'],
#  ['A','D','E','E']
#]
#
#Given word = "ABCCED", return true.
#Given word = "SEE", return true.
#Given word = "ABCB", return false.
class Solution:
    def exist(self, board, word):
        for i, r in enumerate(board):	#Loop through board
            for j, value in enumerate(r):	#Loop through r, row basically
                if value == word[0]:	#Condition-check: If we find the letter 
                    if self.dfs(i, j, 0, board, word)	#Condition-check: If by applying dfs we find the neighboring word 
                        return True	#We return True if find the word 
        return False	#Else We return false
    def dfs(self, i, j, index, board, word):	#Defining helper method dfs  
        if index == len(word):	#Condition-check: If index is equal to len(word)
            return True	#We return True
        if not (0 <= i < len(board) and 0 <= j < len(board[i])) or board[i][j] != word[index]:	#Condition-check
            return False	#We return false
        tmp = board[i][j]	#Initialize tmp board
        board[i][j] = '+'	#Update the value by '+'
        for nI, nJ in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):	#For neighboring elements
            if self.dfs(nI, nJ, index + 1, board, word):	#Condition-check: If by applying dfs we find the word
                return True	#We return True 
        board[i][j] = tmp	#Update board values by tmp
        return True	#We return True 