#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start

from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(0,len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         if (nums[i]+nums[j]) == target:
        #             return [i,j]
        d = {}
        for i in range(0,len(nums)):
            complement = target -nums[i]
            if complement in d:
                    return [d[complement],i]
            d[nums[i]] = i



        
# @lc code=end

