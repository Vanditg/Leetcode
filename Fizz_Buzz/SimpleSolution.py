##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 412
## Problem Name: Fizz Buzz        
##===================================
#Write a program that outputs the string representation of numbers from 1 to n.
#
#But for multiples of three it should output “Fizz” instead of the number and 
#for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.
#
#Example:
#
#n = 15,
#
#Return:
#[
#    "1",
#    "2",
#    "Fizz",
#    "4",
#    "Buzz",
#    "Fizz",
#    "7",
#    "8",
#    "Fizz",
#    "Buzz",
#    "11",
#    "Fizz",
#    "13",
#    "14",
#    "FizzBuzz"
#]
class Solution:
    def fizzBuzz(self, n):
        tmp = []	#Initialize empty tmp list
        for i in range(0, n):	#Loop through numbers 
            if (i+1) % 15 == 0:	#Condition-check: If number gives no remainder when divided by 15. 
                tmp.append("FizzBuzz")	#We append FizzBuzz
            elif (i+1) % 3 == 0:	#Condition-check: Elif number gives no remainder when divided by 3.
                tmp.append("Fizz")	#We append Fizz
            elif (i+1) % 5 == 0:	#Condition-check: Elif number gives no remainder when divided by 5.
                tmp.append("Buzz")	#We append Buzz
            else:	#Condition-check: Else
                tmp.append(str(i+1))	#We append number in string format
        return tmp	#We return tmp at the end