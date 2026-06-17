# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # get the middle of the list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half
        prev, curr = None, slow.next
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node 

        i, j = head, prev
        while j:
            left_temp = i.next
            i.next = j
            i = left_temp
            right_temp = j.next
            j.next = i
            j = right_temp
        i.next = None
