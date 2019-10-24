#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s;
        rows = ['']*min(numRows,len(s)) #创建min()个行
        curRow = 0 #当前行
        goDown = False #当前方向
        for c in s:
            rows[curRow] += c #字符c添加至对于行
            if curRow == 0 or curRow == numRows -1:
                goDown = not goDown
            if goDown:
                curRow+=1
            else:
                curRow+=-1
        res = ''.join(rows) #将列表中的字符串拼接为一个字符串
        return res



        
# @lc code=end

