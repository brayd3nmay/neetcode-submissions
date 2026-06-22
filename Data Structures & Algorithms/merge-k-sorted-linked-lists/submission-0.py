# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        list_map = {} # list index: head of that list
        for i, head in enumerate(lists):
            if head:
                list_map[i] = head

        dummy = tail = ListNode()
        while list_map:
            list_idx = min(list_map, key=lambda i: list_map[i].val)
            tail.next = list_map[list_idx]
            tail = tail.next

            list_map[list_idx] = list_map[list_idx].next
            if list_map[list_idx] == None:
                del list_map[list_idx]
        return dummy.next
