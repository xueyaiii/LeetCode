#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个有序数组的中位数
#

# @lc code=start
from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = nums1 + nums2
        nums3.sort()
        length = len(nums3)
        if length%2 == 0:
            return (nums3[length//2] + nums3[length//2 - 1])/2
        else:
            return nums3[length//2] 
# @lc code=end

