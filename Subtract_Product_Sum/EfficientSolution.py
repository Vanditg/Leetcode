##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 1281
## Problem Name: Subtract the Product and Sum of Digits of an Integer
##===================================
#
#Given an integer number n, return the difference between the product of its digits and the sum of its digits.
#
#Example 1:
#
#Input: n = 234
#Output: 15 
#Explanation: 
#Product of digits = 2 * 3 * 4 = 24 
#Sum of digits = 2 + 3 + 4 = 9 
#Result = 24 - 9 = 15
#
#Example 2:
#
#Input: n = 4421
#Output: 21
#Explanation: 
#Product of digits = 4 * 4 * 2 * 1 = 32 
#Sum of digits = 4 + 4 + 2 + 1 = 11 
#Result = 32 - 11 = 21

class Solution:
    def subtractProductAndSum(self, number):
        splitNumber = [int(i) for i in str(number)]    #Creating the list of splitNumber. 
        #print(splitNumber)
        product, Sum = 1, 0    #Initialize product and sum tuple. 
        
        for i in range(len(splitNumber)):    #Loop through list
            product *= splitNumber[i]     #Product for every ith index in the list.
            #print(product)
        for j in range(len(splitNumber)):    #Loop through list
            Sum += splitNumber[j]     #Sum for every ith index in the list
            #print(Sum)
        return product - Sum  #Return result product - sum. 

#Example. 
#Number = 234 
#splitNumber = [2, 3, 4]
#Product, Sum = 1, 0
#i = 0 >> product = product * splitNumber[0] >> 1 * 2
#i = 1 >> product = product * splitNumber[0] * splitNumber [1] >> 1 * 2 * 3
#i = 2 >> product = product * splitNumber[0] * splitNumber[1] *splitNumber[2] >> 1 * 2 * 3 * 4 = 24
#j = 0 >> Sum = Sum + splitNumber[0] >> 0 + 2
#j = 1 >> Sum = Sum + splitNumber[0] + splitNumber[1] >> 0 + 2 + 3
#j = 2 >> Sum = Sum + splitNumber[0] + splitNumber[1] + splitNumber[2] >> 0 + 2 + 3 + 4 = 9
#product - Sum = 24 - 9 = 15