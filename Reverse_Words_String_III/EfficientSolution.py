##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 557
## Problem Name: Reverse Words in a String III
##===================================
#
#Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
#
#Example 1:
#Input: "Let's take LeetCode contest"
#Output: "s'teL ekat edoCteeL tsetnoc"
class Solution:
    def reverseWords(self, s):
        tmp = s.split()   #creating a tmp list and splitting the string
        for i in range(len(tmp))    #Loop through tmp
            tmp[i] = tmp[i][::-1]    #Reverse individual element
        newTmp = ' '.join(tmp)    #join the elements 
        return "{}".format(newTmp)    #Returning the output with double quotes. 
#Example:
#s = "Let's take LeetCode contest"
#tmp = ["Let's", 'take', 'LeetCode', 'contest']
#i = 0
#tmp[0] = s'teL
#i = 1
#tmp[1] = ekat
#i = 2
#tmp[2] = edoCteeL
#i = 3
#tmp[3] = tsetnoc
#newTmp = s'teL ekat edoCteeL tsetnoc
#output = "s'teL ekat edoCteeL tsetnoc"