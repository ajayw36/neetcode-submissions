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

        node_map = {} # old to new node
        curr, prev = head, Node(0)
        while curr:
            new_node = Node(curr.val)
            node_map[curr] = new_node
            prev.next = new_node
            prev = new_node
            curr = curr.next
        
        curr = head
        while curr:
            node_map[curr].random = node_map[curr.random] if curr.random else None
            curr = curr.next
        
        return node_map[head]
