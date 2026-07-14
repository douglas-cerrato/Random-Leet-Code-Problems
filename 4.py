# Douglas Cerrato
# 7/14/26
# LeetCode Problem: Median of Two Sorted Arrays (Hard)
# https://leetcode.com/problems/median-of-two-sorted-arrays/


# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).
#
# Example 1:
#
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
#
# Example 2:
#
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1Len, nums2Len = len(nums1), len(nums2)
        if nums1Len == 1:
            nums1Median = nums1[0]
        else:
            nums1Median = (nums1[nums1Len // 2] * nums1[(nums1Len // 2) - 1]) if nums1Len % 2 == 0 else nums1[(nums1Len + 1) // 2]
        
        if nums2Len == 1:
            nums2Median = nums2[0]
        else:
            nums2Median = (nums2[nums2Len // 2] * nums2[(nums2Len // 2) - 1]) if nums2Len % 2 == 0 else nums2[(nums2Len + 1) // 2]
        print(f"nums1Median: {nums1Median}, nums2Median: {nums2Median}")



# So far in my code I am able to grab the median from both arrays based on if the array has either only one digit in the list, or if the list is an even or odd length
# I believe there is a way to insert the medians together to find the true middle without having to fully merge both lists
#
# I believe I can see if the length of the list is odd or even, and find where the median is placed on that list, and do the calculations between both lists to see if 
# one of the medians would be in the middle of the two medians in another even list of if theyre both odd and it would make a new even list therefore we would just get 
# the median of both medians from both lists
