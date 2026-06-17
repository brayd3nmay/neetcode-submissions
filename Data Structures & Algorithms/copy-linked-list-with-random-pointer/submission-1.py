"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        copy_map = {}
        curr = head
        while curr:
            copy_map[curr] = Node(curr.val)
            curr = curr.next
        
        for original, copy in copy_map.items():
            if original.next:
                copy.next = copy_map[original.next]
            if original.random:
                copy.random = copy_map[original.random]

        return copy_map[head]