# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        elif not list1:
            return list2
        elif not list2:
            return list1

        merged_head = merged_tail = ListNode()
        one_head, two_head = list1, list2
        while one_head and two_head:
            if one_head.val < two_head.val:
                merged_tail.next = one_head
                merged_tail = merged_tail.next
                one_head = one_head.next
            else:
                merged_tail.next = two_head 
                merged_tail = merged_tail.next
                two_head = two_head.next               

        if one_head:
            merged_tail.next = one_head
        elif two_head:
            merged_tail.next = two_head

        return merged_head.next