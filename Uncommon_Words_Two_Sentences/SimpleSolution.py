##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 884
## Problem Name: Uncommon Words from Two Sentences   
##===================================
#
#We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)
#
#A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
#
#Return a list of all uncommon words. 
#
#You may return the list in any order.
#
#Example 1:
#
#Input: A = "this apple is sweet", B = "this apple is sour"
#Output: ["sweet","sour"]
#
#Example 2:
#
#Input: A = "apple apple", B = "banana"
#Output: ["banana"]
import collections as c
class Solution:
    def uncommonFromSentences(self, A, B);
        count = c.Counter(A.split())	#Using Counter method to count the number of repeating words and mapp in key and value
        count += c.Counter(B.split())	#Using Counter method to count the number of words in B and map in key and value
        return [i for i in count if count[i] == 1]	#Return i if count has 1 value 