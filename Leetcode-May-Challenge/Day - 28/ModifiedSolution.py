##==================================
## Leetcode May Challenge 
## Username: Vanditg
## Year: 2020
## Problem: 28
## Problem Name: Counting Bits
##===================================
#
#Given a non negative integer number num. 
#For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary 
#representation and return them as an array.
#
#Example 1:
#
#Input: 2
#Output: [0,1,1]
#Example 2:
#
#Input: 5
#Output: [0,1,1,2,1,2]
class Solution:
    def countBits(self, num):
        tmp = []	#Initialize tmp empty list 
        for i in range(0, num+1):	#Loop through the num range 
            binary = bin(i).replace('0b', '')	#Initialize binary and convert the decimal to binary
            def countOne(n):	#Defining countOne helper method  
                count = 0	#Initialize count
                for i in str(n):	#Loop through str
                    if i == '1':	#Condition-check: If string element is 1 
                        count += 1	#Update the count 
                return count	#We return the count
            tmp.append(tmpBinary)	#Append the tmpBinary into tmp list 
        return tmp	#We return tmp list 