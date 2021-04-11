class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head or not head.next:
            return head
        fake_head = ListNode(-1)
        fake_head.next = head
        tmp = fake_head
        while tmp.next and tmp.next.val < x:
            tmp = tmp.next
        border = tmp
        tmp = tmp.next
        while tmp and tmp.next:
            if tmp.next and tmp.next.val >= x:
                tmp = tmp.next
            else:
                temp = tmp.next
                tmp.next = temp.next
                temp.next = border.next
                border.next = temp
                border = border.next
        return fake_head.next


s = Solution()
head = ListNode(1)
head.next = ListNode(4)
head.next.next = ListNode(3)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(2)
temp = s.partition(head,3)
while temp:
    print(temp.val)
    temp = temp.next


