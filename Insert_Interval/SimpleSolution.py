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
        tmp = []	#Initialize tmp empty list
        for i in intervals:	#Loop through intervals list
            if newInterval[0] > i[1]:	#Condition-check: If newInterval's first element is greater than i's last element
                tmp.append(i)	#We append the i list to tmp 
            elif newInterval[1] < i[0]: #Condition-check: Elif newInterval's last element is less than i's first element
                tmp.append(newInterval)	#We append the newInterval list to tmp
                newInterval = i	#Update the newInterval to i 
            elif newInterval[0] <= i[1] or newInterval[1] >= i[0]:	Condition-check: Elif newInterval's first element is less than or equal to i's first element or newInterval's last element is greater or equal to i's first element
                newInterval = [min(newInterval[0], i[0]), max(i[1], newInterval[1])]	#Update the newInterval list by finding min and max from i's and newInterval's last and first element respectively 
        tmp.append(newInterval)	#Lastly append the newInterval to tmp list
        return tmp	#Return tmp at the end