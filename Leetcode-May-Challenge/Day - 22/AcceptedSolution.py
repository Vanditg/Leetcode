##==================================
## Leetcode May Challenge 
## Username: Vanditg
## Year: 2020
## Problem: 22
## Problem Name: Sort Characters By Frequency
##===================================
#
#Given a string, sort it in decreasing order based on the frequency of characters.
#
#Example 1:
#
#Input:
#"tree"
#
#Output:
#"eert"
#
#Explanation:
#'e' appears twice while 'r' and 't' both appear once.
#So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
#Example 2:
#
#Input:
#"cccaaa"
#
#Output:
#"cccaaa"
#
#Explanation:
#Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
#Note that "cacaca" is incorrect, as the same characters must be together.
#Example 3:
#
#Input:
#"Aabb"
#
#Output:
#"bbAa"
#
#Explanation:
#"bbaA" is also a valid answer, but "Aabb" is incorrect.
#Note that 'A' and 'a' are treated as two different characters.
class Solution:
    def frequencySort(self, s):
        tmp, res = {}, ''	#Initialize tmp dictionary and res empty string 
        for i in s:	#Loop through string s 
            if i in tmp:	#Condition-check: If char i is in tmp dictionary
                tmp[i] += 1	#We update the value of that character
            else:	#Condition-check: Else
                tmp[i] = 1	#We update that character in dictionary
        s = sorted(tmp, key = lambda i: tmp[i], reverse = True)	#We sort the dictionary's key value in reverse order based on the frequency 
        for char in s:	#Loop through our sorted tring 
            res += char * tmp[char]	#We multiply our character with the frequency and update in the string s 
        return res	#We return string res 