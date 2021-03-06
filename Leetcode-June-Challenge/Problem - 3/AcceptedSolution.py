##==================================
## Leetcode June Challenge 
## Username: Vanditg
## Year: 2020
## Problem: 3
## Problem Name: Two City Scheduling
##===================================
#
#There are 2N people a company is planning to interview. 
#The cost of flying the i-th person to city A is costs[i][0], and the cost of flying the i-th person to city B is costs[i][1].
#
#Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.
#
#Example 1:
#
#Input: [[10,20],[30,200],[400,50],[30,20]]
#Output: 110
#Explanation: 
#The first person goes to city A for a cost of 10.
#The second person goes to city A for a cost of 30.
#The third person goes to city B for a cost of 50.
#The fourth person goes to city B for a cost of 20.
#
#The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.
class Solution: 
    def twoCitySchedCost(self, costs):
        cost = sorted(costs, key = lambda x:x[0] - x[1])	
        tmp = 0
        for i in range(len(costs)):
            if i < len(costs) / 2:
                tmp += cost[i][0]
            else:
                tmp += cost[i][1]
        return tmp