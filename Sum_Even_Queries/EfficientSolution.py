##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 985
## Problem Name: Sum of Even Numbers After Queries    
##===================================
#
#We have an array A of integers, and an array queries of queries.
#
#For the i-th query val = queries[i][0], index = queries[i][1], we add val to A[index].  Then, the answer to the i-th query is the sum of the even values of A.
#
#(Here, the given index = queries[i][1] is a 0-based index, and each query permanently modifies the array A.)
#
#Return the answer to all queries.  Your answer array should have answer[i] as the answer to the i-th query.
#
#Example 1:
#
#Input: A = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]]
#Output: [8,6,2,4]
#Explanation: 
#At the beginning, the array is [1,2,3,4].
#After adding 1 to A[0], the array is [2,2,3,4], and the sum of even values is 2 + 2 + 4 = 8.
#After adding -3 to A[1], the array is [2,-1,3,4], and the sum of even values is 2 + 4 = 6.
#After adding -4 to A[0], the array is [-2,-1,3,4], and the sum of even values is -2 + 4 = 2.
#After adding 2 to A[3], the array is [-2,-1,3,6], and the sum of even values is -2 + 6 = 4.
class Solution:
    def sumEvenAfterQueries(self, A, queries):
        total = sum(i for i in A if i % 2 == 0)	#Calculating sum of even values and store in total.
        answer = []	#Creating empty list answer which we'll return 
        for i, j in queries:	#Loop through queries 
            if A[j] % 2 == 0:	#Condition-check: If given value of index's for A given no remainder after dividing by 2
                total = total - A[j]	#Our total will be total - A[j]
            A[j] += i	#Add i value to A[j]
		    if A[j] % 2 == 0:	#Condition-check: If given value of index's for A given no remainder after dividing by 2
                total = total + A[j]	#total will be total + A[j]
            answer.append(total)	#Append total to answer
        return answer	#Return answer at the end. 