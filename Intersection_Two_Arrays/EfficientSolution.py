##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 349
## Problem Name: Intersection of Two Arrays     
##===================================
#Given two arrays, write a function to compute their intersection.
#
#Example 1:
#
#Input: nums1 = [1,2,2,1], nums2 = [2,2]
#Output: [2]
#
#Example 2:
#
#Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
#Output: [9,4]
class Solution:
    def intersection(self, nums1, nums2):
        set1 = set(nums1)	#Type conversion list to set
        set2 = set(nums2)	#Type conversion list to set
        #print(set1)
        #print(set2)
        if len(set1) < len(set2):	#Condition-check: if set1's length is less than set2 
            return self.s_intersection(set1, set2)	#We return helper method starts from set1 to set2
        else:	#Condition-check: Else 
            return self.s_intersection(set2, set1)	#We return helper method starts from set2 to set1	
    def s_intersection(self, nums1, nums2):	#Defining helper method takes two list as input
        return [i for i in set1 if i in set2]	#Returns the list in which element i is in set1 and set2 or vice-verca.