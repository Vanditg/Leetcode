##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 1108
## Problem Name: Defanging an IP Address
##===================================
#Given a valid (IPv4) IP address, return a defanged version of that IP address.
#
#A defanged IP address replaces every period "." with "[.]".
#
#Example 1:
#
#Input: address = "1.1.1.1"
#Output: "1[.]1[.]1[.]1"
#Example 2:
#
#Input: address = "255.100.50.0"
#Output: "255[.]100[.]50[.]0"
#
#Constraints:
#
#The given address is a valid IPv4 address.

class Solution:

    def defangIPaddr(self, address):
	
        return address.replace(".", "[.]")

#We have a simple method in python for strings name - .replace, in which the specif character/string could be replaced. 
#i.e. str = "1, 2, 3" >> str.replace('2', '4') >> Output will be "1, 4, 3". 
