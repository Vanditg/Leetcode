##==================================
## Leetcode May Challenge 
## Username: Vanditg
## Year: 2020
## Problem: 17
## Problem Name: Find All Anagrams in a String
##===================================
#
#Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
#
#Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
#
#The order of output does not matter.
#
#Example 1:
#
#Input:
#s: "cbaebabacd" p: "abc"
#
#Output:
#[0, 6]
#
#Explanation:
#The substring with start index = 0 is "cba", which is an anagram of "abc".
#The substring with start index = 6 is "bac", which is an anagram of "abc".
#Example 2:
#
#Input:
#s: "abab" p: "ab"
#
#Output:
#[0, 1, 2]
#
#Explanation:
#The substring with start index = 0 is "ab", which is an anagram of "ab".
#The substring with start index = 1 is "ba", which is an anagram of "ab".
#The substring with start index = 2 is "ab", which is an anagram of "ab".
from collections import Counter as c	#Import Counter module 
class Solution:
    def findAnagrams(self, s, p):
        lenS, lenP = len(s), len(p)	#Initialize lenS and lenP
        if lenS < lenP:	#Condition-check: If lenS is smaller then lenP 
            return []	#Return empty list 
        tmp = []	#Initialize tmp 
        countS, countP = c(), c(p)	#Initialize countP and countS
        for i in range(lenS):	#Loop through lenS
            countS[s[i]] += 1	#Update countS 
		    if i >= lenP:	#Condition-check: If i is greater or equal to lenP
                if countS[s[i - lenP]] == 1:	#Condition-check: If s[i - lenP] in the countS is 1 
                    del countS[s[i - lenP]]	#We delete that key and value 
                else:	#Condition-check: Else 
                    countS[s[i - lenP]] -= 1	#Update the value by decreasing 1 in the key of s[i - lenP] of countS
            if countP == countS:	#Condition-check: If the dictionary will have the same key value pair 
                tmp.append(i - lenP + 1)	#Append the value in tmp list 
        return tmp	#We return tmp at the end. 