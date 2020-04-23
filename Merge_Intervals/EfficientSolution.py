##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 56
## Problem Name: Merge Intervals   
##===================================
#
#Given a collection of intervals, merge all overlapping intervals.
#
#Example 1:
#
#Input: [[1,3],[2,6],[8,10],[15,18]]
#Output: [[1,6],[8,10],[15,18]]
#Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
#
#Example 2:
#
#Input: [[1,4],[4,5]]
#Output: [[1,5]]
#Explanation: Intervals [1,4] and [4,5] are considered overlapping.
class Solution:
    def merge(self, intervals):
        intervals.sort(key = lambda x:x[0])	#Sort the intervals by 1st element in sublists 
        i = 1	#Initialize i
        while i < len(intervals):	Loop 
            if intervals[i][0] <= intervals[i-1][1]:	#Condition-check: If first element of 2nd list and last element of 1st list is less than or equal to zero
                intervals[i-1][0] = min(intervals[i-1][0], intervals[i][0])	#Update the lists 1st value by taking min from 1st and 2nd lists first element
                intervals[i-1][1] = max(intervals[i-1][1], intervals[i][1])	#Update the lists 2nd value by taking max from 1st and 2nd lists last element
                intervals.pop(i)	#Remove the 2nd list 
            else:	#Condition-check: Else
                i += 1	#Update i by 1 
        return intervals	#Return intervals at the end 