##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 57
## Problem Name: Insert Interval   
##===================================
#Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
#
#You may assume that the intervals were initially sorted according to their start times.
#
#Example 1:
#
#Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
#Output: [[1,5],[6,9]]
#
#Example 2:
#
#Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
#Output: [[1,2],[3,10],[12,16]]
#Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
class Solution:
    def insert(self, intervals, newInterval):
        l, r = [], []	#Initialize l and r empty list
        intervals.sort(key = lambda x:x[0])	#Sort the intervals by its 1st element in sublists 
        for i in intervals:	#Loop through intervals
            if i[1] < newInterval[0]:	#Condition-check: If i's last element is less than newInterval's first element
                l.append(i)	#We append i in l 
            elif i[0] > newInterval[1]: #Condition-check: Elif i's first element is greater than newInterval's last element
                r.append(i)	#We append i in r  
            else:
                newInterval = [min(newInterval[0], i[0]), max(newInterval[1], i[1])]	#Update the newInterval by taking min and max of newInterval and i's first and last element resepectively 
        return l + [newInterval] + r	#Return the final list