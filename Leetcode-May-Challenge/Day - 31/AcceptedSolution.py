##==================================
## Leetcode May Challenge 
## Username: Vanditg
## Year: 2020
## Problem: 31
## Problem Name: Edit Distance
##===================================
#
#Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.
#
#You have the following 3 operations permitted on a word:
#
#Insert a character
#Delete a character
#Replace a character
#Example 1:
#
#Input: word1 = "horse", word2 = "ros"
#Output: 3
#Explanation: 
#horse -> rorse (replace 'h' with 'r')
#rorse -> rose (remove 'r')
#rose -> ros (remove 'e')
#Example 2:
#
#Input: word1 = "intention", word2 = "execution"
#Output: 5
#Explanation: 
#intention -> inention (remove 't')
#inention -> enention (replace 'i' with 'e')
#enention -> exention (replace 'n' with 'x')
#exention -> exection (replace 'n' with 'c')
#exection -> execution (insert 'u')
class Solution:
    def minDistance(self, word1, word2):
        matrix = [[0 for j in range(len(word1) + 1)] for i in range(len(word2) + 1)]
        for i in range(len(word2) + 1):
            matrix[i][0] = i
        for j in range(len(word1) + 1):
            matrix[0][j] = j
        for i in range(1, len(word2) + 1):
            for j in range(1, len(word1) + 1):
                if word1[j - 1] == word2[i - 1]:
                    matrix[i][j] = matrix[i - 1][j - 1]
                else:
                    matrix[i][j] = min([matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1]]) + 1
        return matrix[len(word2)][len(word1)]