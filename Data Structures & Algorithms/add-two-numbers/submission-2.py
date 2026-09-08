# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res_start = ListNode()
        curr = res_start
        increment = 0

        while l1 or l2 or increment:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            new_val = l1_val + l2_val + increment
            increment = new_val // 10
            new_val = new_val % 10
            curr.next = ListNode(new_val)

            if l1: l1 = l1.next
            if l2: l2 = l2.next
            curr = curr.next

        return res_start.next
            