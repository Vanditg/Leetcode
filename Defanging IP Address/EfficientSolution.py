##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 1108
## Problem Name: Defanging an IP Address
##===================================
#Given a non-negative integer num, return the number of steps to reduce it to zero. 
#
#If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.
#Example 1:
#
#Input: num = 14
#Output: 6
#Explanation: 
#Step 1) 14 is even; divide by 2 and obtain 7. 
#Step 2) 7 is odd; subtract 1 and obtain 6.
#Step 3) 6 is even; divide by 2 and obtain 3. 
#Step 4) 3 is odd; subtract 1 and obtain 2. 
#Step 5) 2 is even; divide by 2 and obtain 1. 
#Step 6) 1 is odd; subtract 1 and obtain 0.
#
#Example 2:
#
#Input: num = 8
#Output: 4
#Explanation: 
#Step 1) 8 is even; divide by 2 and obtain 4. 
#Step 2) 4 is even; divide by 2 and obtain 2. 
#Step 3) 2 is even; divide by 2 and obtain 1. 
#Step 4) 1 is odd; subtract 1 and obtain 0.
#
#Example 3:
#
#Input: num = 123
#Output: 12

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
