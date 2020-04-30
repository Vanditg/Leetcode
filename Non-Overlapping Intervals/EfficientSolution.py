##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 435
## Problem Name: Non-overlapping Intervals      
##===================================
#
#Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
#
#Example 1:
#
#Input: [[1,2],[2,3],[3,4],[1,3]]
#Output: 1
#Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
#Example 2:
#
#Input: [[1,2],[1,2],[1,2]]
#Output: 2
#Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.
#Example 3:
#
#Input: [[1,2],[2,3]]
#Output: 0
#Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

class Solution: 
    def eraseOverlappingIntervals(self, intervals):
        if intervals == []:	#Condition-check: If intervals is empty
            return 0	#We'll return 0 as no overlapping interval presenet
        intervals.sort(key = lambda x:x[1])	#Sort intervals list by 2nd element 
        tmp = 0	#Initialize our tmp counter 
        end = intervals[0][0]	#Initialize end which will be first element of the first sublist
        for i in intervals:	#Loop through intervals
            start = i[0]	#Initialize start which will be first element in every sublist
            if start < end:	#Condition-check: If start is less than end 
                tmp += 1	#Then we'll increase out tmp counter as we encounter the overlapping list
            else:	#Condition-check: Else
                end = i[1]	#We'll update the end by 2nd element of ith sublist
        return tmp	#We'll return tmp counter