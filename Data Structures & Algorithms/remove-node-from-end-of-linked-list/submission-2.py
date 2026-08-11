# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        sz = 0

        while curr:
            curr = curr.next
            sz += 1

        stop = sz - n
        if stop == 0:
            return head.next

        curr = head
        while stop > 1:
            curr = curr.next
            stop -= 1
        
        
        curr.next = curr.next.next
        return head
        