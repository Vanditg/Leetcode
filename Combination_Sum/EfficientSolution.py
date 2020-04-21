##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 39
## Problem Name: Combination Sum  
##===================================
#
#Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.
#
#The same repeated number may be chosen from candidates unlimited number of times.
#
#Note:
#
#All numbers (including target) will be positive integers.
#The solution set must not contain duplicate combinations.
#Example 1:
#
#Input: candidates = [2,3,6,7], target = 7,
#A solution set is:
#[
#  [7],
#  [2,2,3]
#]
#Example 2:
#
#Input: candidates = [2,3,5], target = 8,
#A solution set is:
#[
#  [2,2,2,2],
#  [2,3,3],
#  [3,5]
#]
class Solution:
    def combinationSum(self, candidates, target):
        if not candidates:	#Condition-check: If candidates list is empty 
            return None	#Return None  
        tmp = []	#Initialize tmp empty list
        element = sorted(candidates)	#Initialize element list and sort the candidates list
        def search(t, list, index):	#Defining method search
            if t == 0:	#Condition-check: If t == 0 
                tmp.append(list)	#Append the list in tmp
            for i in range(index, len(element)):	#Loop through index to len(element)
                if t - element[i] < 0:	#Condition-check: If t - element[i] values is less tahn 0
                    break	#Break the loop
                search(t - element[i], list + [element[i]], i)	#Use Recursion  
        search(target, [], 0)	#Use Recursion
		return tmp	#Return tmp list with possible combination sum
 