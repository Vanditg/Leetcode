##==================================
## Leetcode May Challenge 
## Username: Vanditg
## Year: 2020
## Problem: 27
## Problem Name: Possible Bipartition
##===================================
#
#Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.
#
#Each person may dislike some other people, and they should not go into the same group. 
#
#Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.
#
#Return true if and only if it is possible to split everyone into two groups in this way.
#
#Example 1:
#
#Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
#Output: true
#Explanation: group1 [1,4], group2 [2,3]
#Example 2:
#
#Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
#Output: false
#Example 3:
#
#Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
#Output: false
class Solution:
    def possibleBipartition(self, N, dislikes):
        tmp = {}
        for dislike in dislikes:
            if dislike[0] in tmp:
                tmp[dislike[0]].add(dislike[1])
            else:
                tmp[dislike[0]] = set([dislike[1]])
            if dislike[1] in tmp:
                tmp[dislike[1]].add(dislike[0])
            else:
                tmp[dislike[1]] = set([dislike[0]])
        
        lookup = {}
        for i in range(1, N+1):
            if i not in lookup:
                lookup[i] = 0
                stack = [i]
                while stack:
                    a = stack.pop()
                    if a in tmp:
                        for b in tmp[a]:
                            if b in lookup:
                                if lookup[a] == lookup[b]:
                                    return False
                            else:
                                lookup[b] = (lookup[a]+1)%2
                                stack.append(b)
        return True
        