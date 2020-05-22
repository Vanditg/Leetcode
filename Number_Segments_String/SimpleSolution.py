##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 434
## Problem Name: Number of Segments in a String   
##===================================
#
#Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.
#
#Please note that the string does not contain any non-printable characters.
#
#Example:
#
#Input: "Hello, my name is John"
#Output: 5
class Solution:
    def countSegments(self, s):
        tmp = s.split()	#Initialize tmp which is a list of the non-space characters
        return len(tmp)	#We return the length of the list which whill be the number of segments