##==================================
## Leetcode June Challenge 
## Username: Vanditg
## Year: 2020
## Problem: 14
## Problem Name: Cheapest Flights Within K Stops
##===================================
#
#There are n cities connected by m flights. Each flight starts from city u and arrives at v with a price w.
#
#Now given all the cities and flights, together with starting city src and the destination dst, 
#your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.
#
#Example 1:
#Input: 
#n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
#src = 0, dst = 2, k = 1
#Output: 200
#Explanation: 
#The graph looks like this:
#
#The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.
#Example 2:
#Input: 
#n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
#src = 0, dst = 2, k = 0
#Output: 500
#Explanation: 
#The graph looks like this:
#
#The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.
class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        if src == dst:
            return 0
        location, value = collections.defaultdict(list), collections.defaultdict(lambda: float('inf'))
        
        for a, b, c in flights:
            location[a] += [(b, c)]
        d = [(src, -1, 0)]
        
        while d:
            pos, k, cost = d.pop(0)
            if pos == dst or k == K:
                continue
            for neighbor, c in location[pos]:
                if cost + c >= value[neighbor]:
                    continue 
                else:
                    value[neighbor] = cost + c
                    d += [(neighbor, k + 1, cost + c)]
        if value[dst] < float('inf'):
            return value[dst]
        else:
            return -1