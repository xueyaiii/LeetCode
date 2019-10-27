#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        flag = True
        s = []
        if x < 0:
            x = -x
            flag = not flag
        s=list(str(x))
        lens = len(s) - 1
        if s == list('0'):
            return ''.join(s)
        while(s[lens]=='0'):
            s= s[:lens]
            lens-=1
        s=list(reversed(s))
        if flag:
            result=int(''.join(s))
        else:
            result=int('-'+''.join(s))
        if result<=pow(2, 31)-1 and result>=(-1)*pow(2, 31):
            return result
        else:
            return 0





        
# @lc code=end

