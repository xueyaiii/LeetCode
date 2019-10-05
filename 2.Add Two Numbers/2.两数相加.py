#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start ca
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carried = 0
        head = curr = ListNode(-1)
        while l1 or l2 or carried:
            temp = carried
            if l1:
                temp += l1.val
                l1 = l1.next
            if l2:
                temp += l2.val
                l2 = l2.next
            curr.next =  ListNode(temp%10)
            curr = curr.next
            carried = temp//10                    
        return head.next
        
# @lc code=end