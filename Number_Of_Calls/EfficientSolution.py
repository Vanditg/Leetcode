##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 933
## Problem Name: Number of Recent Calls  
##===================================
#Write a class RecentCounter to count recent requests.
#It has only one method: ping(int t), where t represents some time in milliseconds.
#Return the number of pings that have been made from 3000 milliseconds ago until now.
#Any ping with time in [t - 3000, t] will count, including the current ping.
#It is guaranteed that every call to ping uses a strictly larger value of t than before.
#
#Example 1:
#
#Input: inputs = ["RecentCounter","ping","ping","ping","ping"], inputs = [[],[1],[100],[3001],[3002]]
#Output: [null,1,2,3,3]
import collections

class Solution:
    def __init__(self):
        self.q = collections.deque()	#Initialize the constructor 
    def ping(self, t):
        self.q.append(t)	#Append time in q
        while self.q[0] < t - 3000: 	#loop till we reach the condition
            self.q.popleft()	#Pol left in q.
    return len(self.q)	#Return length at the end.