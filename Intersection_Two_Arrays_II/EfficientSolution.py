##==================================
## Leetcode
## Student: Vandit Jyotindra Gajjar
## Year: 2020
## Problem: 350
## Problem Name: Intersection of Two Arrays II          
##===================================
#
#Given two arrays, write a function to compute their intersection.
#
#Example 1:
#
#Input: nums1 = [1,2,2,1], nums2 = [2,2]
#Output: [2,2]
#Example 2:
#
#Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
#Output: [4,9]
#Note:
#
#Each element in the result should appear as many times as it shows in both arrays.
#The result can be in any order.
class Solution:
    def intersect(self, nums1, nums2): 
        i, j, tmp = 0, 0, []	#Initialize i, j, and tmp 
        nums1.sort(), nums2.sort()	#Sort nums1 and nums2
        while i < len(nums1) and j < len(nums2):	#Loop till condition reach
            if nums1[i] == nums2[j]:	#Condition-check: If nums1's i and nums2's j value is same 
                tmp.append(nums1[i])	#Then we append the value to tmp 
                i += 1	#Update i by increasing 1 
                j += 1	#Update j by increasing 1
            elif nums1[i] < nums2[j]:	#Condition-check: Elif nums1's i value is less than nums2's value
                i += 1	#Update i by increasing 1
            else:	#Condition-check:Else
                j += 1	#Update j by increasing 1
        return tmp	#Return updated tmp