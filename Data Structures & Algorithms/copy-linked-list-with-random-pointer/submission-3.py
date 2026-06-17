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
        original_to_copy = collections.defaultdict(lambda: Node(0))
        original_to_copy[None] = None

        curr = head
        while curr:
            original_to_copy[curr].val = curr.val
            original_to_copy[curr].next = original_to_copy[curr.next]
            original_to_copy[curr].random = original_to_copy[curr.random]

            curr = curr.next

        return original_to_copy[head]