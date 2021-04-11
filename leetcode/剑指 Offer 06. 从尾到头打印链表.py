class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 暴力
    def reversePrint(self, head: ListNode):
        res = []
        while head:
            res.insert(0,head.val)
            head = head.next
        return res



