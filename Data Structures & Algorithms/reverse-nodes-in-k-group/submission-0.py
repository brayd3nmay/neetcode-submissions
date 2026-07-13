# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        reversed_head = None
        prev_group_tail = next_group_head = None
        curr = head
        while True:
            curr_group_tail = self.nextKthNode(curr, k - 1)
            if not curr_group_tail:
                if prev_group_tail:
                    prev_group_tail.next = curr
                break
            next_group_head = curr_group_tail.next
            curr_group_tail.next = None

            curr_group_tail = curr
            if prev_group_tail:
                prev_group_tail.next = self.reverseLinkedList(curr)
            else:
                reversed_head = self.reverseLinkedList(curr)

            prev_group_tail = curr_group_tail
            curr = next_group_head

        return reversed_head

    def nextKthNode(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        kth_node = head
        while kth_node and k:
            kth_node = kth_node.next
            k -= 1
        return kth_node

    def reverseLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
