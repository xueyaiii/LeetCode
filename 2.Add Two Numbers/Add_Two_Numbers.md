### 题目
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

**示例：**
```
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
```
### 题目解析
- 新增一个头结点为-1的链表作为输出链表
- carried保存进位，只要l1与l2与carried有一个不为空，就将`l1.val`与`l2.val`与`carried`相加
- 最后处理相加的和，模10后加到新链表，整除10得到的数赋给carried
- 时间复杂度：$O(n)$ 空间复杂度：$O(n)$

**注：**
- 考虑l1与l2不等长
- 未在while循环判断carried,导致l1与l2结点处理完后，产生的进位不能有效加到新的链表