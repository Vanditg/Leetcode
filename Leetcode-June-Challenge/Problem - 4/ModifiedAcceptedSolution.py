##==================================
## Leetcode June Challenge 
## Username: Vanditg
## Year: 2020
## Problem:4
## Problem Name: Reverse String
##===================================
#
#Write a function that reverses a string. The input string is given as an array of characters char[].
#
#Do not allocate extra space for another array, 
#you must do this by modifying the input array in-place with O(1) extra memory.
#
#You may assume all the characters consist of printable ascii characters.
#
#Example 1:
#
#Input: ["h","e","l","l","o"]
#Output: ["o","l","l","e","h"]
#Example 2:
#
#Input: ["H","a","n","n","a","h"]
#Output: ["h","a","n","n","a","H"]
class Solution:
    def reverseString(self, s):
        l, r = 0, len(s)-1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1