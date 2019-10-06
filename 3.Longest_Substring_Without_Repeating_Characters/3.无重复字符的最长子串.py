#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = {}
        l = 0
        r = 0
        res = 0
        for i in range(256):
            freq[i] = 0
        while l < len(s):
            if r < len(s) and freq[ord(s[r])] == 0:
                freq[ord(s[r])] = freq[ord(s[r])] + 1
                r = r + 1
            else:
                freq[ord(s[l])] = freq[ord(s[l])] - 1
                l = l + 1
            res = max(res,r-l)
        return res



# @lc code=end

