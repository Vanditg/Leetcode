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
	
        string = [] #[]
		
        for character in address:
			
            if character == '.':   #1.1.1.1 if . is in address
				
                string.append("[.]")    #we'll append it by ["[.]"]
			
            else:
				
                string.append(character) #Or we'll append it with characters
		
        return "".join(string)  #Finally we'll join the string which will give "1[.]1[.]1[.]1"
.
#Initialize empty string
#For every character in our IP Address, we will check with the condition that if "." is in the address, we'll simply replace with our given value which is "[.]", 
#otherwise, we'll append remaining address. Lastly, we'll simply join all the character in string. 
