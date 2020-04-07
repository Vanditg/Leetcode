##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 771
## Problem Name: Jewels and Stones
##===================================
#
#You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  
#
#Each character in S is a type of stone you have. You want to know how many of the stones you have are also jewels.
#
#The letters in J are guaranteed distinct, and all characters in J and S are letters. 
#
#Letters are case sensitive, so "a" is considered a different type of stone from "A".
#
#Example 1:
#
#Input: J = "aA", S = "aAAbbbb"
#Output: 3
#
#Example 2:
#
#Input: J = "z", S = "ZZ"
#Output: 0

class Solution:
    def numJewelsInStone(self, Jewels, Stones):
        JewelsList = []    #Initialize our empty JewelsList.
        Number = 0    #Initialize our counter number.
		
        for i in range(len(Jewels)):    #Loop through Jewels
            JewelsList.append(Jewels[i])    #We'll append Jewels[i] in our JewelsList
        for j in range(len(Stones)):    #Loop through Stones
            if Stones[j] in JewelsList:    #Condition-check - if Stone is in JewelsList
                Number += 1    #We'll update our number counter. [Condition enter]
        return Number    #Finally, we'll return our counter Number.

#Example 1, Jewels = "z", Stones = "ZZ"
#JewelsList = []
#Number = 0
#i = 0; 
#JewelsList = ["z"] Exit the loop as Jewels has one string character. 
#j = 0;
#Condition-check Stones[0] = "Z" is not in JewelsList, we fail the condition-check
#j = 1; 
#Condition-check Stones[1] = "Z" is not in JewelsList, we fail the condition-check, exit the loop. 
#Return the counter Number which is Zero. 
#Number = 0