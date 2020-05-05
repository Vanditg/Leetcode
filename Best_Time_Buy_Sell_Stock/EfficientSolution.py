##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 121
## Problem Name: Best Time to Buy and Sell Stock          
##===================================
#
#Say you have an array for which the ith element is the price of a given stock on day i.
#
#If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
#
#Note that you cannot sell a stock before you buy one.
#
#Example 1:
#
#Input: [7,1,5,3,6,4]
#Output: 5
#Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#             Not 7-1 = 6, as selling price needs to be larger than buying price.
#Example 2:
#
#Input: [7,6,4,3,1]
#Output: 0
#Explanation: In this case, no transaction is done, i.e. max profit = 0.
class Solution:
    def maxProfits(self, prices):
        if prices == []:	#Condition-check: If prices is empty list 
            return 0	#Return 0 
        tmp, min = 0, prices[0]	#Initialize tmp and min which is 0 and first element of the list respectively
        for i in range(1, len(prices)):	#Loop through prices  
            if prices[i] < min:	#Condition-check: If prices is less thatn min  
                min = prices[i]	#We update min by set to prices[i]
            else:	#Condition-check: Else 
                tmp = max(tmp, prices[i] - min)	#Update tmp by taking max of tmp and difference of prices[i] and min 
        return tmp	#We return tmp				
        