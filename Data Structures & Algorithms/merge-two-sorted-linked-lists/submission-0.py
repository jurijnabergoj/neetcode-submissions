# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        new_list = dummy
        curr_l1 = list1
        curr_l2 = list2

        while curr_l1 and curr_l2:
            if curr_l1.val <= curr_l2.val:
                min_node = curr_l1
                curr_l1 = curr_l1.next
            else:
                min_node = curr_l2
                curr_l2 = curr_l2.next
            new_list.next = min_node
            new_list = new_list.next
        if curr_l1:
            new_list.next = curr_l1
        else:
            new_list.next = curr_l2

        return dummy.next
        