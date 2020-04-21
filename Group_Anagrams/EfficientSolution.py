##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 49
## Problem Name: Group Anagrams    
##===================================
#
#Given an array of strings, group anagrams together.
#
#Example:
#
#Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
#Output:
#[
#  ["ate","eat","tea"],
#  ["nat","tan"],
#  ["bat"]
#]
class Solution:
    def groupAnagrams(self, strs):
        tmp = dict()	#Initialize tmp empty dictionary
        for word in strs:	#Loop through strs list
            sortWord = "".join(sorted(word))	#Initialize sortWord which will sort the word letters and return in a string format
            if sortWord in dict:	#Condition-check:If sortWord is in dictionary 
                tmp[sortWord].append(word)	#We'll append the word in sortWord key
            else:	#Condition-check: Else
                tmp[sortWord] = [word]	#We'll make a new key and add value as a list
        anagrams = []	#Initialize anagrams empty list which we'll return
        for i in tmp.values():	#Loop through tmp values 
            anagrams.append(i)	#Append it to the anagrams list
        return anagrams	#Return anagrams list 
         