# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        res_start = res
        increment = 0

        while l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            if l1_val + l2_val + increment > 9:
                res.val = (l1_val + l2_val + increment) % 10
                increment = 1
            else:
                res.val = (l1_val + l2_val + increment)
                increment = 0
            
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            if l1 or l2 or increment == 1:
                res.next = ListNode()
                res = res.next

        if increment == 1:
            res.val = 1
        return res_start
            