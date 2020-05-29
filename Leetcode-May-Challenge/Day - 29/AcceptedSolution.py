##==================================
## Leetcode May Challenge 
## Username: Vanditg
## Year: 2020
## Problem: 29
## Problem Name: Course Schedule
##===================================
#
#There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.
#
#Some courses may have prerequisites, for example to take course 0 you have to first take course 1, 
#which is expressed as a pair: [0,1]
#
#Given the total number of courses and a list of prerequisite pairs, 
#is it possible for you to finish all courses?
#
#Example 1:
#
#Input: numCourses = 2, prerequisites = [[1,0]]
#Output: true
#Explanation: There are a total of 2 courses to take. 
#             To take course 1 you should have finished course 0. So it is possible.
#Example 2:
#
#Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
#Output: false
#Explanation: There are a total of 2 courses to take. 
#             To take course 1 you should have finished course 0, and to take course 0 you should
#             also have finished course 1. So it is impossible.
import collections as c 
class Solution:
    def canFinish(self, numCourses, prerequisites):
        In, out = c.defaultdict(set), c.defaultdict(set)
        for a, b in prerequisites:
            out[b].add(a)
            In[a].add(b)
        delete = 0
        tmp = []
        for i in range(numCourses):
            if not In[i]:
                tmp.append(i)
                delete += 1
        while tmp:
            node = tmp.pop()
            for x in out[node]:
                In[x].remove(node)
                if not In[x]:
                    tmp.append(x)
                    delete += 1
        return delete == numCourses