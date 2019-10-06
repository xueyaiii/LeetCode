### 题目
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
**示例：**
```
输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
```
### 题目解析
定义一个字典freq，存储字符和位置的映射关系
维护一个滑动窗口res，res的长度就是没有重复的子串的字符个数
- 首先初始化字典freq，值全为0，表示所有字符均没重复，l,r为res的左右边界
- 只要l < len(s),进行循环，若如果当前遍历到的字符从未出现过，那么，此时，当前遍历的字符要标记为出现，并且扩大右边界
- 当前遍历到的字符出现过，则出现的字符要标记为未出现，同时左边界向右移动，然后继续观察当前遍历到的字符
- 每次循环都要更新res，最后返回res