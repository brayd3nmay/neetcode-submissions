# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tracker = 0
        lazy_prev = None
        lazy = curr = head
        while curr:
            curr = curr.next
            tracker += 1
            if tracker > n:
                lazy_prev = lazy
                lazy = lazy.next
                tracker -= 1
        if lazy_prev:
            lazy_prev.next = lazy.next
            return head
        else:
            return lazy.next