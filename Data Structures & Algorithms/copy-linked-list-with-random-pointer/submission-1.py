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
        
        addresses = {None:None}
        curr = head

        while curr:
            addresses[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:   
            addresses[curr].random = addresses[curr.random]
            addresses[curr].next = addresses[curr.next]
            curr = curr.next
        
        return addresses[head]

        
        