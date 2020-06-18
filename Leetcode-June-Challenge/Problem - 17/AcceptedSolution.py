##==================================
## Leetcode June Challenge 
## Username: Vanditg
## Year: 2020
## Problem: 17
## Problem Name: Surrounded Regions
##===================================
#
#Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
#
#A region is captured by flipping all 'O's into 'X's in that surrounded region.
#
#Example:
#
#X X X X
#X O O X
#X X O X
#X O X X
#After running your function, the board should be:
#
#X X X X
#X X X X
#X X X X
#X O X X
#Explanation:
#
#Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. 
#Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. 
#Two cells are connected if they are adjacent cells connected horizontally or vertically.
import collections

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        q = collections.deque()

        for i in xrange(len(board)):
            if board[i][0] == 'O':
                board[i][0] = 'V'
                q.append((i, 0))
            if board[i][len(board[0])-1] == 'O':
                board[i][len(board[0])-1] = 'V'
                q.append((i, len(board[0])-1))

        for j in xrange(1, len(board[0])-1):
            if board[0][j] == 'O':
                board[0][j] = 'V'
                q.append((0, j))
            if board[len(board)-1][j] == 'O':
                board[len(board)-1][j] = 'V'
                q.append((len(board)-1, j))

        while q:
            i, j = q.popleft()
            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= x < len(board) and 0 <= y < len(board[0]) and \
                   board[x][y] == 'O':
                    board[x][y] = 'V'
                    q.append((x, y))

        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if board[i][j] != 'V':
                    board[i][j] = 'X'
                else:
                    board[i][j] = 'O'